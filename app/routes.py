from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from flask_login import login_required, login_user, logout_user, current_user
from .models import Expense, User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import csv
import io

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    category_filter = request.args.get('category')
    if category_filter:
        expenses = Expense.query.filter_by(user_id=current_user.id, category=category_filter).order_by(Expense.date.desc()).all()
    else:
        expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()

    total_amount = sum(exp.amount for exp in expenses)
    categories = db.session.query(Expense.category).distinct().filter_by(user_id=current_user.id).all()

    # Data for Chart
    category_totals = {}
    for exp in expenses:
        if exp.category in category_totals:
            category_totals[exp.category] += exp.amount
        else:
            category_totals[exp.category] = exp.amount

    return render_template('index.html', expenses=expenses, total_amount=total_amount,
                           categories=[c[0] for c in categories],
                           chart_labels=list(category_totals.keys()),
                           chart_values=list(category_totals.values()))

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        description = request.form.get('description', '')
        expense = Expense(category=category, amount=float(amount), description=description, user_id=current_user.id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_expense.html')

@main.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    if request.method == 'POST':
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.description = request.form.get('description', '')
        db.session.commit()
        flash('Expense updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_expense.html', expense=expense)

@main.route('/delete/<int:expense_id>')
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!')
    return redirect(url_for('main.index'))

@main.route('/export')
@login_required
def export_expenses():
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)

    # Write headers
    writer.writerow(['Date', 'Category', 'Description', 'Amount'])

    # Write data rows
    for exp in expenses:
        writer.writerow([exp.date.strftime('%Y-%m-%d'), exp.category, exp.description, f"{exp.amount:.2f}"])

    output.seek(0)

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=expenses.csv"})

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid login details')
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            new_user = User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.login'))
        else:
            flash('User already exists!')
    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

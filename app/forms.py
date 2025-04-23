from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    title = StringField('Expense Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Food', 'Food'), ('Transport', 'Transport'), ('Utilities', 'Utilities'), 
        ('Health', 'Health'), ('Entertainment', 'Entertainment'), ('Other', 'Other')
    ])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expense')

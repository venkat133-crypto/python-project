# SpendWise Tracker 2.0

SpendWise Tracker is a clean and simple web app to **track your daily expenses**, **visualize your spending**, and **manage your monthly budget**.

🚀 Built using **Python Flask**, **SQLite**, **Bootstrap 5**, **Chart.js** and deployed on **Render**.

---

## 🎯 Features

- ✍️ Add, Edit, Delete Expenses
- 📊 Category-wise Pie Chart Visualization
- 🧮 Set Monthly Budget & track progress
- 📈 Budget Usage Bar (with color indicators)
- 📁 Export Expenses to CSV file
- 🌓 Light/Dark Mode toggle
- 🔔 Toast Notifications (Add/Edit/Delete/Budget Save)
- 🔒 User Authentication (Register/Login/Logout)

---

## 📂 Project Structure

spendwise/ ├── app/ │ ├── init.py │ ├── models.py │ ├── routes.py │ ├── templates/ │ │ ├── base.html │ │ ├── index.html │ │ ├── add_expense.html │ │ ├── login.html │ │ ├── register.html │ │ └── settings.html │ └── static/ │ └── style.css ├── spendwise.db ├── run.py ├── init_db.py ├── requirements.txt ├── render.yaml ├── README.md
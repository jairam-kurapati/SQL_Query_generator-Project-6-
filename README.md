# 🤖 AI SQL Assistant - Natural Language to SQL Query Generator

## 📌 Project Overview

AI SQL Assistant is a Generative AI-powered web application that converts natural language questions into SQL queries automatically. Users can ask questions in plain English, and the system generates SQL queries, executes them on a SQLite database, and displays the results in a user-friendly interface.

This project combines **Python, Flask, SQLite, and Google's Gemini API** to simplify database querying for non-technical users.

---

## 🚀 Features

### ✅ Natural Language to SQL Conversion

Convert English questions into SQL queries automatically.

**Example:**

Input:

```text
Show employees earning more than 50000
```

Generated SQL:

```sql
SELECT * FROM employees
WHERE salary > 50000;
```

---

### ✅ Dynamic Database Schema Detection

The application automatically reads the database schema and provides it to Gemini for accurate SQL generation.

---

### ✅ SQL Query Explanation

Every generated SQL query is explained in simple English.

Example:

SQL:

```sql
SELECT * FROM employees WHERE salary > 50000;
```

Explanation:

```text
Retrieve all employee records whose salary is greater than 50000.
```

---

### ✅ Interactive Chat Interface

Users interact with the system using a ChatGPT-style interface.

---

### ✅ Query Execution

Generated SQL queries are executed automatically on the SQLite database.

---

### ✅ Result Display

Query results are displayed in a structured table format.

---

### ✅ Dark Mode Support

Modern UI with Light and Dark Mode toggle.

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Generative AI

* Google Gemini API

---

## 📂 Project Structure

```text
SQL Query Generator/
│
├── app.py
│
├── database/
│   ├── sample.db
│   ├── init_db.py
│   ├── schema_reader.py
│   └── __init__.py
│
├── models/
│   ├── text_to_sql.py
│   └── __init__.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── theme.js
│
├── uploads/
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd SQL-Query-Generator
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

---

### 5. Initialize Database

```bash
python database/init_db.py
```

---

### 6. Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Sample Queries

### Employees Table

```text
Show all employees
```

```text
List employees earning above 50000
```

```text
Who earns the highest salary?
```

```text
Count employees in IT department
```

---

### Students Table

```text
Show students with marks above 85
```

```text
Who scored the highest marks?
```

```text
Count students in AIML branch
```

---

### Projects Table

```text
Show all projects
```

```text
List projects longer than 2 months
```

```text
Which project uses GenAI?
```

---

## 🔮 Future Enhancements

* Database Upload Support
* CSV Export
* Query History Storage
* Chart Generation from SQL Results
* MySQL Support
* PostgreSQL Support
* User Authentication
* SQL Validation Layer
* Dashboard Analytics

---

## 🎯 Learning Outcomes

This project demonstrates:

* Prompt Engineering
* Generative AI Integration
* Flask Web Development
* Database Management
* Natural Language Processing
* SQL Query Generation
* Full Stack Development

---

## 📄 Resume Description

Developed an AI-powered Natural Language to SQL Assistant using Python, Flask, SQLite, and Google Gemini API. Implemented dynamic schema extraction, automated SQL query generation, SQL explanation, and real-time database querying through an interactive chat-based interface.

---

## 👨‍💻 Author

Jairam Kurapati

B.Tech - Artificial Intelligence & Machine Learning

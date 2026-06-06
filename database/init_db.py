import sqlite3
import os

# Create database folder if not exists
os.makedirs("database", exist_ok=True)

# Connect database
conn = sqlite3.connect("database/sample.db")
cursor = conn.cursor()

# ==========================
# EMPLOYEES TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

cursor.execute("DELETE FROM employees")

employees = [
    (1, "Rahul", "IT", 60000),
    (2, "Priya", "HR", 45000),
    (3, "Arjun", "IT", 70000),
    (4, "Sneha", "Finance", 55000),
    (5, "Kiran", "IT", 80000)
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?)",
    employees
)

# ==========================
# STUDENTS TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

students = [
    (1, "Ram", "CSE", 92),
    (2, "Sita", "AIML", 85),
    (3, "Krishna", "ECE", 78),
    (4, "Ravi", "CSE", 95),
    (5, "Anjali", "AIML", 88)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    students
)

# ==========================
# PROJECTS TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects(
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    technology TEXT,
    duration_months INTEGER
)
""")

cursor.execute("DELETE FROM projects")

projects = [
    (1, "Resume Analyzer", "Python", 2),
    (2, "Text Summarizer", "NLP", 3),
    (3, "Gender Detection", "Computer Vision", 4),
    (4, "Natural Language To SQL", "GenAI", 2)
]

cursor.executemany(
    "INSERT INTO projects VALUES (?, ?, ?, ?)",
    projects
)

# Save changes
conn.commit()
conn.close()

print("Database Created Successfully!")
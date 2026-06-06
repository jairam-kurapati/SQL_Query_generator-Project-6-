from flask import Flask, render_template, request
import sqlite3

from models.text_to_sql import generate_sql, explain_sql

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():

    global chat_history

    if request.method == "POST":

        question = request.form.get("question")

        try:

            sql_query = generate_sql(question)

            conn = sqlite3.connect("database/sample.db")
            cursor = conn.cursor()

            cursor.execute(sql_query)

            columns = []
            results = []

            if cursor.description:
                columns = [col[0] for col in cursor.description]
                results = cursor.fetchall()

            conn.close()

            explanation = explain_sql(sql_query)

            chat_history.append({
                "question": question,
                "sql": sql_query,
                "explanation": explanation,
                "columns": columns,
                "results": results,
                "error": None
            })

        except Exception as e:

            chat_history.append({
                "question": question,
                "error": str(e)
            })

    return render_template(
        "index.html",
        chat_history=chat_history
    )

if __name__ == "__main__":
    app.run(debug=True)
import os
import google.generativeai as genai

from dotenv import load_dotenv
from database.schema_reader import get_schema

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question):

    schema = get_schema()

    prompt = f"""
You are an expert SQLite SQL generator.

Database Schema:

{schema}

Rules:
1. Return only SQL.
2. No explanation.
3. No markdown.
4. No ``` blocks.
5. Use SQLite syntax only.

Question:
{question}
"""

    response = model.generate_content(prompt)

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


def explain_sql(sql):

    prompt = f"""
Explain this SQL query in simple English:

{sql}

Only return the explanation.
"""

    response = model.generate_content(prompt)

    return response.text.strip()
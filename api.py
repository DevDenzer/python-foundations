from fastapi import FastAPI
from database import get_all_expenses

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}

@app.get("/expenses")
def read_expenses():
    expenses = get_all_expenses()

    result = []

    for exp_id, category, amount in expenses:
        result.append({
            "id": exp_id,
            "category": category,
            "amount": amount
        })

    return result
from expense_model import Expense
print("Program started")
def main():
    print("=== Monthly Expense Calculator ===")

    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number...")

    income = get_float_input("Enter your monthly income:  ")

    expenses = []

    while True:
        category = input("Enter expense category (or type 'done' to finish): ")

        if category.lower() == "done":
            break

        ammount = get_float_input(f"Enter amount for {category}: ")
        expenses.append(Expense(category, ammount))

    total_expenses = sum(expense.amount for expense in expenses)

    remaining = income - total_expenses

    print("\n=== Summary ===")
    for expense in expenses:
        print(expense.display())
    print(f"Remaining Balance: ${remaining:.2f}")
    if remaining < 0:
        print("Warning: You are overspending.")

if __name__ == "__main__":
    main()
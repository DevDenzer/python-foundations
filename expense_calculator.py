print("Program started")
def main():
    print("=== Monthly Expense Calculator ===")

    income = float(input("Enter your monthly income:  "))
    rent = float(input("Enter your monthly rent:  "))
    food = float(input("Enter your food expenses:  "))
    other = float(input("Enter your other expenses:  "))

    total_expenses = rent + food + other
    remaining = income - total_expenses

    print("\n=== Summary ===")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining:.2f}")
    if remaining < 0:
        print("Warning: You are overspending.")

if __name__ == "__main__":
    main()
expenses = {}

def add_expense():
    if expenses:
        id = max(expenses) + 1
    else:
        id = 1
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    expenses[id] = {"amount": amount, "category": category, "description": description}

def show_expenses():
    if not expenses:
        print("No expenses to display.")
        return
    for id, expense in expenses.items():
        print(f"ID: {id}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def show_expenses_by_category(category):
    found = False
    for id, expense in expenses.items():
        if expense['category'] == category:
            print(f"ID: {id}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
            found = True
    if not found:
        print(f"No expenses found in category '{category}'.")

def delete_expense(expense_id):
    if expense_id in expenses:
        del expenses[expense_id]
        print(f"Expense with ID {expense_id} deleted.")
    else:
        print(f"Expense with ID {expense_id} not found.")


def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Show expenses by category")
        print("4. Delete expense")
        print("5. Exit")
        choice = input("Choose an action (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            category = input("Enter the category: ")
            show_expenses_by_category(category)
        elif choice == "4":
            expense_id = int(input("Enter the expense ID to delete: "))
            delete_expense(expense_id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose an action from 1 to 5.")

if __name__ == "__main__":
    main()

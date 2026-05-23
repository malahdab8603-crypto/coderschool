import csv

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category):
        """Adds an expense using a tuple."""
        expense = (amount, category)
        self.expenses.append(expense)
        print(f"Added expense: ${amount} for {category}.")

    def view_expenses(self):
        """Displays all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nExpenses:")
        for amount, category in self.expenses:
            print(f"- ${amount} for {category}")

    def save_expenses(self):
        """Saves expenses to a CSV file."""
        with open("expenses.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.expenses)
        print("Expenses saved.")

    def load_expenses(self):
        """Loads expenses from a CSV file."""
        try:
            with open("expenses.csv", "r") as f:
                reader = csv.reader(f)
                self.expenses = [tuple(row) for row in reader]
        except FileNotFoundError:
            self.expenses = []

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(amount, category)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.save_expenses()
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

#*****************************************************************************************************
#Expense Tracker is a university project developed for Caltech PG program for AI & ML
#Auther: Shibu Mathew
#Project Submission date : 25-OCT-2024
#*****************************************************************************************************

import csv
import os

# Initialize global variables
expenses = []
monthly_budget = 0

# 1. Function to add an expense
def add_expense():
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    description = input("Enter a brief description of the expense: ")

    # Store expense in a dictionary
    expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
    expenses.append(expense)
    print("Expense added successfully!")

# 2. Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses to display.")
        return
    
    for expense in expenses:
        date = expense.get('date')
        category = expense.get('category')
        amount = expense.get('amount')
        description = expense.get('description')
        
        # Validate data before displaying
        if date and category and amount and description:
            print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")
        else:
            print("Incomplete expense found, skipping...")
    
# 3. Set and track budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {monthly_budget}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def track_budget():
    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return
    
    total_expenses = sum(expense['amount'] for expense in expenses)
    if total_expenses > monthly_budget:
        print(f"Warning: You have exceeded your budget! Total expenses: {total_expenses}")
    else:
        remaining_budget = monthly_budget - total_expenses
        print(f"You have {remaining_budget} left for the month.")

# 4. Save and load expenses
def save_expenses_to_file():
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved to expenses.csv")

def load_expenses_from_file():
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    'date': row['date'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                    'description': row['description']
                })
        print("Expenses loaded from expenses.csv")
    else:
        print("No saved expenses file found.")

# 5. Interactive menu
def display_menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")

def main():
    load_expenses_from_file()  # Load saved expenses at startup
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if monthly_budget == 0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses_to_file()
        elif choice == '5':
            save_expenses_to_file()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid choice.")

if __name__ == "__main__":
    main()


#--------END-------#

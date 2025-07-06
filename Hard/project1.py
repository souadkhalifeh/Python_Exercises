# 🧠 Project 1 – Expense Tracker CLI App
# | A full program combining file I/O, classes, user input, conditionals, lists, and dictionaries. 📌 Objective:

# Create a command-line expense tracker where users can:

# Add a new expense (category, amount, date)
# View all expenses
# View total spent per category
# Save & load expenses from a CSV file
# 🧩 Features:

# Expense class: holds category, amount, date
# ExpenseManager class:
# .add_expense()
# .view_expenses()
# .category_summary()
# .save_to_csv() and .load_from_csv()
# | Note: You can skip the hard section until you finish the Machine Learning Practice Course,
# Because it includes the libraries that you want to work with in order to read and write csv, such as Pandas


import csv 

class Expense:
    def __init__(self,category, amount,date):
        self.category = category
        self.amount = amount
        self.date = date
    def __str__(self):
        return f"{self.date}: {self.category} - ${self.amount:.2f}"

class ExpenseManager:
    def __init__(self):
        self.expenses = []
                
    def add_expense(self, category, amount, date):
        expense = Expense(category, amount, date)
        self.expenses.append(expense)
        print("Expense added successfully!")
        
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for expense in self.expenses:
            print(expense)
    
    
    def category_summary(self, expenses):
        summary={}
        for expense in expenses:
                summary[expense.category] = summary.get(expense.category, 0) + expense.amount
        print("\nTotal spent per category:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
                            
    def load_from_csv(self, filename):
        try: 
            with open (filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses.clear()
                for row in reader:
                    self.add_expense(row['Category'],row['Amount'], row['Date'])       
            print(f"Expenses loaded from '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            
    def save_to_csv(self, filename):
        with open(filename,'w')as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Amount', 'Date'])
            for expense in self.expenses:
                writer.writerow([expense.category, expense.amount, expense.date])     
            print(f"Expenses saved to '{filename}'")    
                   
                   
                   
def main():
    manager=ExpenseManager()
    filename = "expenses.csv"
    
    while True:
        print("\nExpense Tracker CLI")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View total spent per category")
        print("4. Save to CSV")
        print("5. Load from CSV")
        print("6. Exit")
        
        choice =input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            category = input("Enter category: ").strip()
            amount = float(input("Enter amount: ").strip())
            date = input("Enter date (YYYY-MM-DD): ").strip()
            manager.add_expense(category, amount, date)
        elif choice == '2':
            manager.view_expenses()
        elif choice == '3':
            manager.category_summary(manager.expenses)        
        elif choice == '4':
            manager.save_to_csv(filename)   
        elif choice == '5':
            manager.load_from_csv(filename)
        elif choice == '6':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
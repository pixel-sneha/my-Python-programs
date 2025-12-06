print("Welcome to the Daily Expense Tracker!\n")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expense_count = 1
expense = []
while True:
    choice = int(input())
    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    if choice == 1:
        expense.append(float(input()))
        print("Expense added successfully!")
        expense_count += 1
    if choice == 2:
        if expense:
            print("Your expenses:")
            for i in range(1,expense_count):
                print(f"{i}. {expense[i-1]}")
        else:
            print("No expenses recorded yet.")

            

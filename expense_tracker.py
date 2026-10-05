import csv
import os

expenses = []

if os.path.exists("expenses.csv"):
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            expenses.append((category, amount))

while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Highest Expense")
    print("5. View Category-wise Spending")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses.append((category, amount))

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            for category, amount in expenses:
                print("Category:", category)
                print("Amount:", amount)
                print()

    elif choice == "3":
        total = sum(amount for category, amount in expenses)
        print("Total Spending:", total)

    elif choice == "4":
        if not expenses:
            print("No expenses found.")
        else:
            highest_expense = max(expenses, key=lambda x: x[1])
            print("Highest Expense Category:", highest_expense[0])
            print("Highest Expense Amount:", highest_expense[1])

    elif choice == "5":
        category_totals = {}

        for category, amount in expenses:
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        if not category_totals:
            print("No expenses found.")
        else:
            print("\nCategory-wise Spending:")

            for category, amount in category_totals.items():
                print(category + ":", amount)

    elif choice == "6":
        print("Thank you for using Personal Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
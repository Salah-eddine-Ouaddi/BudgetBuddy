from expense import Expense
from income import Income 
import calendar
import datetime

budget = 2000
Transaction_Type = ["INCOME", "EXPENSE"]

while True:
    Choosing_Trasaction = input("Select your transaction INCOME/EXPENSE :")
    if Choosing_Trasaction == "EXPENSE" :
        def main():
            print(f"🎯 Running Budget Tracker!")
            expense_file_path = "Budget_history.csv"
        
           
            expense = get_user_expense()
            
            save_expense_to_file(expense, expense_file_path)
        
            summarize_expenses(expense_file_path, budget)
        
        
        def get_user_expense():
            print(f"🎯 Getting User Expense")
            expense_name = input("Enter expense name: ")
            expense_amount = float(input("Enter expense amount: "))
            expense_categories = [
                "🍔 Food",
                "🏠 Home",
                "💼 Work",
                "🎉 Fun",
                "✨ Others",
            ]
        
            while True:
                print("Select a category: ")
                for i, category_name in enumerate(expense_categories):
                    print(f"  {i + 1}. {category_name}")
        
                value_range = f"[1 - {len(expense_categories)}]"
                selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
                if selected_index in range(len(expense_categories)):
                    selected_category = expense_categories[selected_index]
                    new_expense = Expense(
                        name=expense_name, categorie=selected_category, amount=expense_amount
                    )
                    return new_expense
                else:
                    print("Invalid category. Please try again!")
        
        
        def save_expense_to_file(expense: Expense, expense_file_path):
            print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
            with open(expense_file_path, "a", encoding="utf-8") as f:
                f.write(f"{expense.name},{expense.amount},{expense.categorie}\n")
        
        
        def summarize_expenses(expense_file_path, budget):
            print(f"🎯 Summarizing User Expense")
            expenses: list[Expense] = []
            with open(expense_file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    expense_name, expense_amount, expense_category = line.strip().split(",")
                    line_expense = Expense(
                        name=expense_name,
                        amount=float(expense_amount),
                        categorie=expense_category,
                    )
                    expenses.append(line_expense)
        
            amount_by_category = {}
            for expense in expenses:
                key = expense.categorie
                if key in amount_by_category:
                    amount_by_category[key] += expense.amount
                else:
                    amount_by_category[key] = expense.amount
        
            print("Expenses By Category 📈:")
            for key, amount in amount_by_category.items():
                print(f"  {key}: ${amount:.2f}")
        
            total_spent = sum([x.amount for x in expenses])
            print(f"💵 Total Spent: ${total_spent:.2f}")
        
            remaining_budget = budget - total_spent
        
            now = datetime.datetime.now()
            days_in_month = calendar.monthrange(now.year, now.month)[1]
            remaining_days = days_in_month - now.day
        
            daily_budget = remaining_budget / remaining_days
            if daily_budget >= 0:
                print(f"✅ Budget Remaining: ${remaining_budget:.2f}")
                print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))
            else:
                print("Your Budget has run out!! 🆘")
        
        
        def green(text):
            return f"\033[92m{text}\033[0m"
        
        if __name__ == "__main__":
            main() 
    elif Choosing_Trasaction == "INCOME" :
        
        def main():
            print(f"🎯 Running Income Tracker!")
            income_file_path = "Budget_history.csv"
        
            # Get user input for expense.
            income = get_user_income()
        
            # Write their expense to a file.
            save_income_to_file(income, income_file_path)
        
            # Read file and summarize expenses.
            summarize_incomes(income_file_path, budget)
        
        
        def get_user_income():
            print(f"🎯 Getting User Income")
            income_name = input("Enter income name: ")
            income_amount = float(input("Enter income amount: "))
            income_categories = [
                "💰 selling",
                "🏢 Bussiness",
                "💼 Work",
            ]
        
            while True:
                print("Select a category where that income comes from: ")
                for i, category_name in enumerate(income_categories):
                    print(f"  {i + 1}. {category_name}")
        
                value_range = f"[1 - {len(income_categories)}]"
                selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
                if selected_index in range(len(income_categories)):
                    selected_category = income_categories[selected_index]
                    new_income = Income(
                        name=income_name, categorie=selected_category, amount=income_amount
                    )
                    return new_income
                else:
                    print("Invalid category. Please try again!")
        
        
        def save_income_to_file(income: Income, income_file_path):
            print(f"🎯 Saving User Income: {income} to {income_file_path}")
            with open(income_file_path, "a", encoding="utf-8") as f:
                f.write(f"{income.name}, {income.amount}, {income.categorie}\n")
        
        
        def summarize_incomes(income_file_path, budget):
            print(f"🎯 Summarizing User Income")
            incomes: list[Income] = []
            with open(income_file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    income_name, income_amount, income_category = line.strip().split(",")
                    line_income = Income(
                        name = income_name,
                        amount = float(income_amount),
                        categorie = income_category,
                    )
                    incomes.append(line_income)
        
            amount_by_category = {}
            for income in incomes:
                key = income.categorie
                if key in amount_by_category:
                    amount_by_category[key] += income.amount
                else:
                    amount_by_category[key] = income.amount
        
            print("Incomes By Category 📈:")
            for key, amount in amount_by_category.items():
                print(f"  {key}: ${amount:.2f}")
        
            total_added = sum([x.amount for x in incomes])
            print(f"💵 Total Revenues: ${total_added:.2f}")
        
            new_budget = budget + total_added
        
            now = datetime.datetime.now()
            days_in_month = calendar.monthrange(now.year, now.month)[1]
            remaining_days = days_in_month - now.day     
            daily_budget = new_budget / remaining_days
            if daily_budget >= 0:
                print(f"✅ Budget Remaining: ${new_budget:.2f}")
                print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))
            else:
                print("Your Budget has run out!! 🆘")
        
        
        def green(text):
            return f"\033[92m{text}\033[0m"
    
        if __name__ == "__main__":
            main()
    else :
        print("🔄️  Enter One of the transactions suggested (INCOME/EXPENSE) and retry!! 🔄️")


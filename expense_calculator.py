expense_1=input('Enter expense name:')
category_1=input('Enter category:')
amount_1= float(input('Enter amount:'))
total_first_expense=amount_1
print('\n ----- expense summary----')
print(f'Expense : {expense_1}')
print(f'Category: {category_1}')
print(f"Amount: {amount_1} PKR")
print(f'Total spending : {total_first_expense} PKR')

expense_2 = input('Enter Expense Name:')
amount_2 = float(input('Enter amount of this expense:'))
category_2 = input('category:')
total_spending= total_first_expense+ amount_2
print('\n---- updated record-----')
print(f'Expense 1 : {expense_1} - {category_1} - {amount_1}PKR')
print(f'Expense 2 : {expense_2} - {category_2} - {amount_2}PKR')
print(f'Total spending : {total_spending} PKR')/
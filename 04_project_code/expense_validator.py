print('SMART EXPENSE TRACKER')
print('===EXPENSE VALIDATOR===')
#input leina
expense_name= input('Enter expense name: ')
category = input('Enter category: ')
amount = float(input('Enter expense amount: '))
monthly_budget = float(input('Enter monthly budget: '))

''' Samjhein:
1. expense_name aur category text hain.
2. amount aur monthly_budget numbers hain, is liye float() use hua.
3. Input ka logical order yeh hai: name → category → amount → budget.
'''

#validation order
if amount <= 0:
    print('Amount must be greater than zero.')
elif category == "":
    print('Category is required.')
elif amount > monthly_budget:
    print('Budget exceeded!')
    exceeded_budget = amount - monthly_budget
    print(f'You exceeded your budget by {exceeded_budget} PKR. ')
else:
    print('Expense added successfully.')
    remaining_budget = monthly_budget - amount
    print(f'Your remaining budget is {remaining_budget} PKR.')
    print(f'Expense: {expense_name} - Category: {category} - Amount: {amount} PKR - Remaining budget: {remaining_budget} PKR.')
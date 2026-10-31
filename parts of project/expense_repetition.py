monthly_budget=float(input('Enter monthly budget: '))
total=0
for num in range(1,4):
    expense_name=input('Enter expense name: ')
    category=input('Enter category: ').lower()
    amount=float(input('Enter amount: '))
    if amount<=0:
        print('Invalid amount.Expense skipped')
    elif category!='food' and category!='shopping' and category!='travel' and category!='bill':
        print('Invalid category. Expense skipped.')
    else:
        print(f'Expense added: {expense_name}')
        total=total+amount
print(f'Your total expense is {total} PKR.')
remaining_budget=monthly_budget-total
print(f'Your remaining budget is {remaining_budget} PKR.')

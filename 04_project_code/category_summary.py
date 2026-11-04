# empty transaction leina
transaction=[]
# tamam categories ko start mei total 0 krna
food_total = 0
bill_total=0
travel_total=0
shopping_total=0
# 3 dafa expenses leina
for x in range(1,4):
    expense_name=input('Enter expense name: ')
    amount=float(input('Enter expense amount: '))
    category=input('Enter expense category: ').lower()
    if amount <=0:
        print('Amount must be greater than 0.Transaction skipped')
    elif category=="":
        print('category required.')
    elif category!='food' and category!='shopping' and category!='travel' and category!='bill':
        print('Invalid category! Transaction skipped.')
    else:
        print('Expense added sucessfully.')
        single_list={
            'name':expense_name,
            'amount':amount,
            'category':category
        }
        transaction.append(single_list)
for num in transaction:
    if num['category']=='food':
        food_total=food_total+num['amount']
    elif num['category'] == 'bill':
        bill_total=bill_total+num['amount']
    elif num['category'] == 'shopping':
        shopping_total=shopping_total+num['amount']
    elif num['category'] == 'travel':
        travel_total=travel_total+num['amount']

print(f'food spending: {food_total} PKR.')
print(f'bills spending: {bill_total} PKR.')
print(f'shopping spending: {shopping_total} PKR.')
print(f'travel spending: {travel_total} PKR.')


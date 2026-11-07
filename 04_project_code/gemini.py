expense=[]
while True:
    print('=== SELECT THE CHOICE GIVEN BELOW ===')
    print('1.Add Expense.')
    print('2.View Expense.')
    print('3.Exit.')
    choice=input('Enter your choice: ').lower()
    if choice=='1':
        expense_name=input('Enter expense name: ')
        amount=float(input('Enter expense amount: '))
        category=input('Enter expense category: ')
        if amount<=0:
            print('Amount must be greater than 0.')
            break
        elif category=="":
            print('category required')
            break
        else:
            print('Expense added successfully.')
        single_expense={'name':expense_name,'amount':amount,'category':category}
        expense.append(single_expense)
    elif choice == '2':
        total_amount=0
        if len(expense)==0:
            print('abhi tuk koi expense add nhi hei')
        else:
            for x in expense:
                print(f"Expense is {x['name']} or amount is {x['amount']} PKR or category is {x['category']}.")
                total_amount = total_amount+x['amount']
        print(f'total amount is {total_amount} PKR.')
    else:
        print('Thanks for using our service.')
        break
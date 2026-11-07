# task 1 
def sara(name):
    return(f'welcome,{name}!')
print(sara('arooj'))
print(sara('sara'))
# task 2 
def calculate_total(amount1,amount2):
    total = amount1 +amount2
    return total
print(calculate_total(800,200))
print(calculate_total(500,300))

transaction=[]
def validate_amount(amount):
    if amount <=0:
        return('Amount must be greater than 0.Transaction skipped')
    else:
        return('Expense added sucessfully.')

print(validate_amount(-20))

# 🎯 Practice Challenge: Rectangle Stats
# Aapko ek aisi function banani hai jo aik rectangle ki length aur width input (parameters) ke tor par le, aur do cheezein return kare:

# Area (Formula: length * width)

# Perimeter (Formula: 2 * (length + width))
def rec(length,width):
    area=length*width
    perimeter=2*(length+width)
    return area,perimeter
box_area,box_perimeter=rec(200,600)
print(box_area)
print(box_perimeter)


# Ab validate_category function banayein.

# Requirements:

# text
# Function name: validate_category
# Parameter: category
# Valid categories: Food, Travel, Shopping
# Valid → True
# Invalid → False

def validate_category(category):
    if category in ['food','travel','shopping']:
        return True
    else:
        return False
user_category=validate_category(input('enter category: ').lower())
print(user_category)

# better version 
valid_categories =['food','shopping','travel']
def function_name(category):
    return category in valid_categories
list_category=function_name(input('enter category: ').lower())
print(list_category)

# Ab hum dono validations ko use karenge.

# Task:

# User se amount input lein

# User se category input lein

# Agar amount valid ho aur category valid ho:

#     print: Expense added successfully.

# Warna:

#     print: Invalid amount or category. Transaction skipped.
def val_amount(amount): 
    return amount>0
def val_category(category):
    return category  in ['food','travel','shopping','bills']
user_amount=val_amount(float(input('Enter amount: ')))
user_category=val_category(input('Enter category: ').lower())
if user_amount and  user_category:
    print('Expense added successfully.')
else:
    print('Invalid amount or category. Transaction skipped.')


#    Ek function banayein: add_expense

# Parameters:
#     amount
#     category

# Logic:
#     Agar amount valid ho aur category valid ho:
#         return 'Expense added successfully.'
#     Warna:
#         return 'Invalid amount or category. Transaction skipped.'
valid_category=['food','shopping','travel','bills']
def add_expense(amount,category):
    if val_amount(amount) and val_category(category):
        return "Expense added successfully."
    else:
        return "Invalid amount or category.Transaction skipped."
print(add_expense(800,'food'))
print(add_expense(800,'health'))
print(add_expense(-50,'food'))
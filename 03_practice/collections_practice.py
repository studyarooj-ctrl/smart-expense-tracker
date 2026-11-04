print('==== list practice====')

# eik list banayein jisme 4 categories hon food,travel,shopping or bills
# phir
# 1. Pehli category print karein
# 2. Aakhri category print karein
# 3. List ki length print karein

categories=['food','travel','shopping','bills']
print(categories[0])
print(categories[-1])
print(len(categories))


# uper wali list mei health category add krein

categories=['food','travel','shopping','bills']
categories.append('health')
print(categories)

# ab shopping item ko list se remove krein

categories=['food','travel','shopping','bills']
categories.remove('shopping')
print(categories)


print('=== tuples practice ===')

# eik tuple banayein jisme 3 values  hon 15,august,2000
# phir
# 1. Pehli value print karein
# 2. Aakhri value print karein
# 3. tuple ki length print karein

tuple_name=(15,'august',2000)
print(tuple_name[0])
print(tuple_name[-1])
print(len(tuple_name))

print('=== dictionary practice===')


 
# Ek dictionary banayein jisme yeh 3 key-value pairs hon:
# name → Lunch
# category → food
# amount → 800
# phir
# 1. name print karein
# 2. category print karein
# 3. amount print karein
# 4. Dictionary mein naya pair add karein: date → 2026-11-02
# 5. Poori dictionary print karein

record={
 'name':'lunch',
 'category':'food',
 'amount':800
}
print(record['name'])
print(record['category'])
print(record['amount'])
record['date']='2026-11-02'
print(record)

print('=== nested data practice===')


# ek list banayein jisme 2 dictionaries ho
# Pehli expense:
# name → Lunch
# category → food
# amount → 800

# Doosri expense:
# name → Rickshaw
# category → travel
# amount → 120
# PythonFinalizationError1. Pehli expense ka name print karein
# 2. Doosri expense ka amount print karein
# 3. Dono expenses ke names loop se print karein
# Loop se har expense ka name aur amount print karein.

list_name = [
    {
        'name':'Lunch',
        'category':'food',
        'amount':800
    }
    ,
    {
        'name':'Rickshaw',
        'category':'travel',
        'amount':120
    }
]

# 1. Pehli expense ka name print karein
print(list_name[0]['name'])
# 2. Doosri expense ka amount print karein
print(list_name[1]['amount'])
# 3. Dono expenses ke names loop se print karein
for x in list_name:
    print(x['name'])
# Loop se har expense ka name aur amount print karein.
for x in list_name:
    print(f'name are {x["name"]} or amount are {x["amount"]}')


# Ek list banayein: ['food', 'travel', 'shopping', 'bills']
# Index 2 wali category ko 'health' se replace karein
# Poori list print karein
list_name=['food','shopping','travel','bills']
list_name[2]='health'
print(list_name)

#Ek dictionary banayein:
# name → Lunch
# category → food
# amount → 800

# Amount ko 1000 se replace karein.
# Poori dictionary print karein.
dic_name={
    'name':'lunch',
    'category':'food',
    'amount':800
}
dic_name['amount']=1000
print(dic_name)


print('==== test===')
# guided exercise 1
exercise_1=['food','shopping','travel','bill']
print(exercise_1[0])
print(exercise_1[-1])
print(len(exercise_1))
exercise_1.append('health')
exercise_1.remove('shopping')
print(exercise_1)
#guided exercise 2
exercise_2={
    'name':'lunch',
    'category':'food',
    'amount':800
}
print(exercise_2['name'])
print(exercise_2['amount'])
exercise_2['amount']=1000
exercise_2['date']='2026-11-03'
print(exercise_2)
# independent exercise 
transaction=[
    {
       'name':'lunch',
        'category':'food',
        'amount':800 
    },
    {
        'name':'movie',
        'category':'entertainment',
        'amount':500 
    },
    {
        'name':'grocery',
        'category':'shopping',
        'amount':1500 
    }
]
total=0

print(transaction[0]['name'])
print(transaction[1]['amount'])
print(transaction[2]['category'])
for x in transaction:
    print(x['name'])
for x in transaction:
    print(x['amount'])
    total=total+x['amount']
print(f'Total amount: {total}')
print()

print('===data structure===')
transactions = [
    {
        'name': 'Lunch',
        'category': 'food',
        'amount': 800
    },
    {
        'name': 'Rickshaw',
        'category': 'travel',
        'amount': 120
    },
    {
        'name': 'Grocery',
        'category': 'shopping',
        'amount': 1500
    },
    {
        'name': 'Electricity',
        'category': 'bills',
        'amount': 900
    },
    {
        'name': 'Tea',
        'category': 'food',
        'amount': 200
    }
]
food_total = 0
bills_total=0
shopping_total=0
travel_total=0
for x in transactions:
    if x['category'] == 'food':
        food_total = food_total+x['amount']
    if x['category'] == 'bills':
        bills_total=bills_total+x['amount']
    if x['category']=='shopping':
         shopping_total=shopping_total+x['amount']
    if x['category']=='travel':
        travel_total=travel_total+x['amount']
print(f'food spending: {food_total}')
print(f'bills spending: {bills_total}')
print(f'shopping spending: {shopping_total}')
print(f'travel spending: {travel_total}')
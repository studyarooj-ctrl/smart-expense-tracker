# collections

jub ziada data store krna ho mean eik variable mei multiple values store krna ho toh collections use hoti hei.

## types of collections

- list
- tuple
- dictionary
- set

## list

List ek aisi collection hai jisme aap kai values ek naam ke saath store karti hain

example

```
shopping_items = ["Doodh", "Anday", "Bread", "Chai"]
```

### syntax

```
list_name = [item1, item2, item3]
```

### index

List mein har item ka position number hota hai, jise index kehte hain. Index 0 se start hota hai. categories = \["food", "travel", "shopping", "bills"\] Index 0 → food Index 1 → travel Index 2 → shopping Index 3 → bills " access krne ka tariqa ' print(categories\[0\])

### list is changeable

hum esme se item add or remove kr skty hein

- 

1. append() add krne ke liye categories = \["food", "travel"\] categories.append("bills") print(categories) \['food', 'travel', 'bills'\]

- 

2. remove() item remove krne ke liye categories=\['food','travel','bills'\] categories.remove("travel") print(categories) \['food', 'bills'\]

## tuple

same list ki terhan hei but ye changeable nhi hei,eska syntax list se different hei

### synatx of tuple

```
tuple_name = (item1, item2, item3) suitable for date of birth kuke woh change nhi hoti
```

### example

date_of_birth = (15, "August", 2000)

## dictionary

Dictionary key-value pairs store karti hai.

### syntax of dictionary

```
dict_name = { "key1": value1, "key2": value2 }
```

### syntax rules

her key value pair ke baad comma lagana esme append nhi hota

### example of dictionary

expense = { "name": "Lunch", "category": "food", "amount": 800 }

### key ki value access krne ka method

print(expense\["name"\]) output: lunch

### Dictionary mein naya key-value add karna

expense\["date"\] = "2026-11-02" print(expense) output: {'name': 'Lunch', 'category': 'food', 'amount': 800, 'date': '2026-11-02'}

### Dictionary change karna

expense\["amount"\] = 900 print(expense\["amount"\]) output: {'name': 'Lunch', 'category': 'food', 'amount': 900, 'date': '2026-11-02'}

## nested data

Nested data kya hai? Jab ek collection ke andar doosri collection ho, to usay nested data kehte hain. List of dictionaries Yeh sab se important nested structure hai: expenses = \[ { "name": "Lunch", "category": "food", "amount": 800 }, { "name": "Rickshaw", "category": "travel", "amount": 120 } \]

### Nested data access

print(expenses\[0\]\["name"\]) output:lunch

## mistakes

- 

1. in index categories = \["food", "travel"\] print(categories\[4\]) mistake: index 4 exit nhi krta (error ayega)

- 

2. in mutability categories.append("food", "travel") mistake:append() ek waqt mein sirf ek item leta hai. Do items add karne ke liye do dafa append() karna hoga.

- 

3. in dic print(expense\[name\]) Mistake: name ke around quotes nahi hain. Python name ko variable samjhega. sahi: print(expense\["name"\])

- 

4. in dic print(expense\["price"\]) price key exist nahi karti, is liye error aayega: error: KeyError: 'price'

## active recall questions

1. List aur tuple ka main farq kya hai?
2. List ka index 0 se start hota hai ya 1 se?
3. Dictionary mein key aur value ka kya role hota hai?
4. List of dictionaries kya hoti hai?
5. expenses\[0\]\["amount"\] ka matlab kya hai?

## answers

1. list is changeable or tuple is not changeable
2. 0 se start hota hei index list ka
3. key value ka label hota hei mean us value ka naam hota hei
4. aisi list jisky ander multiple dctionaries hon
5. eska mtlb list ka first dictionary mei se amount label ki value nikalna
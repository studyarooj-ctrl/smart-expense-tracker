# functions

[Function ](../03_practice/functions.py#L7)ek named code block hai jo ek specific kaam karta hai aur jab chahen call kiya ja sakta hai.

## parameter

Parameter → function banate waqt ka input placeholder

## argument

Argument → function call karte waqt di gayi actual value

Argument wo **actual value** hoti hai jo aap function call karte waqt deti hain.

```
def calculate_total(amount1, amount2):
    return amount1 + amount2

total = calculate_total(800, 200)
amount1, amount2 → parameters
800, 200 → arguments
```

### simple rule

Function definition mein → parameter

Function call mein → argument

**example**

```
def greet(name):      # name → parameter
    print(f'Hello, {name}!')

greet('Arooj')        # 'Arooj' → argument
```

yahan

```
name → parameter
'Arooj' → argument
```

## return keyword

return result deita hei

example

```
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

## scope of variables

### local variable

Function ke andar banta hai, bahar access nahi hota.

### global variable

function ke bahir bnta hei

**global variable function ke andar read kiya ja sakta hai.**

```
monthly_budget = 5000

def check_budget(total):
    if total > monthly_budget:
        print('Budget exceeded')
    else:
        print('Within budget')

check_budget(3000)
#output is 
Within budget
```

## function naming rules

same as variable naming rules

✅ Letters, numbers, underscore allowed

✅ Number se start nahi kar sakte

✅ Space allowed nahi

✅ Python keyword use nahi kar sakte, jaise if, for, while

✅ Small letters + underscore recommended

## functions practice questions

.

### 1. 🎯 Practice Challenge: Rectangle Stats

Aapko ek aisi function banani hai jo aik rectangle ki **length** aur **width** input (parameters) ke tor par le, aur do cheezein **return** kare:

1. **Area** (Formula: `length * width`)

2. **Perimeter** (Formula: `2 * (length + width)`)

### [see code here line 22](../03_practice/functions.py#L22)

### 2. validate_category function

```python
# Ab validate_category function banayein.

# Requirements:

# text
# Function name: validate_category
# Parameter: category
# Valid categories: Food, Travel, Shopping
# Valid → True
# Invalid → False
```

[see code here line 37](../03_practice/functions.py#L37)

### 3. Next: Combine validation

Ab hum dono validations ko use karenge.

Task:

User se amount input lein

User se category input lein

Agar amount valid ho aur category valid ho:

    print: Expense added successfully.

Warna:

    print: Invalid amount or category. Transaction skipped.

[see code here line 63](../03_practice/functions.py#L63)

## 4. Expense Tracker structure

Ek function banayein: add_expense

Parameters:

    amount

    category

Logic:

    Agar amount valid ho aur category valid ho:

        return 'Expense added successfully.'

    Warna:

        return 'Invalid amount or category. Transaction skipped.'

[see code line 90](../03_practice/functions.py#L90)
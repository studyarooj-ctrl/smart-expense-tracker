# shortcuts

##  String-only Methods

| Method | Use | Example | Result |
| --- | --- | --- | --- |
| `.lower()` | Small letters | `'FOOD'.lower()` | `'food'` |
| `.upper()` | Capital letters | `'food'.upper()` | `'FOOD'` |
| `.strip()` | Extra spaces hatana | `' food '.strip()` | `'food'` |
| `.replace()` | Text replace | `'food'.replace('f', 'b')` | `'bood'` |
| `.split()` | String ko list banana | `'food travel'.split()` | `['food', 'travel']` |
| `.startswith()` | Start check | `'food'.startswith('f')` | `True` |
| `.endswith()` | End check | `'food'.endswith('d')` | `True` |
| `.find()` | Text ki position | `'food'.find('o')` | `1` |
| `.count()` | Kitni dafa aya | `'food'.count('o')` | `2` |
| `.join()` | List ko string banana | `'-'.join(['a', 'b'])` | `'a-b'` |

## List-only Methods

| Method | Use | Example | Result |
| --- | --- | --- | --- |
| `.append()` | End mein item add | `expenses.append(item)` | List update |
| `.insert()` | Specific position par add | `items.insert(0, 'food')` | List update |
| `.remove()` | Value delete | `items.remove('food')` | List update |
| `.pop()` | Last ya index se delete | `items.pop()` | Deleted item |
| `.sort()` | List sort | `items.sort()` | Sorted list |
| `.reverse()` | Ulta karna | `items.reverse()` | Reversed list |
| `.count()` | Kitni dafa value hai | `items.count('food')` | Number |
| `.index()` | Value ki position | `items.index('food')` | Index |
| `.copy()` | List copy | `items.copy()` | New list |
| `.clear()` | Sab delete | `items.clear()` | Empty list |

## Dictionary Methods

| Method | Use | Example |
| --- | --- | --- |
| `.keys()` | Sirf keys | `expense.keys()` |
| `.values()` | Sirf values | `expense.values()` |
| `.items()` | Key + value pairs | `expense.items()` |
| `.get()` | Safe value access | `expense.get('amount')` |
| `.update()` | Dictionary update | `expense.update({'amount': 900})` |
| `.pop()` | Key delete | `expense.pop('amount')` |

## Functions

| Keyword | Use | Example |
| --- | --- | --- |
| `def` | Function define karna | `def val_amount(amount):` |
| `return` | Function ka output dena | `return amount > 0` |
| `print()` | Output dikhana | `print('Hello')` |
| `input()` | User se input lena | `input('Enter amount: ')` |
| `float()` | Number mein convert | `float('800')` |
| `int()` | Whole number mein convert | `int('800')` |
| `str()` | String mein convert | `str(800)` |
| `len()` | Length nikalna | `len('food')` → `4` |

## Loops

| Keyword | Use | Example |
| --- | --- | --- |
| `for` | List, string, range par repeat | `for item in expenses:` |
| `while` | Jab tak condition True ho | `while amount <= 0:` |
| `range()` | Number sequence banana | `range(5)` → `0,1,2,3,4` |
| `break` | Loop foran rokna | `break` |
| `continue` | Current iteration skip | `continue` |
| `enumerate()` | Index + value dono lena | `for i, item in enumerate(expenses):` |

## if / elif / else

| Keyword | Use | Example |
| --- | --- | --- |
| `if` | Pehli condition check | `if amount > 0:` |
| `elif` | Agli condition check | `elif category == 'food':` |
| `else` | Baqi sab cases | `else:` |
| `and` | Dono conditions | `if a and b:` |
| `or` | Koi ek condition | `if a or b:` |
| `not` | Condition invert | `if not valid:` |

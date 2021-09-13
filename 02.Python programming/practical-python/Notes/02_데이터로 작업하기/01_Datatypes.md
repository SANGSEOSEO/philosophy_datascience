[Contents](../Contents.md) \| [Previous (1.6 Files)](../01_Introduction/06_Files.md) \| [Next (2.2 Containers)](02_Containers.md)

# 2.1 Datatypes and Data structures

This section introduces data structures in the form of tuples and dictionaries.

### Primitive Datatypes

Python has a few primitive types of data:

* Integers
* Floating point numbers
* Strings (text)

We learned about these in the introduction.

### None type

```python
email_address = None
```

`None` is often used as a placeholder for optional or missing value. It evaluates as `False` in conditionals.

```python
def send_email(email_address, msg):
    pass

if email_address:
    msg = "Sending msg"
    send_email(email_address, msg)
else:
    pass
```

### Data Structures

Real programs have more complex data. For example information about a stock holding.

```code
100 shares of GOOG at $490.10
```

This is an "object" with three parts:

* Name or symbol of the stock ("GOOG", a string)
* Number of shares (100, an integer)
* Price (490.10 a float)

### Tuples

A tuple is a collection of values grouped together.

Example:

```python
s = ('GOOG', 100, 490.1)
```

Sometimes the `()` are omitted in the syntax.

```python
s = 'GOOG', 100, 490.1
```

Special cases (0-tuple, 1-tuple).

```python
t = ()            # An empty tuple
w = ('GOOG', )    # A 1-item tuple
```

Tuples are often used to represent *simple* records or structures.
Typically, it is a single *object* of multiple parts. A good analogy: *A tuple is like a single row in a database table.*

Tuple contents are ordered (like an array).

```python
s = ('GOOG', 100, 490.1)
stock_name = s[0]
shares = s[1]
price = s[2]

print(stock_name, shares, price)
```

However, tuple's values cannot be modified. Tuple object is immutable.

```
# Ttuple is immutable.
s[1] = 300   # TypeError: 'tuple' object does not support item assignment
```

You can, however, make a new tuple based on a current tuple.

```python
s1 = (stock_name, price, shares)
print(type(s1), s1)
```

### Tuple Packing

Tuples are more about packing related items together into a single entity.

```python
s = ('GOOG', 100, 490.1)
```

The tuple is then easy to pass around to other parts of a program as a single object.

### Tuple Unpacking

To use the tuple elsewhere, you can unpack its parts into variables.

```python
s2 = ('GOOG', 100, 490.1)
stock_name, shares, price = s2
print(stock_name, shares, price)
```

The number of variables on the left must match the tuple structure.

```python
# tuple should be matched the original tuples
stokc_name, shares = s2
print(stock_name, shares)

ValueError: too many values to unpack (expected 2)
```

### Tuples vs. Lists

Tuples look like read-only lists. However, tuples are most often used for a single items consisting of multiple parts. Lists are usually a collection of distinct items, usually all of the same type.

```python
record = ('GOOG', 100, 490.1)  # A tuple representing a portpolio
symbols = ['GOOG', 'AAPL', 'IBM'] # A list representing three stock symbols
```

### Dictionaries

A dictionary is mapping of keys to values. It's also sometimes called a hash table or associative array. The keys serve as indices for acceesing values.

```python
s = {
    "name": 'GOOG',
    "shares": 100,
    "price": 490.1
}
```

### Common operations

To get values from a dictionary use the key names.

```python
# to get values from dictionary datatype
print("{}주식을 {}개 보유".format(s["name"], s["shares"]))
```

```
GOOG주식을 100개 보유
```

To add or modify values assign using the key names.

To add or modify values assign using the key names.



```python
# to add or modify values assign using the key names
s["shares"] = 75
s["data"] = '2021-09-11'

print("현재 주식 보유 ", s)
```

```
현재 주식 보유  {'name': 'GOOG', 'shares': 75, 'price': 490.1, 'data': '2021-09-11'}
```

To delete a value using `del`

```python
# 삭제
del s["date"]
print(s)
```

```
{'name': 'GOOG', 'shares': 75, 'price': 490.1}
```

### Why dictionaries?

Dictionaries are useful when there are many different vlaues and those values might be modified or manipulated. Dictionaries make your code more readable.

```python
s['price']
# vs
s[2]
```

## Exercises

In the last few excercises, you wrote a program that read a datafile `Data/protfolio.csv`. Using the `.csv` module , it is easy to read the file row-by-row.

```python
import csv

f = open("Data/portfolio.csv")
rows = csv.reader(f)
print(next(rows))

row = next(rows)
print(row)
```

```
['name', 'shares', 'price']
['AA', '100', '32.20']
```

Although reading the file is easy, you often want to do more with the data than read it. For instance, perhaps you want to store it and start performing some calculations on it.

Unfortunately, a raw "row" of data doesn't give you enought to work with. For example, even a simple math calculation doesn't work.

```python
row = ["AA", "100", "32.20"]
cost = row[1] * row[2]
```

```
TypeError: can't multiply sequence by non-int of type 'str'
```

To do more, you typically want ot interpret the raw data in some way and turn it into a more useful kind of object so that you can work with it later.

Two simple options are tuples or dictionaries.

### Exercise 2.1: Tuples

At the interactive prompt, create the folowing tuple that represents the above row, but with the numeric columns converted to proper numbers:

```python
t = (row[0], int(row[1]), float(row[2]))
print(t)  # ('AA', 100, 32.2)
```

Using this, you can now calculate the total cost by mltiplying the shares and the price:

```python
cost = t[1] * t[2]
print(cost)   # 3220.0000000000005
```

Is math broken in Python?  What's the deal with the answer of 3220.0000000000005?

This is an artifact of the floating point hardware on your computer only being able to accuracy represent decimals in Base-2, not Base-10. 

For event simple calculatoions involving base-10 decimals, small errors are introduced.This is normal, although perhaps a bit surprising if you haven't seen it before.

This happens in all programming languages that use floating point decimals, but it often gets hidden when printing. 

For example:

```python
>>> print(f'{cost:0.2f}')
>>> 3220.00
```

Tuples are read-only. Verify this by trying to change the number of shares to 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
  File "D:/projects/myproject/Practical_Python/working_with_datatype.py", line 81, in <module>
    t[1] = 550
TypeError: 'tuple' object does not support item assignment
```

Although you can't change tuple contents, you can always create a completely new tuple that replaces the old one.

```python
>>> t = (t[0], 550, t[2])
>>  print(t)
('AA', 550, 32.2)
>>>
```

Whenever you reassing an existing variable name like this, the old value is discarded. Although the above assignment might look like you are modifying the tuple, you are actually creating a new tuple and throwing the old one away.

Tuples are often used to pack and unpack values into variables. Try the followng.

```python
>>> name, shares, price = t
>>> print(name)
>>> print(shares)
>>> print(price)

AA
550
32.2
```

Take the above variables and pack them back into a tuple

Take the above variables and pack them back into a tuple.

```python
>>> t = (name, 2 * shares, price)
>>> print(t)
('AA', 1100, 32.2)
>>>
```

### Exercise 2.2: Dictionaries as a data structure

An alternative to a tuple is to create a dictionary instead.

```python
d = {
    "name": row[0],
    "shares": int(row[1]),
    "price": float(row[2])
}
print(d)
```

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Calculate the total cost of this holding.

```python
cost = d["shares"] * d["price"]
print(f"Total profit {cost:.2f} " )
```

**Result**

```
Total profit : 3220.00
```

Compare this example with the same calculation involving tuples above. Change the number of shares to 75

```python
# Modifying dictionary
d['shares'] = 156
print("Dictionary : ", d)
```

**Result**

```
Dictionary :  {'name': 'AA', 'shares': 156, 'price': 32.2}
```

Unlike tuples, dictionaries can be freely modified. Add some attributes.

```python
>>> d["date"] = (6, 11, 2007)
>>> d["account"] = "richardgearIamaboyYourareagirl"
>>> print(d)
```

```
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
```

### Exercise 2.3: Some additional dictionary operations

If you turn a dictionary into a list, you’ll get all of its keys:

```python
>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>
```

Similary, if you use the `for` statemnet to iterate on a dictionary. you will get the keys:

```python
>>> for v in d:
       print("k = ", k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Try this variant tht performs a lookup at the same time:

```python
for k in d:
    print("{} = {}".format(k, d[k]))

name = AA
shares = 156
price = 32.2
date = (6, 11, 2007)
acount = 12345
>>>
```

You can also obtain all of the keys using the `keys()` method:

```python
# obtain all of keys
>>> keys = d.keys()
>>> print(keys)
dict_keys(['name', 'shares', 'price', 'date', 'acount'])
>>>
```

`keys()` is a bit unusual in that it returns a special `dict_keys` object. This is an overlay on the original dictionary that always give you the current keys - even if the dictionary changes. For example, try this:

```python
>>> del d['account']
>>> keys
dict_keys(['name', 'shares', 'price', 'date'])
>>>
```

Carefully notice that the `account` disappeared from `keys` even though you didn't call `d.keys()` again.

A more elegant way to wirk with keys and values together is to use the `items()` method. This gives you `(key, value)` tuples:

```python
>>> items = d.items()
>>> print(items)
dict_items([('name', 'AA'), ('shares', 156), ('price', 32.2), ('date', (6, 11, 2007)), ('acount', 12345)])
>>> for k, v in d.items():
       print(k, '=', v)

name = AA
shares = 156
price = 32.2
date = (6, 11, 2007)
>>>
```

If you have tuples such as `items`, you can create a dictionary using the `dict()` function. Try it:

```python
>>> print(items)
dict_items([('name', 'AA'), ('shares', 156), ('price', 32.2), ('date', (6, 11, 2007)), ('acount', 12345)])
>>> d = dict(items)
>>> d
dict_items([('name', 'AA'), ('shares', 156), ('price', 32.2), ('date', (6, 11, 2007)), ('acount', 12345)])
>>>
```

[Contents](../Contents.md) \| [Previous (1.6 Files)](../01_Introduction/06_Files.md) \| [Next (2.2 Containers)](02_Containers.md)

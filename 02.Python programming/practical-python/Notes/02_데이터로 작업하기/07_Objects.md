[Previous (2.6 List Comprehensions)](06_List_comprehension.md) \| [Next (3 Program Organization)](../03_Program_organization/00_Overview.md)

# 2.7 Objects

This section introduces more details about Python's internal object model and discussed some matters related to memory management , copying, and type checking.

### Assignment

Many operations in Python are related to assigning or storing values.

```python
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```

*A caution: assignment operations **never make a copy** of the value being assigned. All assignments are merely reference copies(or pointer copies if you prefer)*

### Assignment example

Consider this code fragment.

```
a = [1, 2, 3]
b = a
c = [a, b]
```

A picture of the underlying memory operations. In this example, there is only one list object `[1,2,3]`, but there are four different references to it.

![references](https://user-images.githubusercontent.com/70785000/134735855-571c3a64-3f5c-4f6b-b615-d9b7a3052461.png)

This means that modifying a value affects all references.

```
>>> a.append(999)
>>> print(a)
>>> print(b)
>>> print(c)
>>>
[1, 2, 3, 999]
[1, 2, 3, 999]
[[1, 2, 3, 999], [1, 2, 3, 999]]
```

Notice how a change in the original list shows up everywhere else. This is because no copies were made.

Everything is pointing to the same thing.

### Reassigning values

Reassigning a value never overwrites the memory used by the previous value.

```
>>> a = [1,2,3]
>>> b = a
>>> a = [4,5,6]

>>> print(a, id(a))
>>> print(b, id(b))
>>>
[4, 5, 6] 2193505236480
[1, 2, 3] 2193504891072
```

Remember: **Variables are names, not memory locations.**

### Some Dangers

If you don't know about this sharing, you will shoot yourself in the foot at some point. Typical scenario.

You modify some data thinking that it's your own private copy and it accidentally corrupts some data in some other part of the program.

*Commnet: This is one fo the reasons why the primitive datatypes(int, float, string) are immutable (read-only).*

### Identify and References

Use th `is` operatosr to check if two values are exactly the same object.

```
a = [1,2,3]
b = a
print(a is b)
>>>
True
```

`is` compares the object identify(an integer). The indentify can be obtained using `id()`.

```
print(f"a's pointer : {id(a)}")
print(f"b's pointer : {id(b)}")
>>>
a's pointer : 1614629812416
b's pointer : 1614629812416
```

Note: It is almost always better to use `==` for checking objets. The behaviour of `is` is often unexpected.

```
a = [1,2,3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)
print(a == c)
>>>
True
False
True
```

###  Shallow copies

Lists and dicts have method for copying.

```
>>> a = [2, 3, [100, 101], 4]
>>> b = list(a)  # make a copy
>>> a is b
>>>
False
```

It's a new list, but the list items are shared.

```
>>> a[2].append((102))
>>> print(b[2], b)
>>> print(a[2] is b[2])
>>>
[100, 101, 102] [2, 3, [100, 101, 102], 4]
True
```

For example, the inner list `[100, 101, 102]` is being shared. This is known as a shallow copy. Here is a picture.

![shallow](https://user-images.githubusercontent.com/70785000/134738939-106211fc-d1ac-40fc-8a91-c25d2a5626a6.png)

### Deep copies

Sometimes you need to make a copy of an object and all the objects contained within it.

You can use the `copy` module for this.

```
a = [2, 3, [100, 101], 4]
import copy

b = copy.deepcopy(a)
a[2].append(102)
print(b[2], b)
>>>
[100, 101] [2, 3, [100, 101], 4]

>>> print(a[2] is b[2])  # False
```

### Names, Values, Types

Variable names do not have a type. It's only a name. However, values do have an underlying type.

```
a = 42
b = 'Hello World'
print(type(a), type(b))
>>>
<class 'int'> <class 'str'>
```

`type()` will tell you what it is. The type name is usually used as a function that creates or converts a value to that type.

### Type Checking

How to tell if an object is a specific type.

```python
if isinstance(a, list):
    print("a is a list")
else:
    print("Nope")
>>>
Nope
```

Checking for one of many  possible type.

```
if isinstance(a, (list, tuple)):
    print("a is a list or tuple")
elif isinstance(a, (str, int)):
    print("a is str or int")
else:
    print("We don't know.")
>>>
a is str or int.
```

*Caution: Don't go overboard with type checking. It can lead to excessive code complexity. Usually you'd only do it if doing so would prevent common mistakes made by others using your code.*

### Everything is a object

Numbers, strings, lists , functions, exceptions, classes, instances, etc are all objects. It means that all objects that can be  named , can be passed around as data, placed in containers, etc., without any restrictions.

There are no *special* kinds of objects. Sometimes it is said that all objects are "first-class".

A simple example:

```python
import math
items = [abs, math, ValueError]
print(items)
>>>
[<built-in function abs>, <module 'math' (built-in)>, <class 'ValueError'>]
>>> print(items[0](-45))
>>> 45
>>> print(items[1].sqrt(2))
>>> 1.4142135623730951
>>> try:
       x = int("not a number")
    except items[2]:
       print("Failed")
>>> 
Failed
```

Here, `items` is a list containing a function, a module and an exception. You can directly use the items in the list in place of the original names.

```python
items[0](-45)   # abs
items[1].sqrt(2)   # math
except items[2]:   # ValueError
```

With greate power comes responsibility.Just because you can do that doesn't mean you should.

### Excercise

In thise set of exercise , you can look at some of the power that comes from first-class objects.

Exercise 2.24: First-class Data

In the file `Data/portfolio.csv` , we read data organized as columns that look like this:

```python
name, share, price
"AA", 100, 32.20
"IBM", 50, 91.10
```

In previous code, we used the `csv` module to read the file, but still had to perform manual type conversions. For example:

```python
for row in rows:
  name = row[0]
  shares = int(row[1])
  price = float(row[2])
```

This kind of conversion can also be performed in a more clever maner using some list baisc operations.

Make a Python list that contains the names of the conversion functions you would use to convert each column into the appropriate type:

```python
>>> types = [str, int, float]
>>>
```

The reason you can even create this list is that everything in Python is *firt-class*. So, if you wanto to have a list of functions, that's fine.

The items in the list you created are functions for converting a values `x` into a given type(e.g., `str(x)`, `int(x)`, `float(x)`).

Now, read a row of data from the above file:

```python
>>> import csv
>>> f = open("Work/Data/portfolio.csv", "rt")
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> print(headers)
>>> row = next(rows)
>>> print(row, type(row))
>>>
['name', 'shares', 'price']
['AA', '100', '32.20'] <class 'list'>
```

As noted, this row isn't enough to do calculations because the types are wrong. For example:

```python
>>> row[1] * row[2]
>>>
row[1] * row[2]
TypeError: can't multiply sequence by non-int of type 'str'
```

However, maybe the data can be paired up with the types you specified in `types`. For example:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Try converting one of the values:

```python
>>> print(types[1](row[1]) * types[2](row[2]))
>>>
3220.0000000000005
```

Try converting a different value:

```python
>>> types[2](row[2])
>>>
32.2
```

Zip the column types with the fields and look at the result:

```python
>>> r = list(zip(types, row))
>>>
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

You will notice that this has paired a type conversion with a value. For example, `int` is paired with the value `'100'`.

The zipped list is usefule if you want to perform conversion on all of the values, one after the other. Try this:

```python
converted = []
for func, val in r:
    converted.append(func(val))

print(converted)
>>>
['AA', 100, 32.2]
```

Make sure you understand what's happening in the above code. In the loop, the `func` variable is one of the type conversions functions(e.g., `str`, `int`, etc). and the `val` variable is one of the values like `'AA'`, `'100'`. The expression `func(val)` is converting a value(kind of like a rype casting).

The above code can be compressed into a single list comprehension.

```python
>>> converted = [func(val) for func, val in r]
>>>
['AA', 100, 32.2]
```

#### Exercise 2.25: Making dictionaries

Remeber how the `dict` function can easily make a dictionary if you have a sequence of key names and values?

Let's make a dictionary form the column headers:

```python
>>> zip_record = zip(headers, converted)
>>> print(dict(zip_record), type(zip_record))
>>>
{'name': 'AA', 'shares': 100, 'price': 32.2} <class 'zip'>
```

Of course, if you're up on your list-comprehension fu, you can do the whole conversion in a single step using a dict-comprehension:

```python
# dictionary comprehension
>>> dic_record = {name:func(val) for name, func, val in zip(headers, types, converted)}
>>> print(dic_record)
>>>
{'name': 'AA', 'shares': 100, 'price': 32.2} <class 'zip'>
```

#### Exercise 2.26: The big picture

Using the techniques in this exercise, you could write statements that easily convert fields from just about any column-oriented datafile into a Python dictionary.

Just to illustrate, suppose you read data from a different datafile like this:

```python
f = open("Work/Data/dowstocks.csv", "rt")
rows = csv.reader(f)
headers = next(rows)
print(headers)
row = next(rows)
print(row)
>>>
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
```

Let's convert the fields using a similiar trick:

```python
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)
>>>
{'name': 'AA', 'price': 39.48, 'date': '6/11/2007', 'time': '9:36am', 'change': -0.18, 'open': 39.67, 'high': 39.69, 'low': 39.45, 'volume': 181800}

>>> record['name']
>>>
'AA'
>>> record['price']
>>>
39.48
```

Bonuse: How would you modify this example to additionally parse the 	`date` entry into a tuple such as `(6, 11, 2007)`?

Spend some time to ponder what you've done in this exercise.We'll revisit these ideas a little later.

[Contents](../Contents.md) \| [Previous (2.6 List Comprehensions)](06_List_comprehension.md) \| [Next (3 Program Organization)](../03_Program_organization/00_Overview.md)

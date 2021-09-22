[Contents](../Contents.md) \| [Previous (2.4 Sequences)](04_Sequences.md) \| [Next (2.6 List Comprehensions)](06_List_comprehension.md)

# 2.5 collections module

The `collections` module provides a number of usefule objects for data handling. 

This part briefly introduces some of these features.

### Example: Counting Things

Let's say you want to tabulate the total shares of each stock.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

There are two `IBM` entries and two `GOOG` entries in this list. The shares need to be combined together somehow.

### Counters

Solution: Use a `Counter`.

```python
# Counters
from collections import Counter

total_shares = Counter()

for name , shares, price in portfolio:
    total_shares[name] += shares

print("Total Shares : {}".format(total_shares))
print(f"{'IBM'} 's shares {total_shares['IBM']}")
```

*result*

```
Total Shares : Counter({'GOOG': 175, 'IBM': 150, 'CAT': 150, 'AA': 50})
IBM 's shares 150
```



### Example: One-Many Mappings

Problem: You want to map a key to multiple values.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

Like in the previous example, the key `IBM` should have two different tuples instead.

Solution: Use a `defaultdict`.

```python
# defaultdict
from collections import defaultdict
holdings = defaultdict(list)

print(holdings, type(holdings))

for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print("holdings' content =>", holdings)
print(holdings['IBM'])
```

```
holdings' content => defaultdict(<class 'list'>, {'GOOG': [(100, 490.1), (75, 572.45)], 'IBM': [(50, 91.1), (100, 45.23)], 'CAT': [(150, 83.44)], 'AA': [(50, 23.15)]})
[(50, 91.1), (100, 45.23)]
```

The `defaultdict` ensures that every time you access a key you get a default value.

### Example: Keeping a History

Problem: We want s history of the last N things.

Solution: Use a `deque`.

```python
from collections import deque
history = deque(maxlen=N)

with open(filename) as f:
  for line in f:
    history.append(line)
    ...
```

## Exercises

The `collections` module might be one of the most usefule library modules for dealing with special purpose kinds of data handling probleams such as tabulating and indexing.

In this exercise, we'll look at a few simple examples. Start by running your `report.py` program so that you have the portfolio of stocks loaded in the interactive mode.

```bash
bash % python3 -i report.py
```

### Exercise 2.18: Tabulating with Counters

Suppose you wanted to tabulate the total number of shares of each stocks. This is easy using `Counter` objects. 

Try it:

```python
# Exercise 2.18 : Tabulating with Counters
from Work import report

portfolio = report.read_portfolio("portfolio.csv")
from collections import Counter

holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']

print(holdings)

>>>
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

Carefully observe how the multiple entries for `MSFT` and `IBM`  in `portfolio` get combined into a single entry here.

You can use a Counter just like a dictionary to retrieve individual values:

```python
print(dir(holdings))
>>>
['__add__', '__and__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__le__', '__len__', '__lt__', '__missing__', '__module__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_keep_positive', 'clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values']

>>> print(holdings["IBM"], holdings["MSFT"])
>>>
150 250
```

If you want to rank the values, do this.

```python
print(holdings.most_common(3))
>>>
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
```

Let's grab another portfolio of stocks and make a new Counter.

```python
portfolio2 = report.read_portfolio("portfolio2.csv")
holdings2 = Counter()

for s in portfolio2:
    holdings2[s['name']] += s['shares']

print(holdings2)
>>>
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
```

Finally, let's combine all of the holdings doing one simple operations:

```python
>>> print(holdings)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})

>>> print(holdings2)
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})

>>> combined = holdings + holdings2
>>> print("combined : ", combined)
combined : Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
```

This is only a small taste of what counters provide. However, if you ever find yourself needing to tabulate values, you should consider using one.

### Commentary: collections module

The `collections` module is one of the most useful library modules in all of Python. In fact, we could do an extended tutorial on just that.

However, doing so now would also be a distraction. For now, put `collections` on your list of bedtime reading for later.

[Contents](../Contents.md) \| [Previous (2.4 Sequences)](04_Sequences.md) \| [Next (2.6 List Comprehensions)](06_List_comprehension.md)
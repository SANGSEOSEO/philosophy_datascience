[Contents](../Contents.md) \| [Previous (2.4 Sequences)](04_Sequences.md) \| [Next (2.6 List Comprehensions)](06_List_comprehension.md)

# 2.5 collections module

The `collections` module provides a number of useful objects for data handling. 

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



```python

```



```python

```



```python

```



```python

```



```python

```



### Commentary: collections module



[Contents](../Contents.md) \| [Previous (2.4 Sequences)](04_Sequences.md) \| [Next (2.6 List Comprehensions)](06_List_comprehension.md)

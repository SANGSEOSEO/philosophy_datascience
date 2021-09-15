[Contents](../Contents.md) \| [Previous (2.1 Datatypes)](01_Datatypes.md) \| [Next (2.3 Formatting)](03_Formatting.md)

# 2.2 Containers

This section discusses lists, dictionaries and sets.

### Overview

Programs often have to work with many objects.

Programs often have to work with many objects.

* A porfolio of stocks
* A table of stock prices

There are three main choices to use.

* Lists. Ordered data.
* Dictionaries. Unordered data.
* Sets. Unorder collection of unique items

### Lists as a Container

Use a list when the order of the data matters. Remeber that lists can  hold any kind of object. For example , a list of tuples.

```python
portfoli = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]
print(portfoli[0])
print(portfoli[1])
```

```
('GOOG', 100, 490.1)
('IBM', 50, 91.3)
```

### List construction

Building a list form scratch.

```
# List construction
records = [] # Initial empty list

# append
records.append(('GOOG', 100, 490.10))
records.append(("IBM", 50, 91.3))

print(records) # [('GOOG', 100, 490.1), ('IBM', 50, 91.3)]
```

An example when reading records from a file.

```
records = [] #Initial empty list
# rt - means read text file.
with open("Data/portfolio.csv", 'rt') as f:
    next(f)  # skip headers
    for line in f:
        row = line.split(",")
        records.append((row[0], int(row[1]), float(row[2])))
```

**reuslt**

```
최종결과 : [('"AA"', 100, 32.2), ('"IBM"', 50, 91.1), ('"CAT"', 150, 83.44), ('"MSFT"', 200, 51.23), ('"GE"', 95, 40.37), ('"MSFT"', 50, 65.1), ('"IBM"', 100, 70.44)]
```

### Dicts as a Container

Dictionaries are usefule if you want fast random lookups (by key name). For example, a dictionary of stock prices.

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Here are some simple lookups:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```

### Dict Construction

Example of building a dict from scratch.

```python
# Dicts as a Container
prices = {}
#insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37

print(prices, type(prices))  # {'GOOG': 513.25, 'CAT': 87.22, 'IBM': 93.37} <class 'dict'>
```

An example populating the dict from the contents of a file.(끄집어내기)

```python
prices = {}
with open("Data/prices.csv", "rt") as f:
    for line in f:
        try:
            row = line.split(",")
            prices[row[0].replace('"', '')] = float(row[1])
        except IndexError:
            pass

print("reuslt : ", prices)
```

**result**

```
reuslt :  {'AA': 9.22, 'AXP': 24.85, 'BA': 44.85, 'BAC': 11.27, 'C': 3.72, 'CAT': 35.46, 'CVX': 66.67, 'DD': 28.47, 'DIS': 24.22, 'GE': 13.48, 'GM': 0.75, 'HD': 23.16, 'HPQ': 34.35, 'IBM': 106.28, 'INTC': 15.72, 'JNJ': 55.16, 'JPM': 36.9, 'KFT': 26.11, 'KO': 49.16, 'MCD': 58.99, 'MMM': 57.1, 'MRK': 27.58, 'MSFT': 20.89, 'PFE': 15.19, 'PG': 51.94, 'T': 24.79, 'UTX': 52.61, 'VZ': 29.26, 'WMT': 49.74, 'XOM': 69.35}
```

Note: If you try this on the `Data/prices.csv` file, you'll find that it almoset works--there'a blank line at the end that causes it to crash. You will need to figure out some way to modify the code to account for that(see Exercise 2.6)

### Dictionary Lookups

You can test the existence of a key.

```python
if 'AA' in prices.keys():
    print("Yeah there.")
else:
    print("Nope")
```

You can look up a values that might not exist and provide a default value in case it doesn't.

```python
name = d.get(key, default)
```

An example:

```python
# Get default value
>>> print(prices.get("KKK", 0.0))  # 0.0
>>> print(prices.get('SCOX', 0.0)) # 0.0
```

### Composite keys

Almost any type of value can be used as a dictionary key in Python. A dictionary key must be of a type that is immutable.

For example check the following out:

```python
# Composite keys.
holidays = {
    (1, 1) : "New Year",
    (3, 14) : "Pi day",
    (9, 13) : "Programmer's day",
}

# access to holidays.
print(holidays[3, 14])
```

*Neither a list, a set, nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable.(변경가능한 것은 키를 구성할 수 없음)

### Sets

Sets are collection of unorderd unique items.

```python
# sets
tech_stocks = {"IBM", "AAPL", "MSFT"}
tech_stocks = set(["IBM", "AAPL", "MSFT"])

print(tech_stocks, type(tech_stocks))

# Sets are usefule for membership tests.
if 'IBM' in tech_stocks:
    print("Yeah!!!!")
else:
    print("Nope")
```

Sets are also usefule for duplicate elimination.

```python
# Sets are usefule for duplicate elimination.
names = ["IBM", "AAPL", "GOOG", "IBM", "GOOG", "YHOO"]
unique = set(names)

print("Unique ->", unique)  # Unique -> {'YHOO', 'IBM', 'GOOG', 'AAPL'}
```

Additional set operations:

```python
# Additional set operations
unique.add('CAT')
unique.add("SAM")
print(unique.pop())  # remove and return arbitrary item
print(unique)

unique.remove("AAPL")
print("After removal : ", unique)

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

print(s1 | s2)
print(s1.union(s2))
print(s1.intersection((s2)))
print(s1 & s2)
print(s1.difference(s2))
print(s1 - s2)
```

```
{'d', 'b', 'c', 'a'}
{'d', 'b', 'c', 'a'}
{'c'}
{'c'}
{'a', 'b'}
{'a', 'b'}
```

## Exercises

In these exercises, you start building one of the major programs used for the rest of this course. Do you work in the file `Work/report.py`

### Exercise 2.4: A list of tuples

The file `Data/portfolio.csv` contains a list of stocks in a portfolio. In [Exercise 1.30](../01_Introduction/07_Functions.md), you wrote a function `portfolio_cost(filename)` that read this file and performed a simple calculation.

Your code should have looked something like this:

```python
# pcost.py

import csv
def portfolio_cost(filename):
    """
    compute the total cost(shares * price)
    :param filename:
    :return: total_cost
    """
    total_cost = 0.0

    with open("../Data/"+ filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost = nshares * price
    return total_cost

# process
total_cost = portfolio_cost("portfolio.csv")
print(f"Total Cost : {total_cost: .2f}")
```

```
Total Cost :  7044.00
```

Using this code as a rough guide, create a new file `report.py`. In that file, define a function `read_portfolio(filename)` that opens a given portfolio file and reads int into a list of tuples. To do this, You're going to make a new minor modifications to the above code. 

First, instead of defining `total_cost = 0`, you' ll make a variable that's initially set to an empty list. 

For example:

```python
portfolio = []
```

Next, instead of totaling up the cost, you’ll turn each row into a
tuple exactly as you just did in the last exercise and append it to
this list. For example:

Next, instead of totaling up the cost, you'll turn each row into a tuple exactly as you just did in the last exercise and append it to this list. For example:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finally, you’ll return the resulting `portfolio` list.

```
# report.py
import csv
def read_porfolio(filename):
    '''

    :param filename:
    :return: composite list with nested tuple
    '''
    portfolio = []
    TARGET_FILE = "../Data/"+ filename
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holdings = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holdings)
    return portfolio

# process
portfolio = read_porfolio("portfolio.csv")
print(portfolio)
```

**result:**

```python
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23), ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
```

**Total Cost:**

```
# Total Cost
total_cost = 0.0
for row in portfolio:
    total_cost += int(row[1]) * float(row[2])
print(f"{total_cost:.2f}")
>>>
44671.15
```

This list of tuples that you have created is very similar to a 2-D array. For example, you can access a specific column and row using a lookup such as `portfolio[row][column]` where `row` and `column` are integers.

That said, you can also rewrite the last for-loop using a statement like this:

```python
# tuple unpacking
total_cost = 0.0
for _, share, price in portfolio:
    total_cost += int(share) * float(price)

>>> print("After tuple unpacking Total Cost : {:.2f}".format(total_cost))
44671.15
>>>
```

### Exercise 2.5: List of Dictionaries

Take the function you wrote in Excercise 2.4 and modify to represent each stock in the portfolio with a dictionary instead of a tuple. In this dictionary use the field names of "names", "shares", and "price" to represent the different columns in the input file.

Experiment with this new function in the same manner as you did in Exercise 2.4.

```python
def read_portfolio(filename:str):
    '''
    Excercise 2-5
    :param fiename:
    :return List with dictionary collections.
    '''
    portfolio = []
    TARGET_FILE = "../Data/"+filename

    key_cols = []
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        key_cols = header  # initialize 

        result_list = []
        for row in rows:
            result = dict()
            #print(row, type(row))  # list datatype

            result[key_cols[0]] = row[0].replace('"', '')
            result[key_cols[1]] = int(row[1])
            result[key_cols[2]] = float(row[2])
            result_list.append(result)
    return result_list

# 수행
portfolio = read_portfolio("portfolio.csv")
print(portfolio[0])
print(portfolio[1])
print("Shares : ", portfolio[1]['shares'])

total = 0.0
for s in portfolio:
    total += int(s["shares"]) * float(s["price"])
print(f"{total:.2f}")
```

**result is the following**

```python
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
Shares :  50
44671.15
```

Here, you will notice that the different fields for each entry are accessed by key names instead of numeric column numbers. This is often preferred because the resulting code is easier to read later.

Viewing large dictionaries and lists can be messy. To clean up the output for debugging, cosider using `pprint` function.

```
from pprint import pprint
pprint(portfolio)
```

```
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

### Exercise 2.6: Dictionaries as a container

A dictionary is a useful way to keep track of items where you wanto to look up items using an index other than an integer. 

In the Python shell, try playing with a dictionary:

```python
>>> prices = {}
>>> prices["IBM"] = 92.45
>>> prices["MSFT"] = 45.12
>>> prices
{'IBM': 92.45, 'MSFT': 45.12}
>>> prices["AAPL"]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'AAPL'
>>> 'AAPL' in prices
False
```

The file `Data/prices.csv` contains a series of lines with stock prices. The file looks something like this.

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Write a function `read_prices(filename)` that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.

To do this, start with an empty dictionary and start inserting values into it just as you did above. However, you are reading the values from a file now.

We'll use this data structure to quickly lookup the price of a given stock name.

A few little tips that you'll need for this part. First, make sure you use the `csv` module just as you did before -- there's no need to reinvent the wheel here.

```python
>>> f = open("../Data/prices.csv", "rt")
>>> rows = csv.reader(f)
>>> for row in rows:
       print(row)
        
>>> ['AA', '9.22']
['AXP', '24.85']
['BA', '44.85']
..............
```

The other little complication is that the `Data/prices.csv` file may have some blank lines in  it. Notice how the last row of data above is an empty list - meaning no data was present on that line.

There's a possibilities that this could cause your program to die with an exception. Use the `try` and `except` statement to catch this as appropriate. Thought: would it be better to guard against bad data with an `if` - statement instead?

Once you have written your `read_prices()` function, test it interactively to make sure it works.

```python
def read_prices(filename: str):
    '''
    Excercies 2-6
    :param filename:
    :return:
    '''
    TARGET_DIR = "../Data/"+filename
    with open(TARGET_DIR, "rt") as f:
        pricesList = csv.reader(f)

        prices = {}
        for lst in pricesList:
            try:
                prices[lst[0]] = lst[1]
            except IndexError:
                pass
    return prices

# 수행
prices = read_prices("prices.csv")
print(prices["IBM"])
print(prices["MSFT"])
```

```
106.28
20.89
```

### Exercise 2.7: Finding out if you can retire

Tie all of this work together by adding a few additional statements to your `report.py` program that computes gain/logss.

These statements should take the list of stocks in Excercise 2.5 and the dictionary of prices in Excercise 2.6 and compute the current value of the portfolio along with the gain/loss.

```
# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += int(s["shares"]) * float(prices[s["name"]])

print(f" total value : {total_value: .2f}")  # total value :  28686.10
```

[Contents](../Contents.md) \| [Previous (2.1 Datatypes)](01_Datatypes.md) \| [Next (2.3 Formatting)](03_Formatting.md)

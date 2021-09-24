[Contents](../Contents.md) \| [Previous (2.5 Collections)](05_Collections.md) \| [Next (2.7 Object Model)](07_Objects.md)

# 2.6 List Comprehensions

A common task is processing items in a list. This section introduces list compreshensings, a powerfule tool for doing just that.

### Creating new lists

A list comprehensing creates a new list by applying an operation to each element of a sequence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2 * x for x in a]
>>> print("List comprehensing ", b)
>>>
List comprehensing  [2, 4, 6, 8, 10]
```

Another example:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> print(a)
['elwood', 'jake']
```

The general syntax is: `[ <expression> for <variable_name> in <sequence> ]`.

### Filtering

You can also filter during the list comprehension.

```python
# Filtering
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2 * x for x in a if x > 0]
>>> print(b)

[2, 8, 4, 20]
```

### Use cases

List comprehensions are hugely useful. For example, you can collect values of a  specific dictionary fields:

```python
>>> from Work import report
>>> portfolio2 = report.read_portfolio("portfolio2.csv")
>>> [s['name'] for s in portfolio2]
>>>
Stocks  ['AA', 'HPQ', 'MSFT', 'GE']
```

You can perform database-like queries on sequences.

```python
>>> a = [s for s in portfolio if s['price'] > 70 and s['shares'] > 50]
>>> print("a : ", a)
>>>
a :  [{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
```

You can also combine a list comprehension with a sequnce reduction.

```python
>>> cost  = sum([s['shares'] * s['price'] for s in portfolio2])
>>> print(f'cost : {cost: .2f}')
>>>
cost :  19908.75
```

### General Syntax

```code
[ <expression> for <variable_name> in <sequence> if <condition>]
```

What it means:

```python
result = []
for variable_name in sequence:
    if condition:
        result.append(expression)
```

### Historical Digression

List comprehensions come from math(set-builder notation).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

It is also implemented in several other languages. Most coder probably aren't thinking about their math class though. So, It's fine to view it as a cool shortcut.

## Exercises

Start by running your 	`report.py` program so that you have the portfolio of stocks loaded in the interactive mode.

```bash
bash % python3 -i report.py
```

Now, at the Python interactive prompt, type statements to perform the operations described below. These operations perform various kinds of data reductions, transform, and queries on the portfolio data.

### Exercise 2.19: List comprehensions

Try a few simple list comprehensions just to become familiar with the syntax.

```python
>>> nums = [1, 2, 3, 4]
>>> squares = [num * num for num in nums]
>>> print(squares)
>>>
[1, 4, 9, 16]
>>> twice = [2 * x for x in nums]
>>> print(twice)
>>>
[2, 4, 6, 8]
```

Notice how the list comprehensions are creating a new list with the data suitably transformed or filtered.

### Exercise 2.20: Sequence Reductions

Compute the total cost of the portfolio using a single Python statement.

```python
>>> portfolio = report.read_portfolio("portfolio.csv")
>>> print(portfolio)
>>> cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(f"Total Cost for Purchasing stocks : {cost:.2f}")
>>>
Total Cost for Purchasing stocks : 44671.15
```

After you have done that, show how you can compute the current value of the portfolio using a single statement.

```python
>>> prices =  report.read_prices("prices.csv")
>>> print(prices)
>>>
{'AA': '9.22', 'AXP': '24.85', 'BA': '44.85', 'BAC': '11.27', 'C': '3.72', 'CAT': '35.46', 'CVX': '66.67', 'DD': '28.47', 'DIS': '24.22', 'GE': '13.48', 'GM': '0.75', 'HD': '23.16', 'HPQ': '34.35', 'IBM': '106.28', 'INTC': '15.72', 'JNJ': '55.16', 'JPM': '36.90', 'KFT': '26.11', 'KO': '49.16', 'MCD': '58.99', 'MMM': '57.10', 'MRK': '27.58', 'MSFT': '20.89', 'PFE': '15.19', 'PG': '51.94', 'T': '24.79', 'UTX': '52.61', 'VZ': '29.26', 'WMT': '49.74', 'XOM': '69.35'}

>>> value = sum([s['shares'] * float(prices[s['name']]) for s in portfolio])
>>> print(f"Current stocks's Total Cost : {value:.2f}")
>>>
Current stocks's Total Cost : 28686.10
```

Both of the above operations are an example of a map-reduction. The list comprehension is mapping an operation across the list.

```python
>>> print([s['shares'] * s['price'] for s in portfolio])
>>>
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
```

The `sum()` function is then performing a reduction across the result.

With this knowledge, you are now ready to go launch a big-data startup company.

### Exercise 2.21: Data Queries

Try the following examples of various data queries.

First, a list of all portfolio holdings with more than 100 shares.

```python
>>> more_100 = [s for s in portfolio if s['shares'] > 100]
>>> print(more_100)
>>>
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

All portfolio holdings for MSFT and IBM stocks

```python
>>> msftibm = [ s for s in portfolio if s['name'] in ['MSFT', 'IBM']]
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT', 'IBM'}] 
>>> print(msftibm)
>>>
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
```

A list fo all portfolio holdings that cost more than $10000.

```python
>>> cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000]
>>> print(f"Cost more than 10K : {cost10k}")
>>>
Cost more than 10K : [{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

### Exercise 2.22: Data Extraction

Show how you could build a list of tuples `(name, shares)` where `name` and `shares` are taken from `portfolio`.

```python
>>> name_shares = [(s['name'], s['shares']) for s in portfolio]
>>> name_shares
>>>
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
```

If you change the square brackets `([,])` to curly braces `({,})`, you get something known as a set comprehension. This gives you unique of distinct values.

For example, this determines the set of unique stock names that appear in `portfolio`:

```python
>>> names = {s.name for s in portfolio}
>>> print(names)
>>>
{'AA', 'IBM', 'GE', 'MSFT', 'CAT'}
```

If you specify `key:value` pairs, you can build a dictionary. For example, make a dictionary that maps the name of a stock to the total number of shares held.

```python
>>> holdings = {name: 0 for name in prices}
>>> print(holdings)
>>>
{'AA': 0, 'AXP': 0, 'BA': 0, 'BAC': 0, 'C': 0, 'CAT': 0, 'CVX': 0, 'DD': 0, 'DIS': 0, 'GE': 0, 'GM': 0, 'HD': 0, 'HPQ': 0, 'IBM': 0, 'INTC': 0, 'JNJ': 0, 'JPM': 0, 'KFT': 0, 'KO': 0, 'MCD': 0, 'MMM': 0, 'MRK': 0, 'MSFT': 0, 'PFE': 0, 'PG': 0, 'T': 0, 'UTX': 0, 'VZ': 0, 'WMT': 0, 'XOM': 0}
```

This latter feature is known as a **dictionary comprehension**. Let's tabulate.

```python
>>> for s in portfolio:
       holdings[s['name']] += s['shares']

>>> print("for..loop result : ", holdings)
>>>
{'AA': 100, 'AXP': 0, 'BA': 0, 'BAC': 0, 'C': 0, 'CAT': 150, 'CVX': 0, 'DD': 0, 'DIS': 0, 'GE': 95, 'GM': 0, 'HD': 0, 'HPQ': 0, 'IBM': 150, 'INTC': 0, 'JNJ': 0, 'JPM': 0, 'KFT': 0, 'KO': 0, 'MCD': 0, 'MMM': 0, 'MRK': 0, 'MSFT': 250, 'PFE': 0, 'PG': 0, 'T': 0, 'UTX': 0, 'VZ': 0, 'WMT': 0, 'XOM': 0}
```

Try this example that filters the `prices` dictionary down to only those names that appears in the portfolio.

```python
>>> portfolio_prices = {name: prices[name] for name in names}
>>> print(portfolio_prices)
>>>
{'GE': '13.48', 'CAT': '35.46', 'IBM': '106.28', 'MSFT': '20.89', 'AA': '9.22'}
```

### Exercise 2.23: Extracting Data From CSV Files

Knowing how to use various combinations of list, set , and dictionary comprehensions can be useful in various froms of data processing. Here's an example that shows how to extract selected columns from a CSV file.

First, read a row of header information from a CSV file:

```python
>>> import csv
>>> f = open("Work/Data/portfoliodate.csv")
>>> rows = csv.reader(f)
>>> header = next(rows)
>>> print(header)
>>>
['name', 'date', 'time', 'shares', 'price']
```

Next, define a variable that lists the columns that you actually care about:

```python
select = [
   'name', 'shares', 'price'
]
```

Now, locate the indices of the above columns in the source CSV file:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> print(indices)
>>>
[0, 3, 4]
```

Finally, read a row of data and turn it into a dictionary using a dictionary comprehensions:

```python
>>> row = next(rows)
>>> record = {colname: row[index] for colname, index in zip(select, indices)}
>>> print(record)
>>>
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

If you're feeling comfortable with what just happend, read the rest of file:

```python
>>> portfolio = [{colname: row[index] for colname, index in zip(select, indices)} for row in rows]
>>> print(portfolio)
>>>
[{'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

oh my, you just reduced much of the `read_portfolio()` function to a single statement.

### Commentary

List comprehensions are commonly used in Python as an efficient means for transforming, filtering, or collecting data.

Due to the syntax, you don't want to go overboard-try to keep each list comprehensions as simple as possible.

It's okay to break things into multiple steps.For example, it's not clear that you would want to spring that last example on your unsuspecting co-workers.

That said, knowing how to quickly manipulate data is a skill that's incredibly useful. There are numerous situations where you might have to solve some kind of one-off problem involving data imports, exports, extraction, and so forth.

Becoming a guru master of list comprehensions can substantially reduce the time spend devising a solution. Also, don't forget about the `collections` module.

[Contents](../Contents.md) \| [Previous (2.5 Collections)](05_Collections.md) \| [Next (2.7 Object Model)](07_Objects.md)
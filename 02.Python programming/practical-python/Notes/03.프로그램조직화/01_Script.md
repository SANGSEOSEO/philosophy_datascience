[Contents](../Contents.md) \| [Previous (2.7 Object Model)](../02_Working_with_data/07_Objects.md) \| [Next (3.2 More on Functions)](02_More_functions.md)

# 3.1 Scripting

In this part we look more closely at the practive of writing Pyton scripts.

### What is a Script?

A script is a program that runs a series of statements and stops.

```python
# program.py

statement1
statement2
statement3
...
```

We have mostly been writing scripts to this point.

### A Problem

If you write a useful script, it will grow in feature and functionality. You may want to apply it to other related problems. 

Over time, It might become a critical application. And if you don't take care, It might turn into a huge tangled mess. 

So, let's get organized.

### Defining Things

Names must always be defined before they get used later.

```python
def square(x):
    return x * x

a = 42
b = a + 2

z = square(b)
print(f"z is {z: .2f}")

>>>
z is  1936.00
```

**The order is important.**
You almost always put the definitions of variables and functions near the top.

### Defining Functions

It is a good idea to put all of the code related to a single *task* all in one place.

Use a function

```python
def read_prices(filename):
    """
    read a csv file and reutrn dictionary
    :param filename: 
    :return: 
    """
    import csv
    prices = dict()
    TARGET_DIR = "Work/Data/"
    with open(TARGET_DIR+filename, 'rt') as f:
        f_csv = csv.reader(f)
        
        for row in f_csv:
            prices[row[0]] = row[1]
    return prices
```

A function also simplifies repeated operations.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```

### What is a Function?

A function is a named sequence of statements.

```python
def funcname(args):
  statement
  statement
  ...
  return result
```

*Any* Python statement can be used inside.

```python
def foo():
    import math
    print(math.sqrt(2))
    help(math)
```

There are no *special* statements in Python(which makes it easy to remember).

### Function Definition

Functions can be *defined* in any order.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# OR
def bar(x):
    statements

def foo(x):
    bar(x)
```

Functions must only be defined prior to actually being used(or called) during program execution.

```python
foo(3)        # foo must be defined already
```

Stylistically, it is probably more common to see functions defined in a bottom-up fashion.

### Bottom-up Style

Functions are treated as building blocks. The smaller / simpler blocks go first.

```python
# myprogram.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Defined above
    ...

def spam(x):
    ...
    bar(x)          # Defined above
    ...

spam(42)            # Code that uses the functions appears at the end
```

Later functions build upon earlier functions. Again, this is only a point of style. The only thing that matters in the above program is that the call to `spam(42)` go last.

### Function Design

They should only operate on passed inputs and avoid global variables and mysterious side-effects. 

Main goals: *Modularity and Predictability*.

### Doc Strings

It's good practive to include documentation in the form of a doc-string. Doc-strings are strings written immediately after the name of the function. They deed `help()`, IDEs and other tools.

```python
def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

A good practice for doc strings is to write a short one sentence
summary of what the function does.  If more information is needed,
include a short example of usage along with a more detailed
description of the arguments.

### Type Annotations

You can also add optional type hints to function definitions.

```python
def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

The hints do noting operationally. They are purely informational. However, they may be used by IDEs, code checkers, and other tools to do more.

## Exercises

In section 2, you wrote a program called `report.py` that pointed out a report showing the performance of a stock portfolio. This program consisted of some functions. For example:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

However, there were also portions of the program that just performed a series of scripted calculations. This code appeared near the end of the program. For example:

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

In this exercise, we're going to take this program and organize it a little more strongly around the use of functions.



### Exercise 3.1: Structuring a program as a collection of functions

Modify your `report.py` program so that all major operations, including calculations and output, are carried out by a collection of functions, Specifically:

* Create a function `print_report(report)` that prints out the report.
* Change the last part of the program so that it is nothing more than a series of function calls and no other computation.

I've added this function in the end part.

```python
def print_report(report):
    """
    Print a nicely formatted table
    :param  - report - list type
    :return: None
    """
    headers = ('name', 'shares', 'price', 'change')
    print("%10s %10s %10s %10s" %headers)
    print(("-" * 10 + ' ') * len(headers))

    for name, share, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
```



### Exercise 3.2: Creating a top-level function for program execution

Take the last part of your program and package it into a single function `portfolio_report(portfolio_filename, price_filename)`. Have the function work so that the following function call creates the report as before.

```python
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
```

In thise final version, your porgram will be noting more than a series of function definitions followd by a single function call to `portfolio_report()` at the very end(whick exeucte all of the steps involved in the program).

By turning your program into a single function, It becomes easy to run it on diffrent inputs. For example, try these statements interactively after running your program:

The following is the main program calling to the sub program.

```python
def portfolio_report(portfoiloFileName: str, pricesFileName: str):
    """
    주식의 Portfolio파일명 주식 가격 파일명을 인자로 받아
    주식 레포트 리턴
    :return: 
    """
    portfolio = read_portfolio(portfoiloFileName)
    prices = read_prices(pricesFileName)
    report = make_report(portfolio, prices)
    print_report(report)
>>> # Excercise 3-2
>>> from Work import report
>>> #호출
>>> report.print_report("portfolio.csv", "prices.csv")
>>>
      name     shares      price     change
---------- ---------- ---------- ---------- 
        AA        100      $9.22      22.98
       IBM         50    $106.28     -15.18
       CAT        150     $35.46      47.98
      MSFT        200     $20.89      30.34
        GE         95     $13.48      26.89
      MSFT         50     $20.89      44.21
       IBM        100    $106.28     -35.84

```

### Commentary

Python makes it very easy to write relatively unstructue scripting code where you just have a file with a sequence of statements in it. In the big picture, It's almose always better to utilize functions whenever you can. At some point, that script is going to grow and you'll wish you had a bit more organization. Also, A little known fact is that Python runs a bit faster if you use functions.

[Contents](../Contents.md) \| [Previous (2.7 Object Model)](../02_Working_with_data/07_Objects.md) \| [Next (3.2 More on Functions)](02_More_functions.md)
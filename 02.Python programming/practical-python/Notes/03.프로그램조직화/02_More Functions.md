[Contents](../Contents.md) \| [Previous (3.1 Scripting)](01_Script.md) \| [Next (3.3 Error Checking)](03_Error_checking.md)

# 3.2 More on Functions

Although functions were introduced earlier, very few details were provided on how they actually wordks at a deeper level. This secitons aims to fill in some gaps add discuss matters such as calling conventions, scoping rules, and more.

### Calling a Function

Consider this function:

```python
def read_prices(filename, debug):
    ...
```

You can call the function with positional arguments:

```
prices = read_prices('prices.csv', True)
```

Or you can call the function with keyword arguments:

```python
prices = read_prices(filename='prices.csv', debug=True)
```

### Default Arguments

Sometimes you want an argument to be optional. If so, assign a default value in the function definition.

```python
def read_prices(filename, debug=False):
    ...
```

If a default value is assigned, the argument is optional in function calls.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

*Note: Arguments with defaults must appear at the end of the argments list(all non-optional arguments go first).*

### Prefer keyword arguments for optional arguments

Compare and contrast these two different calling styles:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

In most cases, keyword arguments improve code clarity-especially for arguments that serve as flags or which are related to optional features.

### Design Best Practices

Always give short, but meaningfule names to functions arguments. Someone using a function may want to use the keyword calling style.

```python
d = read_prices('prices.csv', debug=True)
```

Python development tools will show the names in help features and documentation.

### Returning Values

The `return` statement returns a value

```python
def square(x):
    return x * x
```

It no return value is given or `return` is missing, `None` is returned.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```

### Multiple Return Values

Functions can only return one value. However, a function may return multiple values by returning them in a tuple.

```python
def divide(a, b):
    q = a // b    # 몫을 리턴 - Quotient
    r = a % b # 나머지를 리턴 - remainder
    return q, r
```

Usage example:

```python
>>> x, y = divide(3, 7)
>>> print(f"몫 : {x} , 나머지 : {y}")
>>>
몫 : 0 , 나머지 : 3
>>> x = divide(37, 5)
>>> print(f"X is {x}, Quotient : {x[0]}, Remainder : {x[1]}")
>>> 
X is (7, 2), Quotient : 7, Remainder : 2
```

### Variable Scope

Programs assign values to variables.

```python
x = value # Global variable
def foo():
  y = value # Local variable
```

Variables assignments occur outside and indide function definitions. Variables defined outside are "global". Variables inside a function are "local".

### Local Variables

Variables assigned inside functions are private.(함수내에서 선언된 변수는 함수내에서만 유효함)

```python
def read_portfolio(filename):
  portfolio = []
  for line in open(filename):
    fields = line.split(",")
    s = (fields[0], int(fields[1], float(fields[2])))
    portfolio.append(s)
  return portfolio
```

In this example, `filename`, `portfolio`, `line`, `fields` and `s` are local variables. Those variables are not retained or accessible after the function call.

```
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

Local also can't conflict with variables found elsewhere.

### Global variables

Function can freely access the values of globals defined in the same file.

```python
name = "Dave"

def greeting():
  print("Hello", name)
```

However, functions can't modify globals.

```python
name = 'Dave'

def span():
  name = "Guido"
  
spam()
print(name)  # will print "Dave"
```

**Remeber: All assignments in functions are local**

### Modifying Globals

If you must modify a global variable you must declare it as such.

```python
name = "Dave"

def spam():
  global name
  name = "Guido"  # Changes the gloval name above
```

The global declaration must appear before its use and the corresponding variable must exist in the same file as the function. Having seen this, know that it is considered poor form. In fact, try to avoid `global` entrirely if you can.

If you need a function to modify some kind of state outside of the function, it's better to use a class instead(more on this later)

### Argument Passing

When you call a function, the argument variables are names that refer to the passed values. These values are NOT copies(see section 2.7).

If mutable data types are passed(e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
  items.append(42)
  
a = [1, 2, 3]
foo(a)
print(a)  # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a value and reassigning a variable name.

```
def foo(items):
  items.append(42)
  
a = [1, 2, 3]
foo(a)
print(a)  # [1, 2, 3, 42]
# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*

### Exercises

This set of exercises have you implement what is, perhaps, the most powerfule and difficult part of the course. There are a lot of steps and many concepts from past execised are put together all at once. The final solutions is onyl about 25 lines of code, but take your time and make sure you understand each part.

A central part  of your `report.py` program focuses on the reading of CSV files. 

For example, the function 	`read_portfolio()` reads a file containing rows of portfolio data and the function `read_prices()` reads a file containing rows of price data.

In both of those functions, there are a lot fo low-level "fiddly" bits and similar features. For example, they both open a file and wrap it with `csv` module and they both convert various fields into new types.

If you were doing a lot of file parsing for real, you'd probably want to clean some of this up and make it more general purpose. That's our goal. 

Start this exercise by opening the file called `work/fileparse.py	`.This is where we will be doing our work.

#### Exercise 3-3: Reading CSV Files

To start, let's just focus on the probelam of reading a CSV files into a list of dictionaries. In the `fileparse.py`, define a function that looks like this:

*Read Evaluate Print Loop*

```
>>>import csv
>>> with open("Work/Data/portfolio.csv") as f:
       rows = csv.reader(f)

       # read the file header
       header = next(rows)
       records = []

       for row in rows:
          if not row:  #데이터가 없으면 다음 루프 수행
              continue
          record = dict(zip(header, row))
          records.append((record))

>>> print(records)
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

This function reads a CSV file into a dictionaries while hiding the details of opening the file, wrapping it with the `csv` module, ignoring blank lines, and so forth.

```python
# fileparse.py
def parse_csv(filename):
	"""
	return Stock information with dictionary data collection
	"""
    import csv

    with open("Data/"+filename, 'rt') as f:
        rows = csv.reader(f)
        # read the file header
        header = next(rows)
        records = []

        for row in rows:
            if not row:
                continue
            record = dict(zip(header, row))
            records.append((record))
    return records
  
>>> # 수행
>>> records = parse_csv("portfolio.csv")
>>> print(records) 

[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

This is good except that you can't do any kind of useful calculation with the data because eveythig is represented as a string. We'll fixt this shortly, but let's keep building on it.

#### Exercise 3-4: Building a Column Selector

In many caes, you're only interested in selected columns from a CSV file, not all of the data, Modify the `parse_csv()` function so that is optionally allows user-specified columns to be picked out as follows.

```python

```

[Contents](../Contents.md) \| [Previous (3.1 Scripting)](01_Script.md) \| [Next (3.3 Error Checking)](03_Error_checking.md)
[Contents](../Contents.md) \| [Previous (2.2 Containers)](02_Containers.md) \| [Next (2.4 Sequences)](04_Sequences.md)

# 2.3 Formatting

This section is a slight digression, but when you work with data, you often want to product structured output(tables, etc.)

For example:

```code
      Name      Shares        Price
----------  ----------  -----------
        AA         100        32.20
       IBM          50        91.10
       CAT         150        83.44
      MSFT         200        51.23
        GE          95        40.37
      MSFT          50        65.10
       IBM         100        70.44
```

### String Formatting

One way to format string in Python 3.6+ is with `f-strings`.

One way to format string in Python 3.6+ is with `f-strings.`

```python
>>> name = "IBM"
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:10d} {price:>10.2f}'  # >오른쪽 정렬해서 10자리기준
'       IBM        100      91.10'
```

The part `{expression:format}` is replaced. It is commonly used with `print`. Common code include.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```

### Format codes

Format codes (after the `:` inside the `{}`) aresimilar to C `printf`. 

```code
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

Common modifiers adjust the field width and decimal precision. This is a particular list:

```code
:>10d  Integer right aligned in 10-character field
:<10d  Integer left aligned in 10-character field
:^10d  Interger centered in 10-character field
:0.2f  Float with 2 digit precision
```

### Dictionary Formatting

You can use the `format_map()` method to apply strng formatting to a dictionary of values:

```python
>>> s = {
    "name":"IBM",
    "shares": 100,
    "price": 91.1
   }

>>> msg = "{name: >10s} {shares: 10d} {price:10.2f}".format_map(s)
>>> print(msg)

IBM        100      91.10
```

It uses the same codes as `f-strings` but takes the values from the supplied dictionary.

### format() method

There is a method `format()` that can apply formatting to a arguments or keyword arguments.

```python
>>> s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
>>> "{name:10s} {shares:10d} {price:10.2f}".format_map(s)
'IBM               100      91.10'

>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
```

Frankly, `format` is a bit verbose. I prefer `f string`.

### C-Style Formatting

You can aoso use the formatting operator `%`

```python
>>> "The value is %d" % 3
'The value is 3'
>>> "%5d %-5d %10d" %(3, 4, 5)
'    3 4              5'
>>> "%0.2f"  % (3.1415296)
'3.14'
```

This requires a single items or a tuple on the right. Format codes are modeled after the C `printf()` as well.

Note: This is the only formatting available on byte strings.

```python
# byte strings
>>> msg = b"%s has %d medals on the wall." %(b"Susan", 10)
>>> print(msg)

b'Susan has 10 medals on the wall.'
```

## Exercises

### Exercise 2.8: How to format numbers

A common probleam with printing numbers is specifying the number of decimal places. One way to fix this is to use f-strins.

Try these examples:

```python
>>> values = 42863.1
>>> print(values)
42863.1

>>> print(f"{values:>16.2f}")
        42863.10
>>> print(f"{values:<16.2f}")
42863.10        
>>> print(f"{values:*>16,.2f}") # 16자리로 하되  값을 제외한 나머지 자리는 별표로 보이게 표시
*******42,863.10
```

Full documentation on the formatting codes used f-strings can be found [here](https://docs.python.org/3/library/string.html#format-specification-mini-language). Formatting is also sometimes performed using the `%` operator of strings.

```python
>>> print("%.4f" % values)
42863.1000
>>> print("%16.2f "% values)
        42863.10 

```

Documentation on various codes used with `%` can be found [here](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Although it’s commonly used with `print`, string formatting is not tied to printing. If you want to save a formatted string. Just assign it to a variable.

```
>>> f = "%.4f" % values
>>> f
'42863.1000'
```

### Exercise 2.9: Collecting Data

In Excercise 2.7, you wrote a program called `report.py` that computed the gain/loss of a stock portfolio. 

In this excercise, you're going to start modifying it to produce a table like this.

```
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```

In this report, "Price" is the current share price of the stock and "Change" is the share price form the initial purchase price.

In order to generate the above report, you'll first want to collect all of the data shown in the table. 

Write a function `make_report()` that takes a list of stocks and dictionary of prices as input and reutrns a list fo tuples containing the rows of the above table.

Add this function to your `report.py` file. Here's how it should work if you try it interactively.

```s report, 
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> prices = read_prices('Data/prices.csv')
>>> report = make_report(portfolio, prices)
>>> for r in report:
        print(r)

('AA', 100, 9.22, -22.980000000000004)
('IBM', 50, 106.28, 15.180000000000007)
('CAT', 150, 35.46, -47.98)
('MSFT', 200, 20.89, -30.339999999999996)
('GE', 95, 13.48, -26.889999999999997)
...
>>>
```

This is the script from `report.py`.

```
def make_report(portfolio, prices):
    '''
    주식 레포트 만들기 - Excercise 2-9
    :param portfolio:
    :param prices:
    :return:
    '''
    stockList = []
    for holder in portfolio:
        result = tuple()
        Change = float(holder['price']) - float(prices[holder['name']])
        result = (holder['name'], holder['shares'], float(prices[holder['name']]), Change)
        stockList.append(result)
    print("StockList : ", stockList)
    return stockList

# 수행해보자
>>> portfolio = read_portfolio("portfolio.csv")
>>> prices = read_prices("prices.csv")
>>> report = make_report(portfolio, prices)

>>> for r in report:
       print(r)
```

*result is the following*

```
('AA', 100, '9.22', 22.980000000000004)
('IBM', 50, '106.28', -15.180000000000007)
('CAT', 150, '35.46', 47.98)
('MSFT', 200, '20.89', 30.339999999999996)
('GE', 95, '13.48', 26.889999999999997)
('MSFT', 50, '20.89', 44.209999999999994)
('IBM', 100, '106.28', -35.84)
```

### Exercise 2.10: Printing a formatted table

Redo the `for-loop in Excercise 2.9, but change the print statement to format the tuples.

```python
>>> for r in report:
       print(f"%10s %10d %10.2f %10.2f" %r)

        AA        100       9.22      22.98
       IBM         50     106.28     -15.18
       CAT        150      35.46      47.98
      MSFT        200      20.89      30.34
        GE         95      13.48      26.89
      MSFT         50      20.89      44.21
       IBM        100     106.28     -35.84        
```

You can also expand the values and use f-strings. For example:

```python
>>> for name, shares, price, change in report:
       print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

        AA        100       9.22      22.98
        IBM         50     106.28     -15.18
        CAT        150      35.46      47.98
        MSFT        200      20.89      30.34
        GE         95      13.48      26.89
        MSFT         50      20.89      44.21
        IBM        100     106.28     -35.84
        AA        100       9.22      22.98
        IBM         50     106.28     -15.18
        CAT        150      35.46      47.98
        MSFT        200      20.89      30.34
        GE         95      13.48      26.89
        MSFT         50      20.89      44.21
        IBM        100     106.28     -35.84
```

Take the above statements and add them to your `report.py` program. Have your program take the output of the `make_report()` function and print a nicely formatted table as shown.

```
def make_report(portfolio, prices):
    '''
    주식 레포트 만들기 - Excercise 2-9, Excercise 2-10
    :param portfolio:
    :param prices:
    :return:
    '''
    stockList = []
    for holder in portfolio:
        result = tuple()
        Change = float(holder['price']) - float(prices[holder['name']])
        result = (holder['name'], holder['shares'], float(prices[holder['name']]), Change)
        stockList.append(result)
    print("StockList : ", stockList)
    for name, shares, price, change in stockList:
        print(f"{name: 10s} {shares: 10d} {price: 10.2f} {chage:10.2f}")

    return stockList
```

### Exercise 2.11: Adding some headers

```python
#Excercise 2-11
headers = ('name', 'shares', 'price', 'change')
print("%10s %10s %10s %10s" %headers)
print(("-" * 10 + ' ') * len(headers))

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
```

*result is following.*

```python
---------- ---------- ---------- ---------- 
        AA        100       9.22      22.98
       IBM         50     106.28     -15.18
       CAT        150      35.46      47.98
      MSFT        200      20.89      30.34
        GE         95      13.48      26.89
      MSFT         50      20.89      44.21
       IBM        100     106.28     -35.84
```

Suppose you had a tuple of header names like this.

```python
headers = ('name', 'shares', 'price', 'change')
```

Add code to your program that takes the above the tuple of headers and creates a string where each header names is right-aligned in a 10-character wide field and each field is separated by a single space.

```
print(('*' * 10+ ' ') * len(headers))
```

### Exercise 2.12: Formatting Challenge

How would you modify your code so that the price includes the currency symbol `$` and the output like this.

```
Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100      $9.22     -22.98
       IBM         50    $106.28      15.18
       CAT        150     $35.46     -47.98
      MSFT        200     $20.89     -30.34
        GE         95     $13.48     -26.89
      MSFT         50     $20.89     -44.21
       IBM        100    $106.28      35.84
```

*Code here*

```
>>> dollarMark  = '$'
>>>for name, shares, price, change in report:
      print(f'{name:>10s} {shares:>10d} {dollarMark+str(price):>10s} {change:>10.2f}')
```

*results is following*

```
---------- ---------- ---------- ---------- 
        AA        100      $9.22      22.98
       IBM         50    $106.28     -15.18
       CAT        150     $35.46      47.98
      MSFT        200     $20.89      30.34
        GE         95     $13.48      26.89
      MSFT         50     $20.89      44.21
       IBM        100    $106.28     -35.84
```

[Contents](../Contents.md) \| [Previous (2.2 Containers)](02_Containers.md) \| [Next (2.4 Sequences)](04_Sequences.md)

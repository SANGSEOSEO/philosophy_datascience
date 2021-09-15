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

The part `{expression:format}` is replaced. It is commonly used with `print`.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```

### Format codes



```code

```



```code

```

### Dictionary Formatting



```python

```



### format() method



```python

```



### C-Style Formatting



```python

```



```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>>
```

## Exercises

### Exercise 2.8: How to format numbers



```python

```



```python

```

### Exercise 2.9: Collecting Data

```

```



```python

```

### Exercise 2.10: Printing a formatted table

```python

```



```python

```

### Exercise 2.11: Adding some headers

```python

```



```python

```



```python

```

```

```

### Exercise 2.12: Formatting Challenge

```

```

[Contents](../Contents.md) \| [Previous (2.2 Containers)](02_Containers.md) \| [Next (2.4 Sequences)](04_Sequences.md)

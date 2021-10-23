[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)

# 3.3 Error Checking

Although exceptions were introduced earlier, this section fills in some addition details about error checking and exception handling.

### How programs fail

Python performs no checking or validation of function argument types or values. A function will work on any that is compatible with the statements in the function.

**파이썬에서 함수로 전달되는 인자의 타입 체킹 혹은 검증이 없음에 유의**

```python
def add(x, y):
    return x + y

sum_val = add(3,4)  #같은 숫자형 타입으로 넘김
print(sum_val)  # 7

print(add("Hello", "World")) # HelloWorld
print(add("3", "World"))   # 3World 같은 string타입으로 넘김
```

If there are errors in a function, they appear at run time(as an exception).

```python
print(add(3, "4"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

To verify code, there is a strong emphasis on testing(covered later).

### Exceptions

Exceptions are used to signal errors. To raise an exception yourself, use `raise` statement.

```python
if name not in Authorized:
  raise RuntimeError(f'{name} not authorized.')
```

To catch an exception , use `try..except`.

```python
try:
  authenticate(name)
except RuntimeError as error:
  print(error)
```

### Exception handling

Exception propogates to the first matching `except`.

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # Exception raised here

def spam():
    grok()                        # Call that will raise exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception caught here
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Exception does NOT arrive here
        ...

foo()
```

To handle the exception, put statements in the `except` block. You can add any statements you wanto to handle the error.

```python
def grok():
  raise RuntimeError('Whoa!')

def bar():
  try:
    grok()
  except RuntimeError as e: # Exception caught here
    statements              # Use this statements
    statements
    ...
 
bar()
```

After handling, execution resumes with the first statement after the `try-except`.

```python
def grok():
  raise RuntimeError("Whoa")
  
def bar():
  try:
    grok()
  except RuntimeError as e:  # Exception caught here
    statements               # Resume execution here
    statements
    ....

bar()  #호출
```

### Built-in Exceptions

There are about two-dozen built-in exceptions. Usually the name of the exception is indication of what's wrong(e.g., a `valueError`is raised because you supplied a bad value). This is not an exhausitive list. Check the [documentation](https://docs.python.org/3/library/exceptions.html) for more.

```python
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
```

### Exception values

Exception have an associated value.It contains more specific information aboutn what's wrong.

```python
raise RuntimeError('Invalid user name')
```

This value is part of the exception intance that's placed in the variable supplied to `except`.

```
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e` is an instance of the exception type. However, it often looks like a string when printed.

```
except RuntimeError as e:
    print('Failed : Reason', e)
```

### Catching Multiple Errors

You can catch different kind of exceptiond using multiple `except` blocks.

```python
try:
  ...
except ValueError as v:
  ...
except IndexError as i:
  ...
except IOError as e:
  ....
```

Alternatively, if the statements to handle them is the same, you can group them:

```python
try:
  ...
except  (IOError, ValueError, RuntimeError) as e:
  ...
```

### Catching All errors

To catch an Exception, use `exception` like this:

```python
try:
  ...
except Exception:
  print("An Error occurred!")
```

In general, writing code like that is a bad idea because you'll have no idea why it failed.

### Wrong Way to Catch Errors

Here is the wrong way to catch exceptions.

```python
try:
  go_do_something()
except Exception:
  print("Error occurred!")
```

This catches all possible errors and it may make it impossible to debug when the code is failing for some reason you did't expect at all(e.g., uninstalled python module, etc.).

### Somewhat Better Approach

If you are going to catch all errors, this is a more sane approach.

```python
try:
  ...
except Exception as e:
  print("The following error occured!!", e)
```

It reports a specific reason for failure. It is almose always a good idea to have some mechanism for viewing/reporting erros when you write code that catches all possible exceptions.

In general though, It's better to catch the error as narrowly as is possible. Only catch the erros you can actually handle. Let other errors pass by --maybe some other code can handle them.

### Raising an Exception

Use `raise` to propogate a caught error.

```python
try:
  go_do_something()
except Exception as e:
  print("Computer says no. Reason : ", e)
  raise
```

This allows you to take action(e.g., logging) and pass the error on to the caller.

### Exception Best Practices

Don't catch exceptions. Fail fast and loud. If it's important, someone else will take care of the problem. Only catch an exception if you are *that* someone. That is, only catch errors where you can recover and sanely keep going.

### `finally` statement

It specifies code that must run regardless of whether or not an exception occurs.

```
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

Commonly used to safely manage resources (especially locks, files, etc.).

### `with` statement

In modern code, `try-finally` is often replaced `with` statement.

```python
lock = Lock()
with lock:
  #Lock statement
  ...
  #Lock Released
```

A more familiar example:

```python
with open(filename) as f:
  #Use the file
  ...
  #File closed
```

`with` defines a usage *context* for a resource. When execution leaves that context, resources are released. `with` only works certain objects that have been specifically programmed to support it.

### Exercises

------

#### Exercise #3-8: Rasing exception

The `parse_csv()` function you wrote in the last section allows user-specified columns to be selected, but that only works if the input data file has column headers.

Modify the code so that an exception gets raised if both the `select` and `has_headers=False` arguments are passed. For example:

```python
>>> parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Having added this one check, you might ask if you should be performing other kinds of sanity checks in the function. For example should you check that the filename is a string, that types is a list, or anything of that nature?

As a general rule, it's usually best to skip such tests and to just let the program fail on bad inputs. The taceback message will point at the source of the problem and can assist in debugging.

The main reason for adding the the check is to avoid running the code in a non-sensical mode(e.g., using a feature that requires column headers, but simultaneously specifying that there are no headers).

This indicates a programming error on the part of the calling code. Checking for cases that "aren't  supposed to happen" is often a good idea.

The following is full source that has been added the modified parts.

```python
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    컬럼을 리스트 타입 인자로 받아 원하는 컬럼만 뽑아서 리턴
    :param filename:
    :param select: list
    :param type: list
    :param has_headers : 헤더 존재 여부
    :param delimiter : 구분자
    :return: dictionary를 내포한 리스트
    """
    import csv

    """
    has_headers가 없는데 뽑고자 하는 컬럼을 파라미터로 주면 에러가 나므로 
    해당 에러에 대한 Exception처리 
    Exercise 3-8
    """
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    with open("Work/Data/"+filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        # read the file header
        headers = next(rows) if has_headers else []

        if select:
            col_idx = [headers.index(name) for name in select]
            headers = select
        else:
            col_idx = []

        records = []

        for row in rows:
            if not row:
                continue
            if col_idx:
                row = [row[idx] for idx in col_idx]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if not has_headers:  #헤더가 없으면 튜플로 변환
                records.append(tuple(row))
            else:
                record = dict(zip(headers, row))
                records.append(record)
    return records
```



#### Exercise 3.9: Catching exceptions

The  `parse_csv()` function you wrote is used to process the entire contents of a file. However, in the real-world, it's possible that input files might have corrupted, missing, or dirty data.

Try this experiment.

```python
>>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modify the `parse_csv()` function to catch all `ValueError` exceptions generated during record creation and print a warning message for rows that can't be converted.

The message should include the rows number and information about the reason why it failed.

To test your functions, try reading the file `Data/missing.csv` above. For example:

```python
>>> from Work import file_parse as fp
>>> portfolio = fp.parse_csv('Data/missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}]
>>>
```

execution result as follows:

```python
# Read Evaluate Print Loop
a = ["100", "400", 500, 46.8]

for val, idx in enumerate(a):
    print(val, idx)

portfolio = fp.parse_csv("missing.csv", types=[str, int, float])

>>>
Row 3 : Couldn't convert ['MSFT', '', '51.23']
Row 3 : invalid literal for int() with base 10: ''
Row 6 : Couldn't convert ['IBM', '', '70.44']
Row 6 : invalid literal for int() with base 10: '

[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': '', 'price': '51.23'}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': '', 'price': '70.44'}
```

The full source as follows:

```python
# fileparse.py
# Exercise 3.3
# Exercise 3.4
# Exercise 3.7
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    컬럼을 리스트 타입 인자로 받아 원하는 컬럼만 뽑아서 리턴
    :param filename:
    :param select: list
    :param type: list
    :param has_headers : 헤더 존재 여부
    :param delimiter : 구분자
    :return: dictionary를 내포한 리스트
    """
    import csv
    """
    has_headers가 없는데 뽑고자 하는 컬럼을 파라미터로 주면 에러가 나므로 
    해당 에러에 대한 Exception처리 
    Exercise 3-8
    
    Exercise 3-9
    타입변환시 에러가 나는 경우 예외처리 하기 
    """
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    with open("Work/Data/"+filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        # read the file header
        headers = next(rows) if has_headers else []

        if select:
            col_idx = [headers.index(name) for name in select]
            headers = select
        else:
            col_idx = []

        records = []

        # enumerate객체는 튜플로 리턴하는데
        # 앞에 원소가 인덱스
        for idx, row in enumerate(rows):
            if not row:
                continue
            if col_idx:
                row = [row[idx] for idx in col_idx]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {idx} : Couldn't convert {row}")
                    print(f"Row {idx} : {e}")

            if not has_headers:  #헤더가 없으면 튜플로 변환
                records.append(tuple(row))
            else:
                record = dict(zip(headers, row))
                records.append(record)
    return records
```

#### Exercise 3-10

Modify the `parse_csv()` function so that parsing error messages can be silenced if explicitly desired by the user.

For example:

```python
>>> portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}]
>>>
>>> portfolio1 = fp.parse_csv("missing.csv", types=[str, int, float], silence_errors=False)
>>> print(portfolio1)

Row 3 : Couldn't convert ['MSFT', '', '51.23']
Row 3 : invalid literal for int() with base 10: ''
Row 6 : Couldn't convert ['IBM', '', '70.44']
Row 6 : invalid literal for int() with base 10: ''
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': '', 'price': '51.23'}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': '', 'price': '70.44'}]

```

If you want to display `exception message` , pass `silence_errors` argument  with `True`.

```python
>>> portfolio2 = fp.parse_csv("missing.csv", types=[str, int, float], silence_errors=True)
>>> print(portfolio2)
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': '', 'price': '51.23'}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': '', 'price': '70.44'}]
```

Error handling is one of the most difficult things to get right in most programs. As a general rule, you shouldn't silently ignore errors. Instead, It's better to report problems and to give the user an option to the silence the error message if they choose to do so.

[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)

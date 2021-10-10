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



[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)
[Contents](../Contents.md) \| [Previous (2.6 List Comprehensions)](06_List_comprehension.md) \| [Next (3 Program Organization)](../03_Program_organization/00_Overview.md)

# 2.7 Objects

This section introduces more details about Python's internal object model and discussed some matters related to memory management , copying, and type checking.

### Assignment

Many operations in Python are related to assigning or storing values.

```python
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```

*A caution: assignment operations **never make a copy** of the value being assigned. All assignments are merely reference copies(or pointer copies if you prefer)*

### Assignment example

Consider this code fragment.

```
a = [1, 2, 3]
b = a
c = [a, b]
```

A picture of the underlying memory operations. In this example, there is only one list object `[1,2,3]`, but there are four different references to it.

![references](https://user-images.githubusercontent.com/70785000/134735855-571c3a64-3f5c-4f6b-b615-d9b7a3052461.png)

This means that modifying a value affects all references.

```
>>> a.append(999)
>>> print(a)
>>> print(b)
>>> print(c)
>>>
[1, 2, 3, 999]
[1, 2, 3, 999]
[[1, 2, 3, 999], [1, 2, 3, 999]]
```

Notice how a change in the original list shows up everywhere else. This is because no copies were made.

Everything is pointing to the same thing.

### Reassigning values

Reassigning a value never overwrites the memory used by the previous value.

```
>>> a = [1,2,3]
>>> b = a
>>> a = [4,5,6]

>>> print(a, id(a))
>>> print(b, id(b))
>>>
[4, 5, 6] 2193505236480
[1, 2, 3] 2193504891072
```

Remember: **Variables are names, not memory locations.**

### Some Dangers

If you don't know about this sharing, you will shoot yourself in the foot at some point. Typical scenario.

You modify some data thinking that it's your own private copy and it accidentally corrupts some data in some other part of the program.

*Commnet: This is one fo the reasons why the primitive datatypes(int, float, string) are immutable (read-only).*

### Identify and References

Use th `is` operatosr to check if two values are exactly the same object.

```
a = [1,2,3]
b = a
print(a is b)
>>>
True
```

`is` compares the object identify(an integer). The indentify can be obtained using `id()`.

```
print(f"a's pointer : {id(a)}")
print(f"b's pointer : {id(b)}")
>>>
a's pointer : 1614629812416
b's pointer : 1614629812416
```

Note: It is almost always better to use `==` for checking objets. The behaviour of `is` is often unexpected.

```
a = [1,2,3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)
print(a == c)
>>>
True
False
True
```

###  Shallow copies

Lists and dicts have method for copying.

```
>>> a = [2, 3, [100, 101], 4]
>>> b = list(a)  # make a copy
>>> a is b
>>>
False
```

It's a new list, but the list items are shared.

```
>>> a[2].append((102))
>>> print(b[2], b)
>>> print(a[2] is b[2])
>>>
[100, 101, 102] [2, 3, [100, 101, 102], 4]
True
```

For example, the inner list `[100, 101, 102]` is being shared. This is known as a shallow copy. Here is a picture.

![shallow](https://user-images.githubusercontent.com/70785000/134738939-106211fc-d1ac-40fc-8a91-c25d2a5626a6.png)

### Deep copies

Sometimes you need to make a copy of an object and all the objects contained within it.

You can use the `copy` module for this.

```
a = [2, 3, [100, 101], 4]
import copy

b = copy.deepcopy(a)
a[2].append(102)
print(b[2], b)
>>>
[100, 101] [2, 3, [100, 101], 4]

>>> print(a[2] is b[2])  # False
```

### Names, Values, Types



[Contents](../Contents.md) \| [Previous (2.6 List Comprehensions)](06_List_comprehension.md) \| [Next (3 Program Organization)](../03_Program_organization/00_Overview.md)
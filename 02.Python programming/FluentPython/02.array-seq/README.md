## Chapter 2. An Array of Sequences

*As you may have noticed, several of the operations mentioned work equally for texts, lists and tables. Texts, lists and tables together are called trains.[...] The `FOR` command also works generically on trains.*

   --- Geurts, Meertens, and Pemberton, ABC Programmers's Handbook

Before creating Python, Guido was a contributor to the ABC Language - a 10 year research project to desing a programming environment for beginners. ABC introduced many ideas we now consider "Pythonc": generic operations on sequences, built-in tuple and mapping types, structure by indentations, strong typing without variable declaration, and more. It's no accident that Python is so user-friendly.

Python inherited from ABC the uniform handling of sequences. Strings, lists  byte sequnces arrays XML elements, and database results share a rich set of common operations including iteration, slicing, sorting, and concatenation.

Understanding the variety of sequences available in Python saves us from reinventing the wheel, and their common interface inspires us to create APIs that properly support and leverage existing and future sequence type.

Most of the discussion in this chapter applies to sequences in general, from the familiar `list` to `str` and `bytes` types that are new in Python 3. Specific topics on lists, tuples, arrays, and queues are also covered here.

#### Overview of Built-In Sequences

The standard libray offers a rich selection of sequnces types implemented in C:

Container sequences is as follows:

`list`, `tuple`,and `collections.deque` can hold items of different types

Flat sequences:

`str`, `bytes`,	`bytesarray`, `memoryview`, and `array.array` hold items of one type.

The following figure helps visualize how mutable sequences differ from immutable ones, while also inheriting several methods from them. Note that the built-in concrete sequence types do not actually subclass the **Sequnce** and **MutableSequence** abstract base classes(ABCs) depicted, but the ABCs are still useful as a formalization of what functionality to expect from a full-featured sequnce type.

![flup_0201](https://user-images.githubusercontent.com/70785000/147822885-057938ed-1f88-4114-8ad2-cbddba48c708.png)

Keeping in mind these common traits-mutable versus immutable; container versus flat-is helpful to extrapolate what you know about one sequnces type to others.

The most fundamental sequnce type is the **`list`**- mutable and mixed-type. 

I am sure your are comfortable handling them, so we'll jump right into **list comprehensions**, a powerful way of building lists that is somewhat underused because the syntax may be unfamiliar. **Mastering list comprehensions** opens the door to generator expressions, which - among other uses-can produce elements to fill up sequences of any type. Both are the subject of the next section.

#### List Comprehensions and Generator Expressions

A quick way to build a sequence is using a **list comprehensions**(if the target is a **`list`**) or a generate expressions (for all other kinds of sequences). 

##### List Comprehensions and Readability

see method between **list comprehensions** and **Regular for  statement.**

```python
>>> symbols = [$¢£¥€¤]
>>> codes = []
>>> for symbol in symblos:
  		codes.append(ord(symbol))  // get a ASCII code value 
>>> codes
[36, 162, 163, 165, 8364, 164]
```

```python
>>> codes = [ord(symbol) for symbol in symbols]
>>> codes
[36, 162, 163, 165, 8364, 164]
```

*If the list comprehension spans more than two lines, it is probably best to break it apart or rewirte as a plain old `for` loop.*

> In Python code, line breaks are ignored inside pairs of `[]`, `{}`, or `()`.So you can build multilines lists. listcomps, genexps dictionaries and the like without using the ugly `\` line continuation escape.

List comprehensions, generator expressions, and their siblings `set` and `dict` comprehensions now have their own local scope, like functions. Variables assigned withins the expression are local, but variables in the surrounding scope can still be referenced. Even better, the local variables do not mask the variables from the surrounding scope.

```python
Python 2.7.6 (default, Mar 22 2014, 22:59:38)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 'my precious'
>>> dummy = [x for x in 'ABC']
>>> x
'C'
```

Python 3.xxx Environment.

```python
>>> x = 'My Precious'
>>> dummy = [x for x in 'ABC']  #regard x as a local variable , put a character in x
>>> dummy
['A', 'B', 'C']
```

Check this out:

```python
>>> x = 'ABC'
>>> dummy = [org(x) for x in x]  # The list comprehensions produces the expected list.
>>> dummy
[65, 66, 67]
>>> x  # x is preserved
'ABC'
```

##### Listcomps Versus map and filter

Listcomps do everything the `map` and `filter` functions do, without the contorictions of the functionality challenged Python `lambda`.
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

```python
# example 2-3 The sample list built by a listcomp and a map / filter composition
>>> symbols = '$¢£¥€¤'
>>> beyond_ascii = [ord(symbol) for symbol in symbols]
>>> beyond_ascii
[36, 162, 163, 165, 8364, 164]
```

```python
# the following is the same 
>>> filter(lambda x : x > 127, map(ord, symbols))
<filter object at 0x000001E454A5C250>
>>> list(filter(lambda x:  x> 127, map(ord, symbols)))
[162, 163, 165, 8364, 164]
```

I used to believe that `map` and `filter` were faster thatn the equivalent listcomps, but *Alex Martelli* pointed out that's not the case-at least not in the preceding examples. 

This example will be handled later on.

##### Cartesian Products

Listcomps can generate lists from the Cartesian product of two or more iterables. 

The items that make up the cartesian product are tuples made from items from every input iterable. The resulting list has length equan to the lengths of the input iterables multipled.

![](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781491946237/files/assets/flup_0202.png)

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M','L']
>>> tshirts = [(color, size) for color in colors for size in sizes]
>>> print(f"TShirts tuples are  {tshirts}. ")
TShirts tuples are  [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]. 
>>> for size in sizes:
       for color in colors:
          print((color, size))
('black', 'S')
('white', 'S')
('black', 'M')
('white', 'M')
('black', 'L')
('white', 'L')        
```

##### Generator Expressions

To initialize tuples, arrays, and other types of sequences, you could also start form a listcomp, but a genexo saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.

Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.

```python
# Initializing a tuple and an array from a generator expression
>>> symbols = '$¢£¥€¤'
>>> tuple(ord(symbol) for symbol in symbols)
(36, 162, 163, 165, 8364, 164)

# 'I' means Inter, 'U'- Unsigned integer
>>> import array
>>> array.array("I", (ord(symbol) for symbol in symbols))
array('I', [36, 162, 163, 165, 8364, 164])
```

The `array` constructor takes two arguments, so the parentheses around the generator expressions are mandatory. The first argument of the `array` constructor defines the strorage type used for the numbers in the array.

Using a genexp with a cartesian product

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L'] 
>>> for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes): #(1) generator expression 
       print(tshirt)
    
black S
black M
black L
white S
white M
white L
```

The generator expression yields items one by one; a list with all T-shirt variations is never produced in this example.

Chapter 14 will be take care of the generator expression later on.

#### Tuples Are Not Just Immutable Lists

Some introuctory texts about Python presents tuples as "immutable lists", but that is short selling them. Tuples do double duty: they can be used as immutable lists and also as records with no field names. This use is sometimes overlooked, so we will start with that.

##### Tuples as Records

Tuples hold records: each items in the tuple holds the data for one field and the position of the item gives its meaning.

If you think of a tuple just as an immutable list, the quantity and the order of the items may or may not be important, depending on the context.

But when using a tuple as a collection of fields, the number of items is often fixed and their order is always vital.

```python
# Tuples used as records
# Examples 2-7 Tuples used as records
lax_coordinates = (33.9425, -118.408056) #  latitude and logitude of LA Internaltional Airport
city,year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # Tkyo Postal inforamtion
traveler_ids = [('USA', '31195855'), ('BRA', 'CES342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):  
    # tuple unpacking
    print("%s /%s" % passport)
```

```python
C:\Anaconda3\envs\PyProject\python.exe C:/PythonProject/FluentPython/Example2-7.py
BRA /CES342567
ESP /XDA205856
USA /31195855
```

```python
for country, _ in sorted(traveler_ids):  
    print(country)
```

```
# Output
# `_` not interested in the second items , so it's assigned to `_` , a dummy variable
BRA
ESP
USA
```

We call the above `Tuple Unpacking`.

##### Tuples Unpacking

> Tuples unpacking works with any iterable object. The only requirements is that the iterable yields exactly one item per variable in the receiving tuple, unless you use a star (`*`) to capture excess items 

```python
# tuple unpacking
>>>latitude, longitude = lax_coordinates
>>>print(f"latitude -> {latitude}, longgitude -> {longitude}")

>>>
latitude -> 33.9425, longgitude -> -118.408056
```

```python
# Another example of tuple unpacking
a, b = divmod(20, 8) # 몫과 나머지를 리턴

print(f"a -> {a}, b -> {b}")

# `*` - prefixing an aurgument with a star when calling a function
t = divmod(20, 8)
print(*t)

# `*` - prefixing an aurgument with a star when calling a function
t = divmod(20, 8)
print(*t)
```

```python
a -> 2, b -> 4
2 4
```


# 01.Python Data Model

*Guido's sense of the aesthetic of language desing is amazaging. I've meet many fine language designers who could build theoretically beautiful language that no one would ever use, but Guido is one of those rare people who can build a language that is just slighly less theoretically beautiful but therby is a joy to write programs in.*

-Jim Hugunin, Creator of Jython, cocreator of AspectG, architect of the .Net DLR



One of the best qualififies is the consistency in codeing using Python. 

While coding with any framework , we would encounter the special method are always written with leading and trailing double underscores(i.e., `__getitem__`)

The special method , magic method or dunder method allows your objects to implement , support, and interact with basic langauge contrucst such as:

* Iteration
* Collections
* Attribute access
* Operator overloading
* Function and method invocation
* Object creation and desctruction
* Stirng representation and formatting
* Managed contexts(i.e., `with` blocks )

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrechDeck():
    '''
    Example 1-1
    A deck as a sequence of cards
    '''
    ranks = [str(n) for n in range(2, 11)]+ list('JQKA')
    suits = 'spade diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
       """
       return object's length
       """
        return len(self._cards)

    def __getitem__(self, pos):
      """
      Reading specificard cards from the deck
      """
        return self._cards[pos]
```

The first thing to note is the use of `collecitns.namedtuple()` to contruct a simple class to represent a individual card.

```python
>>> import sys
sys.path.append("C:\PythonProject\FluentPython")
>>> import os
os.getcwd()
'C:\\PythonProject'
>>>os.chdir("C://PythonProject/FluentPython")
>>>import frechdeck
>>>Card = collections.namedtuple('Card', ['rank', 'suit'])
>>>beer_card = Card('7', 'diamonds')
>>>beer_card
Card(rank='7', suit='diamonds')
```

But the point of this example is the `FrechDeck` class. It's short, but it packs a punch. First. like any standard Python colleciton, a deck reponds to the `len()` function by returning the number of cards in it.

```python
>>> deck = frenchdeck.FrechDeck()
>>>deck
<frenchdeck.FrechDeck object at 0x000001B2588F0CD0>
>>> len(deck)
52
```

Returning a specifica card from the Decks- says the first or last card from the `Deck`.

And this is what the `__getitem__`method provides:

```python
>>> deck[0]
Card(rank='2', suit='spade')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>> deck[10]
Card(rank='Q', suit='spade')
```

What if we get a random card from a sequence. Should we need to create a new method for that?

No need. Python already has a function to get a random item from a sequence: *`random.choice()`*

```python
>>> from random import choice
>>> choice(deck)
Card(rank='7', suit='diamonds')
>>> choice(deck)
Card(rank='9', suit='clubs')
```

Check this out. `deck` object supports `slicing` cause `__getitem__()` delegate to the `[]` of `self._cards`.

```python
>>> deck[:3]
[Card(rank='2', suit='spade'), Card(rank='3', suit='spade'), Card(rank='4', suit='spade')]
>>> deck[:13]
deck[:13]
[Card(rank='2', suit='spade'), Card(rank='3', suit='spade'), Card(rank='4', suit='spade'), Card(rank='5', suit='spade'), Card(rank='6', suit='spade'), Card(rank='7', suit='spade'), Card(rank='8', suit='spade'), Card(rank='9', suit='spade'), Card(rank='10', suit='spade'), Card(rank='J', suit='spade'), Card(rank='Q', suit='spade'), Card(rank='K', suit='spade'), Card(rank='A', suit='spade')]

```

`deck` is also iterable just by implementing `__getitem__`.

```python
>>> for card in deck:
       print(card)    
Card(rank='2', suit='spade')
Card(rank='3', suit='spade')
Card(rank='4', suit='spade')
...
Card(rank='K', suit='hearts')
Card(rank='A', suit='hearts')
```

`deck` is also be reversed. check the following soltuion:

```python
>>> for card in reversed(deck):
     print(card)
ard(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
.................
Card(rank='2', suit='spade')
Card(rank='3', suit='spade')
Card(rank='4', suit='spade')
```

Iteration is often implicit. If a collection has no `__contains__` method, the `in` operator does a sequential scan. Case in point: `in` works with our `FenchDeck` class becuase it is iterable. Check this out.

```python
>>> import collections
>>> Card = collections.namedtuple('Card', ['rank', 'suit'])
>>> Card
<class '__main__.Card'>
>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beast') in deck
False
```

 How about sorting? A common system of ranking cards is by rank(with aces being highest), then by suit in the order of spades(highest), then hearts, diamonds, and clubs(lowest). Here is a function that ranks cards by that rule, returnings `0` for 2 of clubs and `51` for the ace of spades:

```python
>>> suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
>>> def spaeds_high(card):
    	rank_value = frenchdeck.FrechDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
```

### How Special Methods Are Used

The first thing you should know that special method is that they are meant to be called by Python interpreter , and not by you.

For example. the statement `for i in x:` actually causes the invocation of `iter(x)`, which in turn may call `x.__iter__()` if that is available.

Check this another thing.

The only special method that is frequently called by user code directly is `__init__`, to invoke the initializer of the superclass in your own `__init__` implementation.

If you need to invoke a special method, it is usually better to call the related builtin function (e.g., `len`,`iter`,`str`, etc). These built-ins call the corresponding special method, but often provide other sevices and- for built-in types-are faster than method calls. 

See, for example, " [A Closer Look at the iter Function]()"

### Emulating Numeric Types

Serveral special methods allows user objects to respond to operators such as `+`.

Check the following example.

```python
# A simple two-dimensional vector class
# Vector operation
from math import hypot

class Vector:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vector(%r, %r)' %(self.x , self.y)
      
    def __abs__(self):
        """
        :return: absolute value
        """
        return hypot(self.x, self.y)
      
    def __bool__(self):
        return bool(abs(self))
      
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

The above `class` aim to test Vector operation.

The following is snippet test for Vector.

```python
>>> import os
>>> os.getcwd()
'C:\\PythonProject'
>>> os.chdir("C:\PythonProject\FluentPython")
>>> import sys
>>> sys.path.append("C:\PythonProject\FluentPython")
>>> from vector2d import Vector
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
```

```python
>>> v1 + v2
Vector(4, 5)
>>> v = Vector(3,4 )
>>> abs(v)
5.0
```

Note how the `+` operator produces a `Vector` result, which is displayed in a friendly manner in the console.

The `abs` built-in function returns the absolute value of integers and floats, and the magnitude of `complex` numbers, so to be consistent, our API also uses `abs` to calculate the magnitude of a vector:

![flup_0101](https://user-images.githubusercontent.com/70785000/147795314-cd2bcd31-fe9b-431a-84ed-54c903564a19.png)


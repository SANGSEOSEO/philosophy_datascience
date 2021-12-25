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
```

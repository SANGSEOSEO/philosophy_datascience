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
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]
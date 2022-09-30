# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 3
suits = ["clubs", "diamonds", "spade", "hearts"]
ranks = [None, "A"] + [x for x in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 12
class Card:
    "A playing card, created by using `rank` from `ranks` and `suit` from `suits`"
    def __init__(self,
                 suit: int, # An index into `suits`  
                 rank: int): # An index into `ranks`
        self.rank, self.suit = rank, suit
    
    def __str__(self):
        return f"({ranks[self.rank]}, {suits[self.suit]})"
    
    __repr__ = __str__
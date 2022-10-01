nbdev_cards
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

A deck of cards demo of nbdev basd on ideas from Think Python 2nd
Edition by Allen B. Downey

## Install

Install using:

    pip install nbdev_cards

or:

    conda install -c fastai nbdev-cards

## How to use

This lib provides a
[`Card`](https://prp0x80.github.io/nbdev_cards/card.html#card) class you
can use to create, display, and compare playing cards:

``` python
Card(suit=1, rank=3)
```

    (3, diamonds)

Suits are numbered according to the list:

``` python
suits
```

    ['clubs', 'diamonds', 'spade', 'hearts']

Another class this lib provides is
[`Deck`](https://prp0x80.github.io/nbdev_cards/deck.html#deck)

``` python
Deck()
```

    (A, clubs); (2, clubs); (3, clubs); (4, clubs); (5, clubs); (6, clubs); (7, clubs); (8, clubs); (9, clubs); (10, clubs); (J, clubs); (Q, clubs); (K, clubs); (A, diamonds); (2, diamonds); (3, diamonds); (4, diamonds); (5, diamonds); (6, diamonds); (7, diamonds); (8, diamonds); (9, diamonds); (10, diamonds); (J, diamonds); (Q, diamonds); (K, diamonds); (A, spades); (2, spades); (3, spades); (4, spades); (5, spades); (6, spades); (7, spades); (8, spades); (9, spades); (10, spades); (J, spades); (Q, spades); (K, spades); (A, hearts); (2, hearts); (3, hearts); (4, hearts); (5, hearts); (6, hearts); (7, hearts); (8, hearts); (9, hearts); (10, hearts); (J, hearts); (Q, hearts); (K, hearts)

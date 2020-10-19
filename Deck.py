#############################################
# Author: Pranay Gundam
#############################################

# This file contains all the types of deck objects

import pygame
from Cards import *
import random

# This class is the Deck object, which contains a list of card objects from the
# Cards file and then randomizes their order.
class Deck(object):
    def __init__(self, cardList):
        self.cards = cardList
        random.shuffle(self.cards)

    # from https://www.cs.cmu.edu/~112/notes/unit5-case-studies.html#twentyOne
    def cardsLeft(self):
        return len(self.cards)

    #from https://www.cs.cmu.edu/~112/notes/unit5-case-studies.html#twentyOne
    def dealCard(self):
        return None if (self.cards == [ ]) else self.cards.pop()

# This class is a subclass of the Deck object and creates a deck with cards that
# are all considered Door Cards. It gets this information about the cards 
# from the Cards file.
class DoorDeck(Deck):
    def __init__(self):
        cardList = []
        cardList += monsterList
        cardList += playerClassList
        cardList += raceList
        super().__init__(cardList)

# This class is a subclass of the Deck object and creates a deck with cards that
# are all considered Treasure Cards. It gets this information about the cards 
# from the Cards file.
class TreasureDeck(Deck):
    def __init__(self):
        cardList = []
        cardList += armourList
        cardList += curseList
        cardList += consumableList
        super().__init__(cardList)

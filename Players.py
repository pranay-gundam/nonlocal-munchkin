#############################################
# Author: Pranay Gundam
#############################################

# This file contains all the code concerning Player objects

import pygame
from Deck import *
from Cards import *

# This class is a Player object that includes attributes that have certain 
# information about a player that includes the player name, his/her level, their
# equiped armour, the cards in their hand, and any curses that apply to them.
class Player(object):
    def __init__(self, name, deckTreasure, deckDoor):
        self.hand = []
        for count in range(4):
            self.hand.append(deckTreasure.dealCard())
            self.hand.append(deckDoor.dealCard())
        self.level = 1
        self.curses = []
        self.name = name
        self.race = None
        self.playerClass = None
        self.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
    
    def calcBattlePower(self):
        handPower = 0
        for card in self.armour:
            if self.armour[card] != None:
                handPower += self.armour[card].power
        lvlpower = 0
        classpower = 0
        if self.race != None:
            lvlpower = self.race.power
        if self.playerClass != None:
            classpower = self.playerClass.power
        return handPower + self.level + lvlpower + classpower

    def changeRace(self, race):
        self.race = race
    
    def changePlayerClass(self, playerClass):
        self.playerClass = playerClass
    
    def levelUp(self, levels):
        self.level += levels
    
    def levelDown(self, levels):
        self.level -= levels
    
    def applyArmour(self, card):
        armourType = card.armourType
        previousArmour = self.armour[armourType]
        self.armour[armourType] = card
        return previousArmour
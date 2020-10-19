#############################################
# Author: Pranay Gundam
#############################################


# This file contains the code to run the gameAI, although some of the motivation
# for my game AI came from the mini-lecture on gameAI, virtually all of the code
# here is my own.

import pygame
from Cards import *
from Players import *
from Deck import *

class PassiveRobot(object):
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
        for card in self.hand:
            if isinstance(card, Armour):
                handPower += card.power
        lvlpower = 0
        classpower = 0
        if self.race != None:
            lvlpower = self.race.power
        if self.playerClass != None:
            classpower = self.playerClass.power
        return handPower + self.level + lvlpower + classpower

    def fightMonster(self, monster):
        itemsToUse = []
        levelDifference = monster.power - self.calcBattlePower()
        if levelDifference < 0:
            return itemsToUse
        else:
            for usableCard in self.hand:
                if (isinstance(usableCard, Curse) or isinstance(usableCard, Consumable) 
                    and usableCard.power > 0):
                    levelDifference -= usableCard.power
                    itemsToUse.append(usableCard)
                    if levelDifference < 0:
                        return itemsToUse
            if levelDifference < 0:
                return itemsToUse
            else:
                return []
    
    def discardApplyCards(self):
        index = 0
        while len(self.hand) > 5 and index < len(self.hand):
            discardCard = self.hand[index]
            if self.race == None and isinstance(discardCard, Race):
                self.race = discardCard
                self.hand.pop(index)
            
            elif self.playerClass == None and isinstance(discardCard, PlayerClass):
                self.playerClass = discardCard
                self.hand.pop(index)

            elif ((isinstance(discardCard, PlayerClass) or isinstance(discardCard, Race))
                   and (self.playerClass != None and self.race != None)):
                self.hand.pop(index)

            elif (isinstance(discardCard, Armour)):
                if (self.armour[discardCard.armourType] == None 
                    or self.armour[discardCard.armourType].power < discardCard.power):
                    self.hand.pop(index)
                    self.armour[discardCard.armourType] = discardCard
                
                elif self.armour[discardCard.armourType].power >= discardCard.power:
                    self.hand.pop(index)
            
            elif index == len(self.hand) - 1 :
                while len(self.hand) > 5:
                    self.hand.pop()

            else:
                index += 1

    def applyArmour(self, armourCard, index):
        for armourSpot in self.armour:
            if armourCard.armourType == armourSpot and self.armour[armourSpot] == None:
                self.hand.pop(index)
                self.armour[armourSpot] = armourCard
                return True
            elif armourCard.armourType == armourSpot and self.armour[armourSpot].power < armourCard.power:
                self.hand.pop(index)
                self.hand.append(self.armour[armourSpot])
                self.armour[armourSpot] = armourCard
                return True
        return False
                    
class AgroRobo(object):
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
        for card in self.hand:
            if isinstance(card, Armour):
                handPower += card.power
        lvlpower = 0
        classpower = 0
        if self.race != None:
            lvlpower = self.race.power
        if self.playerClass != None:
            classpower = self.playerClass.power
        return handPower + self.level + lvlpower + classpower

    def attack(self, monsterCard, otherPlayer, cardsInPlay):
        cardsToAdd = []
        index = 0
        playedCardsPower = 0
        for card in cardsInPlay:
            playedCardsPower += card.power

        while index < len(self.hand):
            card = self.hand[index]
            if ((isinstance(card, Consumable) or isinstance(card, Curse))
                and (monsterCard.power >= otherPlayer.calcBattlePower() + card.power + playedCardsPower) 
                and (monsterCard.power < otherPlayer.calcBattlePower() + playedCardsPower)) :
                cardsToAdd += [card]
                self.hand.pop(index)
                break
            else:
                index += 1
        return cardsToAdd

    def discardApplyCards(self):
        index = 0
        while len(self.hand) > 5 and index < len(self.hand):
            discardCard = self.hand[index]
            if isinstance(discardCard, Race) and (self.race == None or self.race.power < discardCard.power):
                self.race = discardCard
                self.hand.pop(index)
            
            elif isinstance(discardCard, PlayerClass) and (self.playerClass == None or self.playerClass.power < discardCard.power):
                self.playerClass = discardCard
                self.hand.pop(index)

            elif ((isinstance(discardCard, PlayerClass) or isinstance(discardCard, Race))
                   and (self.playerClass != None and self.race != None)):
                self.hand.pop(index)

            elif (isinstance(discardCard, Armour)):
                if (self.armour[discardCard.armourType] == None 
                    or self.armour[discardCard.armourType].power < discardCard.power):
                    self.hand.pop(index)
                    self.armour[discardCard.armourType] = discardCard
                
                elif self.armour[discardCard.armourType].power >= discardCard.power:
                    self.hand.pop(index)

            elif (isinstance(discardCard, Monster)):
                if discardCard.power >= self.calcBattlePower():
                    self.hand.pop(index)
                else:
                    index += 1

            elif index >= len(self.hand) - 1:
                while len(self.hand) > 5:
                    self.hand.pop()

            else:
                index += 1


    def applyArmour(self, armourCard, index):
        for armourSpot in self.armour:
            if armourCard.armourType == armourSpot and self.armour[armourSpot] == None:
                self.hand.pop(index)
                self.armour[armourSpot] = armourCard
            elif armourCard.armourType == armourSpot and self.armour[armourSpot].power < armourCard.power:
                self.hand.pop(index)
                self.hand.append(self.armour[armourSpot])
                self.armour[armourSpot] = armourCard

    def fightMonster(self, monster):
        itemsToUse = []
        levelDifference = monster.power - self.calcBattlePower()
        if levelDifference < 0:
            return itemsToUse
        else:
            for usableCard in self.hand:
                if (isinstance(usableCard, Curse) or isinstance(usableCard, Consumable) 
                    and usableCard.power > 0):
                    levelDifference -= usableCard.power
                    itemsToUse.append(usableCard)
                    if levelDifference < 0:
                        return itemsToUse
            if levelDifference < 0:
                return itemsToUse
            else:
                return []

class OptimalRobo(object):
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

    def applyArmour(self, armourCard, index):
        for armourSpot in self.armour:
            if armourCard.armourType == armourSpot and self.armour[armourSpot] == None:
                self.hand.pop(index)
                self.armour[armourSpot] = armourCard
            elif armourCard.armourType == armourSpot and self.armour[armourSpot].power < armourCard.power:
                self.hand.pop(index)
                self.hand.append(self.armour[armourSpot])
                self.armour[armourSpot] = armourCard

    def discardApplyCards(self):
        index = 0
        while len(self.hand) > 5 and index < len(self.hand):
            discardCard = self.hand[index]
            if self.race == None and isinstance(discardCard, Race):
                self.race = discardCard
                self.hand.pop(index)
            
            elif self.playerClass == None and isinstance(discardCard, PlayerClass):
                self.playerClass = discardCard
                self.hand.pop(index)

            elif ((isinstance(discardCard, PlayerClass) or isinstance(discardCard, Race))
                   and (self.playerClass != None and self.race != None)):
                self.hand.pop(index)

            elif (isinstance(discardCard, Armour)):
                if (self.armour[discardCard.armourType] == None 
                    or self.armour[discardCard.armourType].power < discardCard.power):
                    self.hand.pop(index)
                    self.armour[discardCard.armourType] = discardCard
                
                elif self.armour[discardCard.armourType].power >= discardCard.power:
                    self.hand.pop(index)

            elif (isinstance(discardCard, Monster)):
                if discardCard.power >= self.calcBattlePower():
                    self.hand.pop(index)
                else:
                    index +=1

            elif index == len(self.hand) - 1 :
                while len(self.hand) > 5:
                    self.hand.pop()

            else:
                index += 1

    def calcBattlePower(self):
        handPower = 0
        for card in self.hand:
            if isinstance(card, Armour):
                handPower += card.power
        lvlpower = 0
        classpower = 0
        if self.race != None:
            lvlpower = self.race.power
        if self.playerClass != None:
            classpower = self.playerClass.power
        return handPower + self.level + lvlpower + classpower

    def fightOwnMonster(self):
        for cardIndex in range(len(self.hand)):
            if isinstance(self.hand[cardIndex], Monster):
                if (self.calcBattlePower() > self.hand[cardIndex].power):
                    return cardIndex
        return None

    def attack(self, monsterCard, otherPlayer, cardsInPlay, playerList):
        cardsToAdd = []
        index = 0
        playedCardsPower = 0
        for card in cardsInPlay:
            playedCardsPower += card.power

        totalCardsAgro = 0
        for player in playerList:
            if isinstance(player[0], AgroRobo) or isinstance(player[0], Player) or isinstance(player[0], OptimalRobo):
                totalCardsAgro += len(player[0].hand)

        while index < len(self.hand):
            card = self.hand[index]
            if ((isinstance(card, Consumable) or isinstance(card, Curse)) and 
                (monsterCard.power >= otherPlayer.calcBattlePower() + card.power + playedCardsPower) and 
                (monsterCard.power < otherPlayer.calcBattlePower() + playedCardsPower)):
                cardsToAdd += [card]
                self.hand.pop(index)
                break

            elif ((isinstance(card, Consumable) or isinstance(card, Curse)) and 
                  (monsterCard.power < otherPlayer.calcBattlePower() + card.power + playedCardsPower) and 
                  (monsterCard.power < otherPlayer.calcBattlePower() + playedCardsPower)):
                if totalCardsAgro >  8:
                    cardsToAdd += [card]
                    self.hand.pop(index)
                    break
            else:
                index += 1
        return cardsToAdd

    def fightMonster(self, monster):
        itemsToUse = []
        levelDifference = monster.power - self.calcBattlePower()
        if levelDifference < 0:
            return itemsToUse
        else:
            for usableCard in self.hand:
                if (isinstance(usableCard, Curse) or isinstance(usableCard, Consumable) 
                    and usableCard.power > 0):
                    levelDifference -= usableCard.power
                    itemsToUse.append(usableCard)
                    if levelDifference < 0:
                        return itemsToUse
            if levelDifference < 0:
                return itemsToUse
            else:
                return []

class StupidRobot(object):
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
    
    def discardApplyCards(self):
        while len(self.hand) > 5:
            self.hand.pop()
    
    def fightMonster(self, monster):
        return []
    
    def applyArmour(self, armourCard, index):
        for armourSpot in self.armour:
            if armourCard.armourType == armourSpot and self.armour[armourSpot] == None:
                self.hand.pop(index)
                self.armour[armourSpot] = armourCard

    def calcBattlePower(self):
        handPower = 0
        for card in self.hand:
            if isinstance(card, Armour):
                handPower += card.power
        lvlpower = 0
        classpower = 0
        if self.race != None:
            lvlpower = self.race.power
        if self.playerClass != None:
            classpower = self.playerClass.power
        return handPower + self.level + lvlpower + classpower
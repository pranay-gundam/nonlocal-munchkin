#############################################
# Author: Pranay Gundam
#############################################

# This file contains the main code to run the game

import pygame
from pygame import mixer
from Cards import *
from DrawingScreens import *
from Deck import *
from Players import *
from GameAI import *

# The base code structure for this class is from 
# https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py,
# although I have added a lot of additional specifications that are specific to 
# my term project

class PygameGame(object):

    def init(self):
        pass

    def mousePressed(self, x, y, screen):
        if self.isHomeScreen:
            w = self.width
            h = self.height
            
            '''
            oneTwoPlayBoundsX = (x >= w/4 - 10) and (x <= w/2 - 10)
            oneThreePlayBoundsY = (y >= 3*h/4 - 60) and (y <= 3*h/4 - 10)
            threeFourPlayBoundsX = (x >= w/2 + 10) and (x <= 3*w/4 + 10)
            twoFourPlayBoundsY = (y >= 3*h/4 + 10) and (y <= 3*h/4 + 60)
            '''
            
            inRulesX = (x >= w/4 - 10) and (x <= w/2 - 10)
            inRulesY = (y >= 3*h/4 - 130) and (y <= 3*h/4 - 80)
            inSettingsX = (x >= w/2 + 10) and (x <= 3*w/4 + 10)
            inSettingsY = (y >= 3*h/4 - 130) and (y <= 3*h/4 - 80)
            inPlayButtonX = (x >= 3*w/8) and (x <= 5*w/8)
            inPlayButtonY = (y >= 3*h/4 - 55) and (y <= 3*h/4 - 5)

            if inRulesX and inRulesY:
                self.isHomeScreen = False
                self.isDrawRules = True
        
            if inSettingsX and inSettingsY:
                self.isHomeScreen = False
                self.isDrawSettings = True

            if inPlayButtonX and inPlayButtonY:
                self.playScreen = True
                self.isHomeScreen = False

            '''
            if oneTwoPlayBoundsX and oneThreePlayBoundsY:
                self.isHomeScreen = False
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                self.gameTreasureDeck = TreasureDeck()
                self.gameDoorDeck = DoorDeck()
                self.playerList = [[Player('Jimbob1', self.gameTreasureDeck, self.gameDoorDeck), True, True]]
            
            if oneTwoPlayBoundsX and twoFourPlayBoundsY:
                self.isHomeScreen = False
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                self.gameTreasureDeck = TreasureDeck()
                self.gameDoorDeck = DoorDeck()
                self.playerList = [[Player('Jimbob1', self.gameTreasureDeck, self.gameDoorDeck), True, True],
                                   [Player('Jimbob2', self.gameTreasureDeck, self.gameDoorDeck), False, False]]

            if threeFourPlayBoundsX and oneThreePlayBoundsY:
                self.isHomeScreen = False
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                self.gameTreasureDeck = TreasureDeck()
                self.gameDoorDeck = DoorDeck()
                self.playerList = [[Player('Jimbob1', self.gameTreasureDeck, self.gameDoorDeck), True, True],
                                   [Player('Jimbob2', self.gameTreasureDeck, self.gameDoorDeck), False, False],
                                   [Player('Jimbob3', self.gameTreasureDeck, self.gameDoorDeck), False, False]]

            if threeFourPlayBoundsX and twoFourPlayBoundsY:
                self.isHomeScreen = False
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                self.gameTreasureDeck = TreasureDeck()
                self.gameDoorDeck = DoorDeck()
                self.playerList = [[Player('Jimbob1', self.gameTreasureDeck, self.gameDoorDeck), True, True],
                                   [Player('Jimbob2', self.gameTreasureDeck, self.gameDoorDeck), False, False],
                                   [Player('Jimbob3', self.gameTreasureDeck, self.gameDoorDeck), False, False],
                                   [Player('Jimbob4', self.gameTreasureDeck, self.gameDoorDeck), False, False]]
            '''
        elif self.isDrawRules:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            
            if inBackButtonX and inBackButtonY:
                self.isDrawRules = False
                self.isHomeScreen = True
        
        elif self.isDrawSettings:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            
            if inBackButtonX and inBackButtonY:
                self.isDrawSettings = False
                self.isHomeScreen = True
        
        elif self.playScreen:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            inHuman0X = (x>=160) and (x<=180)
            inHuman0Y = (y>=self.height/2 - 30) and (y<=self.height/2 - 10)
            inHuman1X = (x>=200) and (x<=220)
            inHuman1Y = (y>=self.height/2 - 30) and (y<=self.height/2 - 10)
            inHuman2X = (x>=240) and (x<=260)
            inHuman2Y = (y>=self.height/2 - 30) and (y<=self.height/2 - 10)
            inHuman3X = (x>=280) and (x<=300)
            inHuman3Y = (y>=self.height/2 - 30) and (y<=self.height/2 - 10)
            inComputer0X = (x>=185) and (x<=205)
            inComputer0Y = (y>=self.height/2 + 20) and (y<=self.height/2 + 40)
            inComputer1X = (x>=225) and (x<=245)
            inComputer1Y = (y>=self.height/2 + 20) and (y<=self.height/2 + 40)
            inComputer2X = (x>=265) and (x<=285)
            inComputer2Y = (y>=self.height/2 + 20) and (y<=self.height/2 + 40)
            inComputer3X = (x>=305) and (x<=325)
            inComputer3Y = (y>=self.height/2 + 20) and (y<=self.height/2 + 40)
            inStartGameX = (x>=3*self.width/8) and (x<=5*self.width/8)
            inStartGameY = (y>=self.height - 100) and (y<=self.height - 50)


            if inBackButtonX and inBackButtonY:
                self.playScreen = False
                self.isHomeScreen = True

            if inHuman0X and inHuman0Y:
                if self.howManyHuman == 0:
                    self.howManyHuman = None
                else:
                    self.howManyHuman = 0
            elif inHuman1X and inHuman1Y:
                if self.howManyHuman == 1:
                    self.howManyHuman = None
                else:
                    self.howManyHuman = 1
            elif inHuman2X and inHuman2Y:
                if self.howManyHuman == 2:
                    self.howManyHuman = None
                else:
                    self.howManyHuman = 2
            elif inHuman3X and inHuman3Y:
                if self.howManyHuman == 3:
                    self.howManyHuman = None
                else:
                    self.howManyHuman = 3
            
            if inComputer0X and inComputer0Y:
                if self.howManyComputer == 0:
                    self.howManyComputer = None
                else:
                    self.howManyComputer = 0
            elif inComputer1X and inComputer1Y:
                if self.howManyComputer == 1:
                    self.howManyComputer = None
                else:
                    self.howManyComputer = 1
            elif inComputer2X and inComputer2Y:
                if self.howManyComputer == 2:
                    self.howManyComputer = None
                else:
                    self.howManyComputer = 2
            elif inComputer3X and inComputer3Y:
                if self.howManyComputer == 3:
                    self.howManyComputer = None
                else:
                    self.howManyComputer = 3

            if (inStartGameX and inStartGameY and 
                (self.howManyComputer != None and self.howManyHuman != None)):                
                self.isNameScreen = True
                self.playScreen = False

                '''
                self.gameTreasureDeck = TreasureDeck()
                self.gameDoorDeck = DoorDeck()
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                self.playScreen = False
                for num in range(self.howManyHuman):
                    if num == 0:
                        self.playerList.append([Player(f'Hooman{num+1}', self.gameTreasureDeck, self.gameDoorDeck), True, True])
                    else:
                        self.playerList.append([Player(f'Hooman{num+1}', self.gameTreasureDeck, self.gameDoorDeck), False, False])
                
                for num in range(self.howManyComputer):
                    if num == 0 and self.howManyHuman == 0:
                        self.playerList.append([PassiveRobot(f'Robot{num+1}', self.gameTreasureDeck, self.gameDoorDeck), True, True])
                    else:
                        self.playerList.append([PassiveRobot(f'Robot{num+1}', self.gameTreasureDeck, self.gameDoorDeck), False, False])
                '''
        elif self.isNameScreen:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)

            inStartGameX = (x>=3*self.width/8) and (x<=5*self.width/8)
            inStartGameY = (y>=self.height - 100) and (y<=self.height - 50)

            inHuman1X = (x>=180) and (x<=180+325)
            inHuman1Y = (y>=120) and (y<=150)
            inHuman2X = (x>=180) and (x<=180+325)
            inHuman2Y = (y>=170) and (y<=200)
            inHuman3X = (x>=180) and (x<=180+325)
            inHuman3Y = (y>=220) and (y<=250)
            
            inComp1X = (x>=200) and (x<=500)
            inComp1Y = (y>=self.height/2-5) and (y<=self.height/2+25)
            inComp2X = (x>=200) and (x<=500)
            inComp2Y = (y>=self.height/2-5 + 70) and (y<=self.height/2+25 + 70)
            inComp3X = (x>=200) and (x<=500)
            inComp3Y = (y>=self.height/2-5 + 140) and (y<=self.height/2+25 + 140)

            inComp1D1X = (x>=30) and (x<=50)
            inComp1D1Y = (y>=self.height/2 + 30) and (y<=self.height/2 + 50)
            inComp2D1X = (x>=30) and (x<=50)
            inComp2D1Y = (y>=self.height/2 + 100) and (y<=self.height/2 + 120)
            inComp3D1X = (x>=30) and (x<=50)
            inComp3D1Y = (y>=self.height/2 + 170) and (y<=self.height/2 + 190)
            inComp4D1X = (x>=30) and (x<=50)
            inComp4D1Y = (y>=self.height/2 + 240) and (y<=self.height/2 + 260)

            inComp1D2X = (x>=70) and (x<=90)
            inComp1D2Y = (y>=self.height/2 + 30) and (y<=self.height/2 + 50)
            inComp2D2X = (x>=70) and (x<=90)
            inComp2D2Y = (y>=self.height/2 + 100) and (y<=self.height/2 + 120)
            inComp3D2X = (x>=70) and (x<=90)
            inComp3D2Y = (y>=self.height/2 + 170) and (y<=self.height/2 + 190)
            inComp4D2X = (x>=70) and (x<=90)
            inComp4D2Y = (y>=self.height/2 + 240) and (y<=self.height/2 + 260)

            inComp1D3X = (x>=110) and (x<=130)
            inComp1D3Y = (y>=self.height/2 + 30) and (y<=self.height/2 + 50)
            inComp2D3X = (x>=110) and (x<=130)
            inComp2D3Y = (y>=self.height/2 + 100) and (y<=self.height/2 + 120)
            inComp3D3X = (x>=110) and (x<=130)
            inComp3D3Y = (y>=self.height/2 + 170) and (y<=self.height/2 + 190)
            inComp4D3X = (x>=110) and (x<=130)
            inComp4D3Y = (y>=self.height/2 + 240) and (y<=self.height/2 + 260)

            inComp1D4X = (x>=150) and (x<=170)
            inComp1D4Y = (y>=self.height/2 + 30) and (y<=self.height/2 + 50)
            inComp2D4X = (x>=150) and (x<=170)
            inComp2D4Y = (y>=self.height/2 + 100) and (y<=self.height/2 + 120)
            inComp3D4X = (x>=150) and (x<=170)
            inComp3D4Y = (y>=self.height/2 + 170) and (y<=self.height/2 + 190)
            inComp4D4X = (x>=150) and (x<=170)
            inComp4D4Y = (y>=self.height/2 + 240) and (y<=self.height/2 + 260)

            if inHuman1X and inHuman1Y:
                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = False

                self.isHumanName1 = True
                self.isHumanName2 = False
                self.isHumanName3 = False

            elif inHuman2X and inHuman2Y:
                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = False

                self.isHumanName1 = False
                self.isHumanName2 = True
                self.isHumanName3 = False

            elif inHuman3X and inHuman3Y:
                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = False

                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = True

            elif (not inHuman1X and not inHuman1Y) and (not inHuman2X and not inHuman2Y) and (not inHuman3X and not inHuman3Y):
                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = False

                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = False

            if inComp1X and inComp1Y:
                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = False

                self.isCompName1 = True
                self.isCompName2 = False
                self.isCompName3 = False

            elif inComp2X and inComp2Y:
                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = False

                self.isCompName1 = False
                self.isCompName2 = True
                self.isCompName3 = False

            elif inComp3X and inComp3Y:
                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = False

                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = True

            elif (not inComp1X and not inComp1Y) and (not inComp2X and not inComp2Y) and (not inComp3X and not inComp3Y):
                self.isHumanName1 = False
                self.isHumanName2 = False
                self.isHumanName3 = False

                self.isCompName1 = False
                self.isCompName2 = False
                self.isCompName3 = False

            if inComp1D1X and inComp1D1Y:
                if self.comp1Diff == 0:
                    self.comp1Diff = None
                else:
                    self.comp1Diff = 0
                

            elif inComp1D2X and inComp1D2Y:
                if self.comp1Diff == 1:
                    self.comp1Diff = None
                else:
                    self.comp1Diff = 1
                
            elif inComp1D3X and inComp1D3Y:
                if self.comp1Diff == 2:
                    self.comp1Diff = None
                else:
                    self.comp1Diff = 2

            elif inComp1D4X and inComp1D4Y:
                if self.comp1Diff == 3:
                    self.comp1Diff = None
                else:
                    self.comp1Diff = 3
    
            if inComp2D1X and inComp2D1Y:
                if self.comp2Diff == 0:
                    self.comp2Diff = None
                else:
                    self.comp2Diff = 0

            elif inComp2D2X and inComp2D2Y:
                if self.comp2Diff == 1:
                    self.comp2Diff = None
                else:
                    self.comp2Diff = 1

            elif inComp2D3X and inComp2D3Y:
                if self.comp2Diff == 2:
                    self.comp2Diff = None
                else:
                    self.comp2Diff = 2

            elif inComp2D4X and inComp2D4Y:
                if self.comp2Diff == 3:
                    self.comp2Diff = None
                else:
                    self.comp2Diff = 3

            if inComp3D1X and inComp3D1Y:
                if self.comp3Diff == 0:
                    self.comp3Diff = None
                else:
                    self.comp3Diff = 0

            elif inComp3D2X and inComp3D2Y:
                if self.comp3Diff == 1:
                    self.comp3Diff = None
                else:
                    self.comp3Diff = 1
            
            elif inComp3D3X and inComp3D3Y:
                if self.comp3Diff == 2:
                    self.comp3Diff = None
                else:
                    self.comp3Diff = 2
        
            elif inComp3D4X and inComp3D4Y:
                if self.comp3Diff == 3:
                    self.comp3Diff = None
                else:
                    self.comp3Diff = 3

            if inBackButtonX and inBackButtonY:
                self.playScreen = True
                self.isNameScreen = False
            
            if inStartGameX and inStartGameY:
                self.gameDoorDeck = DoorDeck()
                self.gameTreasureDeck = TreasureDeck()
                self.isNameScreen = False
                self.playScreen = False
                self.isHomeScreen = False
                
                # music is from https://www.youtube.com/watch?v=57eu6krzkKo
                pygame.mixer.music.load('boombap.wav')
                pygame.mixer.music.play(-1)
                for count in range(self.howManyHuman):
                    if count == 0:
                        self.playerList.append([Player(''.join(self.humanName1), self.gameTreasureDeck, self.gameDoorDeck), True, True])
                    elif count == 1:
                        self.playerList.append([Player(''.join(self.humanName2), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                    elif count == 2:
                        self.playerList.append([Player(''.join(self.humanName3), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                for count in range(self.howManyComputer):
                    if count == 0 and self.howManyHuman == 0:
                        if self.comp1Diff == 0:
                            self.playerList.append([StupidRobot(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), True, True])
                        elif self.comp1Diff == 1:
                            self.playerList.append([PassiveRobot(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), True, True])
                        elif self.comp1Diff == 2:
                            self.playerList.append([AgroRobo(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), True, True])
                        elif self.comp1Diff == 3:
                            self.playerList.append([OptimalRobo(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), True, True])
                    elif count == 0:
                        if self.comp1Diff == 0:
                            self.playerList.append([StupidRobot(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp1Diff == 1:
                            self.playerList.append([PassiveRobot(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp1Diff == 2:
                            self.playerList.append([AgroRobo(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp1Diff == 3:
                            self.playerList.append([OptimalRobo(''.join(self.compName1), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                    elif count == 1:
                        if self.comp2Diff == 0:
                            self.playerList.append([StupidRobot(''.join(self.compName2), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp2Diff == 1:
                            self.playerList.append([PassiveRobot(''.join(self.compName2), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp2Diff == 2:
                            self.playerList.append([AgroRobo(''.join(self.compName2), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp2Diff == 3:
                            self.playerList.append([OptimalRobo(''.join(self.compName2), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                    elif count == 2:
                        if self.comp3Diff == 0:
                            self.playerList.append([StupidRobot(''.join(self.compName3), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp3Diff == 1:
                            self.playerList.append([PassiveRobot(''.join(self.compName3), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp3Diff == 2:
                            self.playerList.append([AgroRobo(''.join(self.compName3), self.gameTreasureDeck, self.gameDoorDeck), False, False])
                        elif self.comp3Diff == 3:
                            self.playerList.append([OptimalRobo(''.join(self.compName3), self.gameTreasureDeck, self.gameDoorDeck), False, False])
        else:
            # the next couple of boolean values contain information about whether
            # or not the location where the mouse was clicked should trigger a 
            # response
            numCards = len(self.currentPlayer.hand)
            inHandCardsX = (x >= self.width/4) and (x<=self.width/4 + 20*numCards)
            inHandCardsY = (y >= 3*self.height/4 + 10)
            inSwitchPlayerX = (x>=14*self.width/18 + 60) and (x<= 14*self.width/18 + 110)
            inSwitchPlayerY = (y>=14*self.height/18) and (y<=14*self.height/18 + 50)
            inDiscardCardX = (x>=14*self.width/18) and (x<=14*self.width/18 + 50)
            inDiscardCardY = (y>=14*self.height/18 + 60) and (y<=14*self.height/18 + 110)
            inDoorCardsX = (x>=14*self.width/18) and (x<=14*self.width/18+50)   
            inDoorCardsY = (y>=14*self.height/18) and (y<= 14*self.height/18+50)
            inBeatBattleX = (x>=14*self.width/18 + 120) and (x<=14*self.width/18 + 170)
            inBeatBattleY = (y>=14*self.height/18) and (y<=14*self.height/18 + 50)
            inUseCardX = (x>=14*self.width/18 + 120) and (x<=14*self.width/18 + 170)
            inUseCardY = (y>=14*self.height/18 + 60) and (y<=14*self.height/18 + 110)
            inNextTurnX = (x>=14*self.width/18 + 60) and (x<=14*self.width/18 + 110)
            inNextTurnY = (y>=14*self.height/18 + 60) and (y<=14*self.height/18 + 110)

            allBelowFive = True
            for player in self.playerList:
                if len(player[0].hand) > 5:
                    allBelowFive = False

            # Changes the useCardMode based on whether or not the button was clicked.
            # This also turns off discard mode.
            if inUseCardX and inUseCardY:
                self.useCardMode = not self.useCardMode
                self.isDiscardPhase = False

            # Changes the discardMode based on whether or not the button was clicked.
            # This also turns off useCardMode.
            if inDiscardCardX and inDiscardCardY:
                self.isDiscardPhase = not self.isDiscardPhase
                self.useCardMode = False
    
            # if a card in a player's hand was clicked and we are in useCardMode
            # then we use the card based on the type of card it is
            if self.useCardMode and inHandCardsX and inHandCardsY:
                self.isDiscardPhase = False
                cardIndex = int((x - self.width/4)//20)
                playCard = self.currentPlayer.hand[cardIndex]
                
                # Apply a consumable to the playing field when a player is in battle
                if (isinstance(playCard, Consumable) and (self.cardOnSpot != None) and self.isBattlePhase):
                    self.currentPlayer.hand.pop(cardIndex)
                    numCards = len(self.currentPlayer.hand)
                    if numCards == 0:
                        self.onHandCards = (False, None)
                    elif cardIndex >= numCards:
                        cardIndex = numCards - 1
                        self.onHandCards = (True, self.currentPlayer.hand[cardIndex])
                    self.cardsInPlay.append(playCard)
                
                # Apply a curse to the current player whenever
                elif isinstance(playCard, Curse) and (self.cardOnSpot != None):
                    self.currentPlayer.hand.pop(cardIndex)
                    numCards = len(self.currentPlayer.hand)
                    if numCards == 0:
                        self.onHandCards = (False, None)
                    elif cardIndex >= numCards:
                        cardIndex = numCards - 1
                        self.onHandCards = (True, self.currentPlayer.hand[cardIndex])
                    self.cardOnSpot.power -= playCard.power
                    self.cardsInPlay.append(playCard)
                
                # Equip armour when a player is not in battle
                elif isinstance(playCard, Armour) and not self.isBattlePhase:
                    self.currentPlayer.hand.pop(cardIndex)
                    previousArmour = self.currentPlayer.applyArmour(playCard)
                    if previousArmour != None:
                        self.currentPlayer.hand.append(previousArmour)
            
                # If we are in the second door phase and we want to fight against
                # our own monster
                elif (isinstance(playCard, Monster) and not self.canKickDoor[0] and
                      self.canKickDoor[1] and (self.currentPlayer == self.currentPlayerTurn)):
                    self.cardOnSpot = playCard
                    self.isBattlePhase = True
                    self.canKickDoor[1] = False
                    self.currentPlayer.hand.pop(cardIndex)
                
                # If the card is a Race card, then equip it
                elif (isinstance(playCard, Race) and not self.isBattlePhase):
                    self.currentPlayer.hand.pop(cardIndex)
                    if self.currentPlayer.race != None:
                        self.currentPlayer.hand.append(self.currentPlayer.race)
                    self.currentPlayer.race = playCard
                    
                # If the card is a class card, then equip it
                elif (isinstance(playCard, PlayerClass) and not self.isBattlePhase):
                    self.currentPlayer.hand.pop(cardIndex)
                    if self.currentPlayer.playerClass != None:
                        self.currentPlayer.hand.append(self.currentPlayer.playerClass)
                    self.currentPlayer.playerClass = playCard

            playedCardsPower = 0
            for card in self.cardsInPlay:
                playedCardsPower += card.power

            # If you click fight monster and you can beat the monster, then reap
            # the rewards
            if (inBeatBattleX and inBeatBattleY and self.isBattlePhase and 
               (self.currentPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power)):
                self.isBattlePhase = False
                self.currentPlayerTurn.level += 1
                self.cardsInPlay = []
                for num in range(self.cardOnSpot.reward):
                    if len(self.gameDoorDeck.cards) == 0:
                        self.gameDoorDeck = DoorDeck()
                    if len(self.gameTreasureDeck.cards) == 0:
                        self.gameTreasureDeck = TreasureDeck()

                    self.currentPlayer.hand.append(self.gameTreasureDeck.cards.pop())
            
            # If you click fight monster and you can beat the monster, then suffer
            # the consequences
            elif (inBeatBattleX and inBeatBattleY and self.isBattlePhase and 
                 (self.currentPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power)):
                self.isBattlePhase = False
                self.currentPlayerTurn.level = 1
                self.currentPlayerTurn.hand = []
                self.currentPlayer.playerClass = None
                self.currentPlayer.race = None
                self.currentPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                for num in range(4):
                    self.currentPlayerTurn.hand.append(self.gameDoorDeck.cards.pop())
                    self.currentPlayerTurn.hand.append(self.gameTreasureDeck.cards.pop())
            
            # if we are in discard mode and we click on a card, then remove it
            # from the players hand
            if self.isDiscardPhase and inHandCardsX and inHandCardsY:
                cardIndex = int((x - self.width/4)//20)
                self.currentPlayer.hand.pop(cardIndex)
                numCards = len(self.currentPlayer.hand)
                if numCards == 0:
                    self.onHandCards = (False, None)
                elif cardIndex >= numCards:
                    cardIndex = numCards - 1
                    self.onHandCards = (True, self.currentPlayer.hand[cardIndex])
            
            # if a player can kick down the door and clicks the button, then 
            # kick open the door (note that what happens to the door card is 
            # determined by if it was the first or second time the a player has
            # drawn a door card).
            if (self.canKickDoor[1] and inDoorCardsX and inDoorCardsY and 
               (self.currentPlayerTurn == self.currentPlayer) and 
               (len(self.currentPlayer.hand) <= 5) and allBelowFive):
                if not self.canKickDoor[0]:
                    self.canKickDoor[1] = False
                if self.isDiscardPhase:
                    self.isDiscardPhase = False
                doorCard = self.gameDoorDeck.cards.pop()
                if isinstance(doorCard, Monster) and self.canKickDoor[0]:
                    self.cardOnSpot = doorCard
                    self.isBattlePhase = True
                    self.canKickDoor[1] = False
                else:
                    self.canKickDoor[0] = False
                    self.currentPlayer.hand.append(doorCard) 
            
            # If you click the switch player button then switch the display for
            # the player.
            if inSwitchPlayerX and inSwitchPlayerY:
                self.isDiscardPhase = False
                self.useCardMode = False
                for index in range(len(self.playerList)):
                    if self.playerList[index][1] == True:
                        self.playerList[index][1] = False
                        self.playerList[(index+1)%len(self.playerList)][1] = True
                        break
            
            # If all the player have fewer than five cards and we are not in battle
            # and you click the next turn button then move on to the next player's
            # turn.
            if (inNextTurnX and inNextTurnY and not self.isBattlePhase and allBelowFive and 
                not self.canKickDoor[1]):
                self.canKickDoor = [True, True]
                self.isDiscardPhase = False
                self.useCardMode = False
                for index in range(len(self.playerList)):
                    if self.playerList[index][2] == True:
                        self.playerList[index][2] = False
                        self.playerList[index][1] = False
                        self.playerList[(index+1)%len(self.playerList)][2] = True
                        self.playerList[(index+1)%len(self.playerList)][1] = True
                        break

    def mouseReleased(self, x, y):
        pass
    
    # Most of the code in this function is dedicated to displaying cards whenever
    # they are hovered over.
    def mouseMotion(self, x, y):
        if not self.isHomeScreen and not self.isDrawRules and not self.isDrawSettings and not self.playScreen and not self.isNameScreen:
            howManyArmour = 0
            for armour in self.currentPlayer.armour:
                if self.currentPlayer.armour[armour] != None:
                    howManyArmour += 1
            
            numCards = len(self.currentPlayer.hand)
            inHandCardsX = (x >= self.width/4) and (x<=self.width/4 + 20*numCards)
            inHandCardsY = (y >= 3*self.height/4 + 10)
            inCardsPlayedX = (x>=150) and (x<=150 + 20*len(self.cardsInPlay))
            inCardsPlayedY = (y>=20) and (y<=220)
            inArmourX = (x>=5) and (x<=5 + 20*howManyArmour)
            inArmourY = (y>=3*self.height/4 + 10)
            inRaceX = (x>=3*self.width/4 - 100) and (x<=3*self.width/4 - 70)
            inRaceY = (y>=self.height - 20)
            inPlayerClassX = (x>=3*self.width/4 - 70) and (x<=3*self.width/4 - 70 + 126)
            inPlayerClassY = (y>=self.height - 20)

            # If the mouse hovers over the cards in the player's hands
            if inHandCardsX and inHandCardsY:
                cardIndex = int((x - self.width/4)//20)
                if cardIndex >= numCards:
                    cardIndex = numCards - 1
                self.onHandCards = (True, self.currentPlayer.hand[cardIndex])
            
            # if the mouse hovers over the cards that have been played
            elif self.isBattlePhase and inCardsPlayedX and inCardsPlayedY:
                cardIndex = int((x - 150)//20)
                if cardIndex >= numCards:
                    cardIndex = numCards - 1
                self.onHandCards = (True, self.cardsInPlay[cardIndex])
            
            # if the mouse hovers over the armour cards
            elif inArmourX and inArmourY:
                cardIndex = int((x - 5)//20)
                count = 0
                for armourPiece in self.currentPlayer.armour:
                    if self.currentPlayer.armour[armourPiece] != None and count == cardIndex:
                        self.onHandCards = (True, self.currentPlayer.armour[armourPiece])
                        break
                    elif self.currentPlayer.armour[armourPiece] != None:
                        count +=1
            
            # if the mouse hovers over the race card
            elif inRaceX and inRaceY:
                self.onHandCards = (True, self.currentPlayer.race)

            # if the mouse hovers over the class card
            elif inPlayerClassX and inPlayerClassY:
                self.onHandCards = (True, self.currentPlayer.playerClass)

            else:
                self.onHandCards = (False, None)

    def mouseDrag(self, x, y):
        pass

    # basic idea about typing in pygame is from https://gamedev.stackexchange.com/questions/138888/user-input-text-in-pygame
    def keyPressed(self, keyCode, modifier):
        if self.isNameScreen:
            if self.isHumanName1:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.humanName1 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.humanName1 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.humanName1 = self.humanName1[:-1]  
            elif self.isHumanName2:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.humanName2 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.humanName2 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.humanName2 = self.humanName2[:-1]  
            elif self.isHumanName3:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.humanName3 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.humanName3 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.humanName3 = self.humanName3[:-1]  
            
            if self.isCompName1:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.compName1 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.compName1 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.compName1 = self.compName1[:-1]  
            elif self.isCompName2:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.compName2 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.compName2 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.compName2 = self.compName2[:-1]  
            elif self.isCompName3:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.compName3 += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.compName3 += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.compName3 = self.compName3[:-1]  


    def keyReleased(self, keyCode, modifier):
        pass
    

    def timerFired(self, dt):
        if len(self.gameDoorDeck.cards) == 0:
            self.gameDoorDeck = DoorDeck()
        if len(self.gameTreasureDeck.cards) == 0:
            self.gameTreasureDeck = TreasureDeck()
        if (isinstance(self.currentPlayer, PassiveRobot) and not self.isHomeScreen 
            and not self.isDrawRules and not self.isDrawSettings 
            and not self.isNameScreen):
            self.cpuTimer += dt
            if self.cpuTimer > self.interval:
                allBelowFive = True
                for player in self.playerList:
                    if len(player[0].hand) > 5:
                        allBelowFive = False
                
                index = 0
                while index < len(self.currentPlayer.hand):
                    if isinstance(self.currentPlayer.hand[index], Armour):
                        if not self.currentPlayer.applyArmour(self.currentPlayer.hand[index], index):
                            index += 1
                    else:
                        index += 1
                
                if len(self.currentPlayer.hand) > 5:
                    self.currentPlayer.discardApplyCards()

                elif (self.canKickDoor[1] and (self.currentPlayerTurn == self.currentPlayer) and 
                (len(self.currentPlayer.hand) <= 5) and allBelowFive):
                    if not self.canKickDoor[0]:
                        self.canKickDoor[1] = False
                    if self.isDiscardPhase:
                        self.isDiscardPhase = False
                    doorCard = self.gameDoorDeck.cards.pop()
                    if isinstance(doorCard, Monster) and self.canKickDoor[0]:
                        self.cardOnSpot = doorCard
                        self.isBattlePhase = True
                        self.canKickDoor[1] = False
                    else:
                        self.canKickDoor[0] = False
                        self.currentPlayer.hand.append(doorCard) 

                elif not self.canKickDoor[1] and not self.isBattlePhase and allBelowFive:
                    self.canKickDoor = [True, True]
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][2] == True:
                            self.playerList[index][2] = False
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][2] = True
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.isBattlePhase and self.currentPlayer == self.currentPlayerTurn:
                    itemList = self.currentPlayer.fightMonster(self.cardOnSpot)
                    self.cardsInPlay += itemList
                    playedCardsPower = 0
                    for card in self.cardsInPlay:
                        playedCardsPower += card.power

                    # If you click fight monster and you can beat the monster, then reap
                    # the rewards
                    if (self.currentPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level += 1
                        self.cardsInPlay = []
                        for num in range(self.cardOnSpot.reward):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()

                            self.currentPlayer.hand.append(self.gameTreasureDeck.cards.pop())
                    
                    # If you click fight monster and you can beat the monster, then suffer
                    # the consequences
                    elif (self.currentPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level = 1
                        self.currentPlayerTurn.hand = []
                        self.currentPlayer.playerClass = None
                        self.currentPlayer.race = None
                        self.currentPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                        for num in range(4):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()
                            
                            self.currentPlayerTurn.hand.append(self.gameDoorDeck.cards.pop())
                            self.currentPlayerTurn.hand.append(self.gameTreasureDeck.cards.pop())

                elif not allBelowFive:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.currentPlayer != self.currentPlayerTurn:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                self.cpuTimer = 0
        
        elif (isinstance(self.currentPlayer, AgroRobo) and not self.isHomeScreen 
            and not self.isDrawRules and not self.isDrawSettings 
            and not self.isNameScreen):
            self.cpuTimer += dt
            if self.cpuTimer > self.interval:
                allBelowFive = True
                for player in self.playerList:
                    if len(player[0].hand) > 5:
                        allBelowFive = False
                
                index = 0
                while index < len(self.currentPlayer.hand):
                    if isinstance(self.currentPlayer.hand[index], Armour):
                        if not self.currentPlayer.applyArmour(self.currentPlayer.hand[index], index):
                            index += 1
                    else:
                        index += 1
                
                if len(self.currentPlayer.hand) > 5:
                    self.currentPlayer.discardApplyCards()

                elif (self.canKickDoor[1] and (self.currentPlayerTurn == self.currentPlayer) and 
                (len(self.currentPlayer.hand) <= 5) and allBelowFive):
                    if not self.canKickDoor[0]:
                        self.canKickDoor[1] = False
                    if self.isDiscardPhase:
                        self.isDiscardPhase = False
                    doorCard = self.gameDoorDeck.cards.pop()
                    if isinstance(doorCard, Monster) and self.canKickDoor[0]:
                        self.cardOnSpot = doorCard
                        self.isBattlePhase = True
                        self.canKickDoor[1] = False
                    else:
                        self.canKickDoor[0] = False
                        self.currentPlayer.hand.append(doorCard) 

                elif not self.canKickDoor[1] and not self.isBattlePhase and allBelowFive:
                    self.canKickDoor = [True, True]
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][2] == True:
                            self.playerList[index][2] = False
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][2] = True
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.isBattlePhase and self.currentPlayer == self.currentPlayerTurn:
                    itemList = self.currentPlayer.fightMonster(self.cardOnSpot)
                    self.cardsInPlay += itemList
                    playedCardsPower = 0
                    for card in self.cardsInPlay:
                        playedCardsPower += card.power

                    # If you click fight monster and you can beat the monster, then reap
                    # the rewards
                    if (self.currentPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level += 1
                        self.cardsInPlay = []
                        for num in range(self.cardOnSpot.reward):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()
                            self.currentPlayer.hand.append(self.gameTreasureDeck.cards.pop())
                    
                    # If you click fight monster and you can beat the monster, then suffer
                    # the consequences
                    elif (self.currentPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level = 1
                        self.currentPlayerTurn.hand = []
                        self.currentPlayer.playerClass = None
                        self.currentPlayer.race = None
                        self.currentPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                        for num in range(4):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()
                            
                            self.currentPlayerTurn.hand.append(self.gameDoorDeck.cards.pop())
                            self.currentPlayerTurn.hand.append(self.gameTreasureDeck.cards.pop())

                elif not allBelowFive:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.currentPlayer != self.currentPlayerTurn:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                self.cpuTimer = 0
        
        elif (isinstance(self.currentPlayer, StupidRobot) and not self.isHomeScreen 
            and not self.isDrawRules and not self.isDrawSettings 
            and not self.isNameScreen):
            self.cpuTimer += dt
            if self.cpuTimer > self.interval:
                allBelowFive = True
                for player in self.playerList:
                    if len(player[0].hand) > 5:
                        allBelowFive = False
                
                index = 0
                while index < len(self.currentPlayer.hand):
                    if isinstance(self.currentPlayer.hand[index], Armour):
                        if not self.currentPlayer.applyArmour(self.currentPlayer.hand[index], index):
                            index += 1
                    else:
                        index += 1
                
                if len(self.currentPlayer.hand) > 5:
                    self.currentPlayer.discardApplyCards()

                elif (self.canKickDoor[1] and (self.currentPlayerTurn == self.currentPlayer) and 
                (len(self.currentPlayer.hand) <= 5) and allBelowFive):
                    if not self.canKickDoor[0]:
                        self.canKickDoor[1] = False
                    if self.isDiscardPhase:
                        self.isDiscardPhase = False
                    doorCard = self.gameDoorDeck.cards.pop()
                    if isinstance(doorCard, Monster) and self.canKickDoor[0]:
                        self.cardOnSpot = doorCard
                        self.isBattlePhase = True
                        self.canKickDoor[1] = False
                    else:
                        self.canKickDoor[0] = False
                        self.currentPlayer.hand.append(doorCard) 

                elif not self.canKickDoor[1] and not self.isBattlePhase and allBelowFive:
                    self.canKickDoor = [True, True]
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][2] == True:
                            self.playerList[index][2] = False
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][2] = True
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.isBattlePhase and self.currentPlayer == self.currentPlayerTurn:
                    itemList = self.currentPlayer.fightMonster(self.cardOnSpot)
                    self.cardsInPlay += itemList
                    playedCardsPower = 0
                    for card in self.cardsInPlay:
                        playedCardsPower += card.power

                    # If you click fight monster and you can beat the monster, then reap
                    # the rewards
                    if (self.currentPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level += 1
                        self.cardsInPlay = []
                        for num in range(self.cardOnSpot.reward):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()

                            self.currentPlayer.hand.append(self.gameTreasureDeck.cards.pop())
                    
                    # If you click fight monster and you can beat the monster, then suffer
                    # the consequences
                    elif (self.currentPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level = 1
                        self.currentPlayerTurn.hand = []
                        self.currentPlayer.playerClass = None
                        self.currentPlayer.race = None
                        self.currentPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                        for num in range(4):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()
                            
                            self.currentPlayerTurn.hand.append(self.gameDoorDeck.cards.pop())
                            self.currentPlayerTurn.hand.append(self.gameTreasureDeck.cards.pop())

                elif not allBelowFive:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.currentPlayer != self.currentPlayerTurn:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                self.cpuTimer = 0

        elif (isinstance(self.currentPlayer, OptimalRobo) and not self.isHomeScreen 
              and not self.isDrawRules and not self.isDrawSettings 
              and not self.isNameScreen):
            self.cpuTimer += dt
            if self.cpuTimer > self.interval:
                allBelowFive = True
                for player in self.playerList:
                    if len(player[0].hand) > 5:
                        allBelowFive = False
                
                index = 0
                while index < len(self.currentPlayer.hand):
                    if isinstance(self.currentPlayer.hand[index], Armour):
                        if not self.currentPlayer.applyArmour(self.currentPlayer.hand[index], index):
                            index += 1
                    else:
                        index += 1
                
                if len(self.currentPlayer.hand) > 5:
                    self.currentPlayer.discardApplyCards()

                elif (self.canKickDoor[1] and (self.currentPlayerTurn == self.currentPlayer) and 
                      (len(self.currentPlayer.hand) <= 5) and allBelowFive):
                    monsterCardIndex = self.currentPlayer.fightOwnMonster()
                    if self.isDiscardPhase:
                        self.isDiscardPhase = False
                    
                    if self.canKickDoor[0]:
                        doorCard = self.gameDoorDeck.cards.pop()
                        if isinstance(doorCard, Monster):
                            self.cardOnSpot = doorCard
                            self.isBattlePhase = True
                            self.canKickDoor[1] = False
                        else:
                            self.canKickDoor[0] = False
                            self.currentPlayer.hand.append(doorCard) 
                    
                    elif not self.canKickDoor[0] and monsterCardIndex == None:
                        self.canKickDoor[1] = False       
                        doorCard = self.gameDoorDeck.cards.pop()
                        self.canKickDoor[0] = False
                        self.currentPlayer.hand.append(doorCard) 

                    elif not self.canKickDoor[0]:
                        self.cardOnSpot = self.currentPlayer.hand[monsterCardIndex]
                        self.currentPlayer.hand.pop(monsterCardIndex)
                        self.isBattlePhase = True
                        self.canKickDoor[1] = False

                elif not self.canKickDoor[1] and not self.isBattlePhase and allBelowFive:
                    self.canKickDoor = [True, True]
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][2] == True:
                            self.playerList[index][2] = False
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][2] = True
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.isBattlePhase and self.currentPlayer == self.currentPlayerTurn:
                    itemList = self.currentPlayer.fightMonster(self.cardOnSpot)
                    self.cardsInPlay += itemList
                    playedCardsPower = 0
                    for card in self.cardsInPlay:
                        playedCardsPower += card.power

                    # If you click fight monster and you can beat the monster, then reap
                    # the rewards
                    if (self.currentPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level += 1
                        self.cardsInPlay = []
                        for num in range(self.cardOnSpot.reward):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()

                            self.currentPlayer.hand.append(self.gameTreasureDeck.cards.pop())
                    
                    # If you click fight monster and you can beat the monster, then suffer
                    # the consequences
                    elif (self.currentPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power):
                        self.isBattlePhase = False
                        self.currentPlayerTurn.level = 1
                        self.currentPlayerTurn.hand = []
                        self.currentPlayer.playerClass = None
                        self.currentPlayer.race = None
                        self.currentPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                        for num in range(4):
                            if len(self.gameDoorDeck.cards) == 0:
                                self.gameDoorDeck = DoorDeck()
                            if len(self.gameTreasureDeck.cards) == 0:
                                self.gameTreasureDeck = TreasureDeck()
                            self.currentPlayerTurn.hand.append(self.gameDoorDeck.cards.pop())
                            self.currentPlayerTurn.hand.append(self.gameTreasureDeck.cards.pop())

                elif not allBelowFive:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                
                elif self.currentPlayer != self.currentPlayerTurn:
                    self.isDiscardPhase = False
                    self.useCardMode = False
                    for index in range(len(self.playerList)):
                        if self.playerList[index][1] == True:
                            self.playerList[index][1] = False
                            self.playerList[(index+1)%len(self.playerList)][1] = True
                            break
                self.cpuTimer = 0

        elif not self.isHomeScreen and not self.isDrawRules and not self.isDrawSettings and not self.isNameScreen and not self.playScreen:
            self.cpuTimer = 0

    def redrawAll(self, screen, time):
        if self.isHomeScreen:
            drawHomeScreen(screen, self.width, self.height)
        elif self.isDrawRules:
            drawRulesScreen(screen, self.width, self.height)
        elif self.isDrawSettings:
            drawSettingsScreen(screen, self.width, self.height)
        elif self.playScreen:
            drawPlayScreen(screen, self.width, self.height, self.howManyHuman, self.howManyComputer)
        elif self.isBattlePhase:
            drawBattleCards(screen, self.width, self.height, 
                            self.cardOnSpot, time, self.isDiscardPhase, 
                            self.currentPlayer, self.useCardMode, self.cardsInPlay,
                            self.currentPlayerTurn, self.currentPlayer.race, 
                            self.currentPlayer.playerClass, self.cpuTimer, self.interval)
            if self.onHandCards[0]:
                drawCards(screen, self.width - 300, 10, self.onHandCards[1])
        elif self.isWin[0]:
            drawWinScreen(screen, self.width, self.height, self.currentPlayer, self.isWin[1])
        elif self.isNameScreen:
            drawNameScreen(screen, self.width, self.height, self.howManyHuman, 
                           self.howManyComputer, self.comp1Diff, self.comp2Diff,
                           self.comp3Diff, self.humanName1, self.humanName2,
                           self.humanName3, self.compName1, self.compName2,
                           self.compName3)
        else:
            drawGameScreen(screen, self.width, self.height, time, self.currentPlayer,
                           self.isDiscardPhase, self.currentPlayerTurn, 
                           self.useCardMode, self.currentPlayer.race, 
                            self.currentPlayer.playerClass, self.cpuTimer, self.interval)
            if self.onHandCards[0]:
                drawCards(screen, self.width - 300, 10, self.onHandCards[1])  
            
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1000, height=600, fps=50, title='112 Pygame Game'):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColorHome = (144,204,245)
        self.bgColorGame = (255,229,204)
        self.isHomeScreen = True
        self.isDoorPhase = False
        self.isBattlePhase = False
        self.isDiscardPhase = False
        self.playerList = []
        self.gameDoorDeck = DoorDeck()
        self.gameTreasureDeck = TreasureDeck()
        self.onHandCards = (False, None)
        self.currentPlayer = None
        self.currentPlayerTurn = None
        self.cardOnSpot = None
        self.useCardMode = False
        self.cardsInPlay = list()
        self.isWin = (False, None)
        self.canKickDoor = [True, True]
        self.isDrawRules = False
        self.isDrawSettings = False
        self.playScreen = False
        self.howManyHuman = None
        self.howManyComputer = None
        self.cpuTimer = 0
        self.isNameScreen = False
        self.isHumanName1 = False
        self.humanName1 = []
        self.isHumanName2 = False
        self.humanName2 = []
        self.isHumanName3 = False
        self.humanName3 = []
        self.isCompName1 = False
        self.compName1 = []
        self.isCompName2 = False
        self.compName2 = []
        self.isCompName3 = False
        self.compName3 = []
        self.comp1Diff = None
        self.comp2Diff = None
        self.comp3Diff = None
        self.validChars = "`1234567890qwertyuiopasdfghjklzxcvbnm"
        self.shiftChars = '~!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'
        self.interval = 1000
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        start_time = pygame.time.get_ticks()
        playing = True
        while playing:
            counting_time = pygame.time.get_ticks() - start_time
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos), screen)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            
            if isinstance(self.currentPlayer, Player) and self.isBattlePhase:
                for player in self.playerList:
                    if isinstance(player[0], AgroRobo):
                        self.cardsInPlay += player[0].attack(self.cardOnSpot, self.currentPlayer, self.cardsInPlay)
            
            if isinstance(self.currentPlayer, Player) and self.isBattlePhase:
                for player in self.playerList:
                    if isinstance(player[0], OptimalRobo):
                        self.cardsInPlay += player[0].attack(self.cardOnSpot, self.currentPlayer, self.cardsInPlay, self.playerList)
            
            if self.isHomeScreen:
                screen.fill(self.bgColorHome)
            else:
                screen.fill(self.bgColorGame)
                for player in self.playerList:
                    if player[1] == True:
                        self.currentPlayer = player[0]
                    if player[2] == True:
                        self.currentPlayerTurn = player[0]
                    if player[0].level >= 10:
                        self.isWin = (True, player[0])
            
            # If either the door deck or the treasure deck runs out, then make a
            # new deck
            if len(self.gameDoorDeck.cards) == 0:
                self.gameDoorDeck = DoorDeck()
            if len(self.gameTreasureDeck.cards) == 0:
                self.gameTreasureDeck = TreasureDeck()
            
            self.redrawAll(screen, counting_time)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
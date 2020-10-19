#############################################
# Author: Pranay Gundam
#############################################

import socket
import threading
from queue import Queue

import pygame
from pygame import mixer
from Cards import *
from DrawScreensSockets import *
from Deck import *
from Players import *


# most of the basic beginning code to set up the socket and threading connections
# came from the TA mini-lecture starter code made by Rohan Varma and adapted by 
# Kyle Chin/Ping-Ya Chao
class PygameGame(object):
    
    ## 2 new functions specific to sockets! ##
    @staticmethod
    def setUpServer():

        # Be sure to specify a both a IP address in HOST and a port in PORT. If you want
        # to play local multiplayer then just put your internal IP address in HOST and
        # specify any port above 50000. If you want to play non-local multiplayer then
        # put you external IP address in HOST and assign PORT to a forwarded port.
        
        # 26.212.126.138
        HOST = "18.216.69.198"
        PORT = 64425

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((HOST, PORT))
        print("connected to server")

        serverMsg = Queue(100)
        threading.Thread(target=PygameGame.handleServerMsg, args=(server, serverMsg)).start()

        return server, serverMsg

    @staticmethod
    def handleServerMsg(server, serverMsg):
        server.setblocking(1)
        msg = ""
        command = ""
        while True:
            msg += server.recv(10).decode("UTF-8")
            command = msg.split("\n")
            while len(command) > 1:
                readyMsg = command[0]
                msg = "\n".join(command[1:])
                serverMsg.put(readyMsg)
                command = msg.split("\n")


    def init(self):
        pass

    def mousePressed(self, x, y, screen):
        w = self.width
        h = self.height  
        msg = ''
        if self.isHomeScreen:
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
                self.isNameScreen = True
                self.isHomeScreen = False
        
        elif self.isDrawSettings:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            
            if inBackButtonX and inBackButtonY:
                self.isDrawSettings = False
                self.isHomeScreen = True

        elif self.isDrawRules:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            
            if inBackButtonX and inBackButtonY:
                self.isDrawRules = False
                self.isHomeScreen = True           

        elif self.isNameScreen:
            inBackButtonX = (x>=20) and (x<=100)
            inBackButtonY = (y>=20) and (y<=100)
            inNameBarX = (x >= w/2 - 175) and (x <= w/2+175)
            inNameBarY = (y >= h/2 - 15) and (y <= h/2 + 15)
            inStartGameX = (x>= 3*w/8) and (x<= 5*w/8)
            inStartGameY = (y>= h - 100) and (y<= h - 50)
            name = ''.join(self.ownName)
            if inBackButtonX and inBackButtonY:
                self.isNameScreen = False
                self.isHomeScreen = True
            
            if inNameBarX and inNameBarY:
                self.inNameBar = True
            else:
                self.inNameBar = False

            if inStartGameX and inStartGameY:
                self.isNameScreen = False
                msg = f'AddPlayer {name} 4 4 None None 1\n'
                self.gameDoorDeck = DoorDeck()
                self.gameTreasureDeck = TreasureDeck()
                self.ownPlayer = Player(f'{name}', self.gameTreasureDeck, self.gameDoorDeck)
    
        else:
            numCards = len(self.ownPlayer.hand)
            inHandCardsX = (x >= self.width/4) and (x<=self.width/4 + 20*numCards)
            inHandCardsY = (y >= 3*self.height/4 + 10)
            inUseCardX = (x>=14*self.width/18 + 60) and (x<= 14*self.width/18 + 110)
            inUseCardY = (y>=14*self.height/18) and (y<=14*self.height/18 + 50)
            inDiscardCardX = (x>=14*self.width/18) and (x<=14*self.width/18 + 50)
            inDiscardCardY = (y>=14*self.height/18 + 60) and (y<=14*self.height/18 + 110)
            inDoorCardsX = (x>=14*self.width/18) and (x<=14*self.width/18+50)   
            inDoorCardsY = (y>=14*self.height/18) and (y<= 14*self.height/18+50)
            inNextTurnX = (x>=14*self.width/18 + 60) and (x<=14*self.width/18 + 110)
            inNextTurnY = (y>=14*self.height/18 + 60) and (y<=14*self.height/18 + 110)
            inPlayer1ButtonX = (x>=w-60) and (x<=w-20)
            inPlayer1ButtonY = (y>=h-164) and (y<=h-114)
            inPlayer2ButtonX = (x>=w-60) and (x<=w-20)
            inPlayer2ButtonY = (y>=h-112) and (y<=h-62)
            inPlayer3ButtonX = (x>=w-60) and (x<=w-20)
            inPlayer3ButtonY = (y>=h-60) and (y<=h-10)
            inBeatBattleX = (x>=14*self.width/18 - 80) and (x<=14*self.width/18 - 30)
            inBeatBattleY = (y>=14*self.height/18) and (y<=14*self.height/18 + 50)
            name = ''.join(self.ownName)

            isShowingPlayer = self.player1Show or self.player2Show or self.player3Show

            allBelowFive = True
            if len(self.ownPlayer.hand) > 5:
                allBelowFive = False
            for player in self.playerList:
                if player['TreasureCards'] + player['DoorCards'] > 5:
                    allBelowFive = False
                    break

            if inPlayer1ButtonX and inPlayer1ButtonY and len(self.playerList)>=1:
                self.player1Show = not self.player1Show
                self.player2Show = False
                self.player3Show = False


            elif inPlayer2ButtonX and inPlayer2ButtonY and len(self.playerList)>=2:
                self.player2Show = not self.player2Show
                self.player1Show = False
                self.player3Show = False
 
            elif inPlayer3ButtonX and inPlayer3ButtonY and len(self.playerList)>=3:
                self.player3Show = not self.player3Show
                self.player2Show = False
                self.player1Show = False
 
            # Changes the useCardMode based on whether or not the button was clicked.
            # This also turns off discard mode.
            if inUseCardX and inUseCardY and not isShowingPlayer:
                self.useCardMode = not self.useCardMode
                self.isDiscardPhase = False

            # Changes the discardMode based on whether or not the button was clicked.
            # This also turns off useCardMode.
            elif inDiscardCardX and inDiscardCardY and not isShowingPlayer:
                self.isDiscardPhase = not self.isDiscardPhase
                self.useCardMode = False

            # if we are in discard mode and we click on a card, then remove it
            # from the players hand
            elif self.isDiscardPhase and inHandCardsX and inHandCardsY and not isShowingPlayer:
                cardIndex = int((x - self.width/4)//20)
                poppedCard = self.ownPlayer.hand.pop(cardIndex)
                cardType = None
                if isinstance(poppedCard, Monster) or isinstance(poppedCard, PlayerClass) or isinstance(poppedCard, Race):
                    cardType = 'Door'
                else:
                    cardType = 'Treasure'
                msg = f'RemoveCard {name} {cardType}\n'

                numCards = len(self.ownPlayer.hand)
                if numCards == 0:
                    self.onHandCards = (False, None)
                elif cardIndex >= numCards:
                    cardIndex = numCards - 1
                    self.onHandCards = (True, self.ownPlayer.hand[cardIndex])

            # if a card in a player's hand was clicked and we are in useCardMode
            # then we use the card based on the type of card it is
            elif self.useCardMode and inHandCardsX and inHandCardsY and not isShowingPlayer:
                
                self.isDiscardPhase = False
                cardIndex = int((x - self.width/4)//20)
                playCard = self.ownPlayer.hand[cardIndex]
                print(playCard)
                # Apply a consumable to the playing field when a player is in battle
                if (isinstance(playCard, Consumable) and (self.cardOnSpot != None) and self.isBattlePhase):
                    self.ownPlayer.hand.pop(cardIndex)
                    numCards = len(self.ownPlayer.hand)
                    if numCards == 0:
                        self.onHandCards = (False, None)
                    elif cardIndex >= numCards:
                        cardIndex = numCards - 1
                        self.onHandCards = (True, self.ownPlayer.hand[cardIndex])
                    self.cardsInPlay.append(playCard)

                    msg = f'UseCard {name} Treasure cardsInPlay {str(playCard)}\n'
                
                # Apply a curse to the current player whenever
                elif isinstance(playCard, Curse) and (self.cardOnSpot != None):
                    self.ownPlayer.hand.pop(cardIndex)
                    numCards = len(self.ownPlayer.hand)
                    if numCards == 0:
                        self.onHandCards = (False, None)
                    elif cardIndex >= numCards:
                        cardIndex = numCards - 1
                        self.onHandCards = (True, self.ownPlayer.hand[cardIndex])
                    self.cardOnSpot.power -= playCard.power
                    self.cardsInPlay.append(playCard)

                    msg = f'UseCard {name} Treasure cardsInPlay {str(playCard)}\n'
                
                # Equip armour when a player is not in battle
                elif isinstance(playCard, Armour) and not self.isBattlePhase:
                    self.ownPlayer.hand.pop(cardIndex)
                    previousArmour = self.ownPlayer.applyArmour(playCard)
                    if previousArmour != None:
                        self.ownPlayer.hand.append(previousArmour)

                    msg = f'UseCard {name} Treasure Armour {str(playCard)}\n'
            
                # If we are in the second door phase and we want to fight against
                # our own monster
                elif (isinstance(playCard, Monster) and not self.canKickDoor[0] and
                      self.canKickDoor[1] and (self.currentPlayerTurn[1])):
                    self.cardOnSpot = playCard
                    self.isBattlePhase = True
                    self.canKickDoor[1] = False
                    self.ownPlayer.hand.pop(cardIndex)

                    msg = f'UseCard {name} Door Monster {str(playCard)}\n'
                
                # If the card is a Race card, then equip it
                elif (isinstance(playCard, Race) and not self.isBattlePhase):
                    self.ownPlayer.hand.pop(cardIndex)
                    if self.ownPlayer.race != None:
                        self.ownPlayer.hand.append(self.ownPlayer.race)
                    self.ownPlayer.race = playCard

                    msg = f'UseCard {name} Door Race {str(playCard)}\n'
                    
                # If the card is a class card, then equip it
                elif (isinstance(playCard, PlayerClass) and not self.isBattlePhase):
                    self.ownPlayer.hand.pop(cardIndex)
                    if self.ownPlayer.playerClass != None:
                        self.ownPlayer.hand.append(self.ownPlayer.playerClass)
                    self.ownPlayer.playerClass = playCard

                    msg = f'UseCard {name} Door playerClass {str(playCard)}\n'
            
            # If all the player have fewer than five cards and we are not in battle
            # and you click the next turn button then move on to the next player's
            # turn.
            
            elif ((inNextTurnX and inNextTurnY) and (not self.isBattlePhase) and (allBelowFive) and (not self.canKickDoor[1]) and (self.currentPlayerTurn[1])):
                self.canKickDoor = [True, True]
                self.isDiscardPhase = False
                self.useCardMode = False
                self.isBattlePhase = False
                self.canKickDoor = [True, True]
                self.currentPlayerTurn[0] = (self.currentPlayerTurn[0]+1) % (1+len(self.playerList))
                self.currentPlayerTurn[1] = False
                msg = f'NextTurnTrigger {name}\n'
                
            # if a player can kick down the door and clicks the button, then 
            # kick open the door (note that what happens to the door card is 
            # determined by if it was the first or second time the a player has
            # drawn a door card).
            
            elif (self.canKickDoor[1] and inDoorCardsX and inDoorCardsY and 
                  self.currentPlayerTurn[1] and allBelowFive):
                
                if not self.canKickDoor[0]:
                    self.canKickDoor[1] = False
                if self.isDiscardPhase:
                    self.isDiscardPhase = False
                if self.useCardMode:
                    self.useCardMode = False
                doorCard = self.gameDoorDeck.cards.pop()
                if isinstance(doorCard, Monster) and self.canKickDoor[0]:
                    self.cardOnSpot = doorCard
                    self.isBattlePhase = True
                    self.canKickDoor[1] = False
                    msg = f'DoorKickBattle {name} {str(doorCard)}\n'
                else:
                    self.canKickDoor[0] = False
                    self.ownPlayer.hand.append(doorCard)
                    msg = f'DoorKickNormal {name}\n'

            playedCardsPower = 0
            for card in self.cardsInPlay:
                playedCardsPower += card.power

            # If you click fight monster and you can beat the monster, then reap
            # the rewards
            if (inBeatBattleX and inBeatBattleY and self.isBattlePhase and 
               (self.ownPlayer.calcBattlePower() + playedCardsPower > self.cardOnSpot.power) and self.currentPlayerTurn[1]):
                self.isBattlePhase = False
                self.ownPlayer.level += 1
                self.cardsInPlay = []
                rewardCount = self.cardOnSpot.reward
                for num in range(self.cardOnSpot.reward):
                    self.ownPlayer.hand.append(self.gameTreasureDeck.cards.pop())

                msg = f'BeatMonster {name} {rewardCount}\n'

            # If you click fight monster and you can beat the monster, then suffer
            # the consequences
            elif (inBeatBattleX and inBeatBattleY and self.isBattlePhase and 
                 (self.ownPlayer.calcBattlePower() + playedCardsPower <= self.cardOnSpot.power) and self.currentPlayerTurn[1]):
                self.isBattlePhase = False
                self.ownPlayer.level = 1
                self.ownPlayer.hand = []
                self.cardsInPlay = []
                self.ownPlayer.playerClass = None
                self.ownPlayer.race = None
                self.ownPlayer.armour = {'LeftH': None, 'RightH': None, 'Boots': None, 
                       'Chest': None, 'Headgear': None, 'Misc': None}
                for num in range(4):
                    self.ownPlayer.hand.append(self.gameDoorDeck.cards.pop())
                    self.ownPlayer.hand.append(self.gameTreasureDeck.cards.pop())

                msg = f'LostMonster {name}\n'

            print(f'first can kick door: {self.canKickDoor[0]}')
            print(f'second can kick door: {self.canKickDoor[1]}')

        if msg != "":
            print("sending: " + msg)
            self.server.send(msg.encode()) 

    def mouseReleased(self, x, y):
        pass
    
    def mouseMotion(self, x, y):
        if not self.isHomeScreen and not self.isDrawRules and not self.isDrawSettings and not self.playScreen and not self.isNameScreen:
            howManyArmour = 0
            for armour in self.ownPlayer.armour:
                if self.ownPlayer.armour[armour] != None:
                    howManyArmour += 1
            
            numCards = len(self.ownPlayer.hand)
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
            
            isShowingPlayer = self.player1Show or self.player2Show or self.player3Show

            # If the mouse hovers over the cards in the player's hands
            if inHandCardsX and inHandCardsY and not isShowingPlayer:
                cardIndex = int((x - self.width/4)//20)
                if cardIndex >= numCards:
                    cardIndex = numCards - 1
                self.onHandCards = (True, self.ownPlayer.hand[cardIndex])
            
            # if the mouse hovers over the cards that have been played
            elif self.isBattlePhase and inCardsPlayedX and inCardsPlayedY and not isShowingPlayer:
                cardIndex = int((x - 150)//20)
                if cardIndex >= numCards:
                    cardIndex = numCards - 1
                self.onHandCards = (True, self.cardsInPlay[cardIndex])
            
            # if the mouse hovers over the armour cards
            elif inArmourX and inArmourY and not isShowingPlayer:
                cardIndex = int((x - 5)//20)
                count = 0
                for armourPiece in self.ownPlayer.armour:
                    if self.ownPlayer.armour[armourPiece] != None and count == cardIndex:
                        self.onHandCards = (True, self.ownPlayer.armour[armourPiece])
                        break
                    elif self.ownPlayer.armour[armourPiece] != None:
                        count +=1
            
            # if the mouse hovers over the race card
            elif inRaceX and inRaceY and not isShowingPlayer:
                self.onHandCards = (True, self.ownPlayer.race)

            # if the mouse hovers over the class card
            elif inPlayerClassX and inPlayerClassY and not isShowingPlayer:
                self.onHandCards = (True, self.ownPlayer.playerClass)

            else:
                self.onHandCards = (False, None)

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if self.isNameScreen:
            if self.inNameBar:
                if chr(keyCode) in self.validChars and (self.isKeyPressed(pygame.K_RSHIFT) or self.isKeyPressed(pygame.K_LSHIFT)):
                    self.ownName += self.shiftChars[self.validChars.index(chr(keyCode))]
                elif chr(keyCode) in self.validChars:
                    self.ownName += chr(keyCode)
                elif keyCode == pygame.K_BACKSPACE:
                    self.ownName = self.ownName[:-1]  


    def keyReleased(self, keyCode, modifier):
        pass    

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen, time):
        if self.isHomeScreen:
            drawHomeScreen(screen, self.width, self.height)
        elif self.isDrawRules:
            drawRulesScreen(screen, self.width, self.height)
        elif self.isDrawSettings:
            drawSettingsScreen(screen, self.width, self.height)
        elif self.isWin[0]:
            drawWinScreen(screen, self.width, self.height, self.isWin[1])
        elif self.isNameScreen:
            drawNameScreen(screen, self.width, self.height, ''.join(self.ownName))
        elif self.isBattlePhase:
            drawBattleCards(screen, self.width, self.height, self.cardOnSpot, self.cardsInPlay, 
                            self.useCardMode, self.isDiscardPhase, self.currentPlayerTurn[1], self.playerList, 
                            self.ownPlayer, self.player1Show, self.player2Show, self.player3Show)
            if self.onHandCards[0]:
                drawCards(screen, self.width - 300, 10, self.onHandCards[1])
        else:
            drawGameScreen(screen, self.width, self.height, self.playerList, self.currentPlayerTurn[1], self.isDiscardPhase,
                           self.useCardMode, self.ownPlayer, self.player1Show, self.player2Show, self.player3Show)
            if self.onHandCards[0]:
                drawCards(screen, self.width - 300, 10, self.onHandCards[1])
            
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)


    def __init__(self, width=1000, height=600, fps=50, title='112 Pygame Game'):
        self.server, self.serverMsg = self.setUpServer()
        #basic class attributes for pygame
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColorHome = (144,204,245)
        self.bgColorGame = (255,229,204)

        #class attributes that give info on the phase of the game
        self.isHomeScreen = True
        self.isDoorPhase = False
        self.isBattlePhase = False
        self.isDiscardPhase = False
        self.isDrawRules = False
        self.isDrawSettings = False
        self.playScreen = False
        self.isWin = (False, None)
        self.useCardMode = False
        self.isNameScreen = False

        #class attributes that keep track of all the players
        self.playerList = []
        self.ownPlayer = None
        self.currentPlayerTurn = [0, True]
        self.inNameBar = False
        self.ownName = []
        self.player1Show = False
        self.player2Show = False
        self.player3Show = False
        
        #class attributes that keep track of information regarding the cards in 
        #play and the cards on the screen
        self.gameDoorDeck = DoorDeck()
        self.gameTreasureDeck = TreasureDeck()
        self.onHandCards = (False, None)
        self.cardOnSpot = None
        self.cardsInPlay = list()

        #extra class attribute
        self.canKickDoor = [True, True]

        #class attribute used for typing text
        self.validChars = "`1234567890qwertyuiopasdfghjklzxcvbnm"
        self.shiftChars = '~!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'
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
            
            # If either the door deck or the treasure deck runs out, then make a
            # new deck
            if len(self.gameDoorDeck.cards) == 0:
                self.gameDoorDeck = DoorDeck()
            if len(self.gameTreasureDeck.cards) == 0:
                self.gameTreasureDeck = TreasureDeck()

            if self.isHomeScreen:
                screen.fill(self.bgColorHome)
            else:
                screen.fill(self.bgColorGame)
                if self.ownPlayer != None and self.ownPlayer.level >= 10:
                    self.isWin = (True, self.ownPlayer.name)
                if not self.isNameScreen:
                    for player in self.playerList:
                        if player != None and player['Level'] >= 10:
                            self.isWin(True, player['Name'])
            while self.serverMsg.qsize() > 0:
                msg = self.serverMsg.get(False)

                try:
                    print("received: " + msg + "\n")
                    msg = msg.split()
                    command = msg[0]

                    if command == "AddPlayer":
                        self.currentPlayerTurn[1] == True
                        self.playerList.append({'Name':msg[2], 'DoorCards': int(msg[3]), 'TreasureCards': int(msg[4]), 'Race': None, 'PlayerClass': None,
                                                'Level': int(msg[7]), 'Armour': {'LeftH': None, 'RightH': None, 'Boots': None, 'Chest': None, 'Headgear': None, 'Misc': None}})
                        print('the player code is ' + msg[1])
                        print(int(msg[1]) == self.currentPlayerTurn[0])
                        print(int(msg[1]))
                        print(self.currentPlayerTurn[0])
                        if int(msg[1]) == self.currentPlayerTurn[0]:
                            self.currentPlayerTurn[1] = False
                        print(self.currentPlayerTurn[1])

                    elif command == "RemoveCard":
                        for player in self.playerList:
                            if player['Name'] == msg[2]:
                                if msg[3] == 'Treasure':
                                    player['TreasureCards'] -= 1
                                else:
                                    player['DoorCards'] -= 1

                    elif command == 'UseCard':
                        for player in self.playerList:
                            if player['Name'] == msg[2]:
                                if msg[3] == 'Treasure':
                                    player['TreasureCards'] -= 1
                                elif msg[3] == 'Door':
                                    player['DoorCards'] -= 1
                                
                                if msg[4] == 'Race':
                                    if player['Race'] != None:
                                        player['DoorCards'] += 1
                                    player['Race'] = returnObject(msg[5])
                                
                                elif msg[4] == 'playerClass':
                                    if player['PlayerClass'] != None:
                                        player['DoorCards'] += 1                               
                                    player['PlayerClass'] = returnObject(msg[5])
                                
                                elif msg[4] == 'Armour':
                                    armourPiece = returnObject(msg[5])
                                    armourType = armourPiece.armourType
                                    if player['Armour'][armourType] != None:
                                        player['TreasureCards'] += 1
                                    player['Armour'][armourType] = armourPiece
                                
                                elif msg[4] == 'cardsInPlay':
                                    cardToPlace = returnObject(msg[5])
                                    self.cardsInPlay.append(cardToPlace)
                                    
                                elif msg[4] == 'Monster':
                                    monsterCard = returnObject(msg[5])
                                    self.cardOnSpot = monsterCard
                                    self.isBattlePhase = True
                    
                    # I think that the NextTurnTrigger and NextTurnTriggered command and instructions
                    # are a pretty cool way to get around clients not being able to access their own
                    # IDs in order to figure out whose turn it is.
                    elif command == 'NextTurnTrigger':
                        self.currentPlayerTurn[0] =  (self.currentPlayerTurn[0]+1) % (1+len(self.playerList))
                        name = ''.join(self.ownPlayer.name)
                        if len(self.playerList) == 1:
                            self.currentPlayerTurn[1] = True
                        msgTurn = f'NextTurnTriggered {name}\n'
                        print("sending: " + msgTurn)
                        self.server.send(msgTurn.encode())

                    
                    elif command == 'NextTurnTriggered':
                        print(f'currentplayerturn: {self.currentPlayerTurn[0]}')
                        self.currentPlayerTurn[1] = True
                        if int(msg[1]) == self.currentPlayerTurn[0]:
                            self.currentPlayerTurn[1] = False

                    elif command == 'DoorKickBattle':
                        self.cardOnSpot = returnObject(msg[3])
                        self.isBattlePhase = True

                    elif command == 'DoorKickNormal':
                        for player in self.playerList:
                            if player['Name']:
                                player['DoorCards'] += 1

                    elif command == 'BeatMonster':
                        self.cardOnSpot = None
                        self.isBattlePhase = False
                        self.cardsInPlay = []
                        for player in self.playerList:
                            if player['Name'] == msg[2]:
                                player['Level'] += 1
                                player['TreasureCards'] += int(msg[3])

                    elif command == 'LostMonster':
                        self.cardOnSpot = None
                        self.isBattlePhase = False
                        self.cardsInPlay = []
                        for player in self.playerList:
                            if player['Name'] == msg[2]:
                                player['DoorCards'] = 4
                                player['TreasureCards'] = 4
                                player['Armour'] = {'LeftH': None, 'RightH': None, 'Boots': None, 'Chest': None, 'Headgear': None, 'Misc': None}
                                player['Level'] = 1
                                player["Race"] = None
                                player['PlayerClass'] = None


                except Exception as e:
                    print(f"we failed in client: {e}")
                self.serverMsg.task_done()
                        
            self.redrawAll(screen, counting_time)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
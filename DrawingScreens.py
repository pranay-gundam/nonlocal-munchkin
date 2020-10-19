#############################################
# Author: Pranay Gundam
#############################################

# This file contains most of the functions to draw the main screens

import pygame
from HelperFunction import *
from Players import *
from GameAI import *

# This function draws the screen when we are on the homepage
def drawHomeScreen(screen, width, height):
    LIGHTYELLOW = (255,255,204)
    
    '''
    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/4 - 10, 3*height/4 - 60),(width/4, 50)))
    playButtonText = 'One Player'
    writeTextCenter(screen, 3*width/8 - 10, 3*height/4 - 35, playButtonText, (0,0,0), 32, None)    
   
    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/4 - 10, 3*height/4 + 10),(width/4, 50)))
    playButtonText = 'Two Player'
    writeTextCenter(screen, 3*width/8 - 10, 3*height/4 + 35, playButtonText, (0,0,0), 32, None)

    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/2 + 10, 3*height/4 - 60),(width/4, 50)))
    playButtonText = 'Three Player'
    writeTextCenter(screen, 5*width/8+10, 3*height/4 - 35, playButtonText, (0,0,0), 32, None)

    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/2 + 10, 3*height/4 + 10),(width/4, 50)))
    playButtonText = 'Four Player'
    writeTextCenter(screen, 5*width/8+10, 3*height/4 + 35, playButtonText, (0,0,0), 32, None)
    '''

    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((3*width/8, 3*height/4 - 55),(width/4, 50)))
    playButtonText = 'Play'
    writeTextCenter(screen, width/2, 3*height/4 - 30, playButtonText, (0,0,0), 32, None)

    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/4 - 10, 3*height/4 - 130),(width/4, 50)))
    playButtonText = 'Rules and Information'
    writeTextCenter(screen, 3*width/8 - 10, 3*height/4 - 105, playButtonText, (0,0,0), 32, None)

    pygame.draw.rect(screen, LIGHTYELLOW, 
                    ((width/2 + 10, 3*height/4 - 130),(width/4, 50)))
    playButtonText = 'Settings'
    writeTextCenter(screen, 5*width/8+10, 3*height/4 - 105, playButtonText, (0,0,0), 32, None)

    titleText = 'Munchkins (Special 112 Edition)'
    writeTextCenter(screen, width/2, height/4, titleText, (0,0,0), 32, None)    

def drawPlayScreen(screen, width, height, numHumans, numComps):
    pygame.draw.rect(screen, (0,0,0), 
                    ((20, 20),(80, 80)))
    backButtonText = 'Go Back'
    writeTextCenter(screen, 60, 60, backButtonText, (255,255,255), 20, None)

    writeTextTopLeft(screen, 20, height/2 - 30, 'Human Players:', (0,0,0), 25, None)
    x0 = 160
    y0 = height/2 - 30
    for count in range(4):
        pygame.draw.rect(screen, (0,0,0), ((x0 + 40*count-1, y0-1), (22,22)))
        pygame.draw.rect(screen, (255,255,255), ((x0 + 40*count, y0), (20,20)))
        writeTextCenter(screen, x0 + 40*count + 10, y0+30, f'{count}', (0,0,0), 15, None)

        if numHumans != None and numHumans == count:
            pygame.draw.line(screen, (0,0,0), (x0 + 40*count + 5, y0 + 5), 
                             (x0 + 40*count + 10, y0 + 10), 3)
            pygame.draw.line(screen, (0,0,0), (x0 + 40*count + 10, y0 + 10), 
                             (x0 + 40*count + 25, y0 - 5), 3)
    '''
    x0 = width/2
    y0 = 50
    if numHumans != None and numHumans != 0:
        for count in range(numHumans):
            writeTextTopLeft(screen, x0, y0, f'Human #{count+1} Name:', (0,0,0), 25, None)

            pygame.draw.rect(screen, (0,0,0), ((x0 + 149, y0 - 6),(327, 32)))
            pygame.draw.rect(screen, (255,255,255), ((x0 + 150, y0 - 5),(325, 30)))

            y0 += 50
    '''
    writeTextTopLeft(screen, 20, height/2 + 20, 'Computer Players:', (0,0,0), 25, None)
    x0 = 185
    y0 = height/2 + 20
    for count in range(4):
        pygame.draw.rect(screen, (0,0,0), ((x0 + 40*count-1, y0-1), (22,22)))
        pygame.draw.rect(screen, (255,255,255), ((x0 + 40*count, y0), (20,20)))
        writeTextCenter(screen, x0 + 40*count + 10, y0+30, f'{count}', (0,0,0), 15, None)

        if numComps != None and numComps == count:
            pygame.draw.line(screen, (0,0,0), (x0 + 40*count + 5, y0 + 5), 
                             (x0 + 40*count + 10, y0 + 10), 3)
            pygame.draw.line(screen, (0,0,0), (x0 + 40*count + 10, y0 + 10), 
                             (x0 + 40*count + 25, y0 - 5), 3)
    '''
    x0 = width/2
    y0 = height/2 - 40
    if numComps != None and numComps != 0:
        for count in range(numComps):
            writeTextTopLeft(screen, x0, y0, f'Computer #{count+1} Name:', (0,0,0), 25, None)
            for count2 in range(4):
                pygame.draw.rect(screen, (0,0,0), ((x0 + 40*count2 - 1, y0 -1 + 30),(22,22)))
                pygame.draw.rect(screen, (255,255,255), ((x0 + 40*count2, y0 + 30),(20,20)))
                if count2 == 0:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Very Easy', (0,0,0), 12, None)
                if count2 == 1:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Easy', (0,0,0), 12, None)
                if count2 == 2:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Medium', (0,0,0), 12, None)
                if count2 == 3:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Hard', (0,0,0), 12, None)
            
            pygame.draw.rect(screen, (0,0,0), ((x0 + 169, y0 - 6),(302, 32)))
            pygame.draw.rect(screen, (255,255,255), ((x0 + 170, y0 - 5),(300, 30)))

            
            y0 += 70
    '''
    
    pygame.draw.rect(screen, (0,0,0), 
                    ((3*width/8 - 2, height - 102),(width/4 + 4, 54)))
    pygame.draw.rect(screen, (153,255,204), 
                    ((3*width/8, height - 100),(width/4, 50)))
    backButtonText = 'Next'
    writeTextCenter(screen, 4*width/8, height - 75, backButtonText, (0,0,0), 32, None)

def drawNameScreen(screen, width, height, numHumans, numComps, comp1Diff, 
                   comp2Diff, comp3Diff, human1Name, human2Name, human3Name, 
                   comp1Name, comp2Name, comp3Name):
    
    pygame.draw.rect(screen, (0,0,0), 
                    ((20, 20),(80, 80)))
    backButtonText = 'Go Back'
    writeTextCenter(screen, 60, 60, backButtonText, (255,255,255), 20, None)

    x0 = 30
    y0 = height/2
    if numComps != None and numComps != 0:
        for count in range(numComps):
            writeTextTopLeft(screen, x0, y0, f'Computer #{count+1} Name:', (0,0,0), 25, None)
            for count2 in range(4):
                pygame.draw.rect(screen, (0,0,0), ((x0 + 40*count2 - 1, y0 -1 + 30),(22,22)))
                pygame.draw.rect(screen, (255,255,255), ((x0 + 40*count2, y0 + 30),(20,20)))
                
                if (count2 == comp1Diff) and (count == 0):
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 5, y0 + 35), 
                                    (x0 + 40*count2 + 10, y0 + 40), 3)
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 10, y0 + 40), 
                                    (x0 + 40*count2 + 25, y0 + 25), 3)
                if (count2 == comp2Diff) and (count == 1):
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 5, y0 + 35), 
                                    (x0 + 40*count2 + 10, y0 + 40), 3)
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 10, y0 + 40), 
                                    (x0 + 40*count2 + 25, y0 + 25), 3)                
                if (count2 == comp3Diff) and (count == 2):
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 5, y0 + 35), 
                                    (x0 + 40*count2 + 10, y0 + 40), 3)
                    pygame.draw.line(screen, (0,0,0), (x0 + 40*count2 + 10, y0 + 40), 
                                    (x0 + 40*count2 + 25, y0 + 25), 3)

                if count2 == 0:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Very Easy', (0,0,0), 12, None)
                if count2 == 1:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Easy', (0,0,0), 12, None)
                if count2 == 2:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Medium', (0,0,0), 12, None)
                if count2 == 3:
                    writeTextCenter(screen, x0 + 40*count2 + 10, y0+60, 'Hard', (0,0,0), 12, None)
                
            pygame.draw.rect(screen, (0,0,0), ((x0 + 169, y0 - 6),(302, 32)))
            pygame.draw.rect(screen, (255,255,255), ((x0 + 170, y0 - 5),(300, 30)))
            if count == 0:
                comp1Text = ''.join(comp1Name)
                writeTextTopLeft(screen, x0 + 170, y0+3, comp1Text, (0,0,0), 25, None)
            elif count == 1:
                comp2Text = ''.join(comp2Name)
                writeTextTopLeft(screen, x0 + 170, y0+3, comp2Text, (0,0,0), 25, None)
            elif count == 2:
                comp3Text = ''.join(comp3Name)
                writeTextTopLeft(screen, x0 + 170, y0+3, comp3Text, (0,0,0), 25, None)
            y0 += 70

    x0 = 30
    y0 = 125
    if numHumans != None and numHumans != 0:
        for count in range(numHumans):
            writeTextTopLeft(screen, x0, y0, f'Human #{count+1} Name:', (0,0,0), 25, None)

            pygame.draw.rect(screen, (0,0,0), ((x0 + 149, y0 - 6),(327, 32)))
            pygame.draw.rect(screen, (255,255,255), ((x0 + 150, y0 - 5),(325, 30)))

            if count == 0:
                human1Text = ''.join(human1Name)
                writeTextTopLeft(screen, x0 + 165, y0+3, human1Text, (0,0,0), 20, None)
            elif count == 1:
                human2Text = ''.join(human2Name)
                writeTextTopLeft(screen, x0 + 165, y0+3, human2Text, (0,0,0), 20, None)
            elif count == 2:
                human3Text = ''.join(human3Name)
                writeTextTopLeft(screen, x0 + 165, y0+3, human3Text, (0,0,0), 20, None)

            y0 += 50

    pygame.draw.rect(screen, (0,0,0), 
                    ((3*width/8 - 2, height - 102),(width/4 + 4, 54)))
    pygame.draw.rect(screen, (153,255,204), 
                    ((3*width/8, height - 100),(width/4, 50)))
    
    backButtonText = 'Start Game'
    writeTextCenter(screen, 4*width/8, height - 75, backButtonText, (0,0,0), 32, None)

# Ideas about timer came from 
# https://stackoverflow.com/questions/20359845/how-would-i-add-a-running-timer-that-shows-up-on-the-screen-in-pygame?rq=1
# This function draws the screen when it is in game mode
def drawGameScreen(screen, width, height, time, cplayer, discardPhase, 
                   currentTurn, useCardMode, playerRace, playerClass, compTimer, interval):
    
    DOORCARDCOLOR = (201,150,99)
    DOORCARDEDGE = (111,82,54)
    pygame.draw.rect(screen, DOORCARDEDGE, 
                    ((7,height/2 - 103),(126,206)))
    pygame.draw.rect(screen, DOORCARDCOLOR, 
                    ((10,height/2 - 100),(120,200)))

    doorText = 'Door'
    writeTextCenter(screen, 70, height/2, doorText, (0,0,0), 25, None)

    TREASURECARDCOLOR = (200,167,114)
    TREASURECARDEDGE = (100,76,53)
    pygame.draw.rect(screen, TREASURECARDEDGE, 
                    ((width - 133,height/2 - 103),(126,206)))
    pygame.draw.rect(screen, TREASURECARDCOLOR, 
                    ((width - 130,height/2 - 100),(120,200)))

    treasureText = 'Treasure'
    writeTextCenter(screen, width - 70, height/2, treasureText, (0,0,0), 25, None) 
    
    # these next four lines of code draw the timer at the top of the screen
    minutes = str(int(time/60000)).zfill(2)
    seconds = str(int((time%60000)/1000)).zfill(2)
    timeText = f'{minutes}:{seconds}'
    writeTextCenter(screen, width/2, 40, timeText, (0,0,0), 25, None)

    writeTextCenter(screen, width/2, height/2 - 30, f'{currentTurn.name}\'s Turn', (0,0,0), 40, None)
    writeTextCenter(screen, width/2, height/2, f'{cplayer.name}\'s Screen', (0,0,0), 40, None)
    writeTextCenter(screen, width/2, height/2 + 20, f'Player Level: {cplayer.level}', (0,0,0), 30, None)

    DRAWDOORCOLOR = (153,225,204)
    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 20, 'Draw', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 30, 'Card', (0,0,0), 15, None)
    
    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 60, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 20, 'Switch', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 30, 'Player', (0,0,0), 15, None)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 60, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 80, 'Next', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 90, 'Turn', (0,0,0), 15, None)

    USECARDCOLOR = DRAWDOORCOLOR

    if discardPhase:
        DRAWDOORCOLOR = (255,153,255)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 80, 'Discard', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 90, 'Card', (0,0,0), 15, None)

    if useCardMode:
        USECARDCOLOR = (255,153,255)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 120, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, USECARDCOLOR, ((14*width/18 + 120, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 80, 'Use', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 90, 'Card', (0,0,0), 15, None)

    # the next five lines of codes draw the cards in the player's hand
    x0 = width/4
    y0 = 3*height/4 + 10
    for card in cplayer.hand:
        if card != None:
            drawCards(screen, x0, y0, card)
            x0 += 20

    # the next six lines of codes draw the cards that the player has equiped as
    # armour
    x0 = 5
    y0 = 3*height/4 + 10
    for armourType in cplayer.armour:
        if cplayer.armour[armourType] != None:
            drawCards(screen, x0, y0, cplayer.armour[armourType])
            x0+=20

    drawCards(screen, 3*width/4 - 100, height - 20, playerRace)
    drawCards(screen, 3*width/4 - 70, height - 20, playerClass)
    
    if isinstance(cplayer, PassiveRobot) or isinstance(cplayer, AgroRobo) or isinstance(cplayer, StupidRobot) or isinstance(cplayer, OptimalRobo):
        pygame.draw.rect(screen, (0,0,0),((width/3-1, 4),(width/3+2, 22)))
        pygame.draw.rect(screen, (255,255,255),((width/3, 5),(width/3, 20)))
        pygame.draw.rect(screen, (160,160,160),((width/3, 5),((compTimer/interval)*width/3, 20)))

# draw the screen when we are in battling phase
def drawBattleCards(screen, width, height, monsterCard, time, discardPhase, 
                    cplayer, useCardMode, cardsInPlay, currentTurn, playerRace,
                    playerClass, compTimer, interval):
    monsterCard.drawMonster(screen, width/2 - 60, height/2 - 100)

    writeTextCenter(screen, width/2, height/2 - 230, f'{currentTurn.name}\'s Turn', (0,0,0), 40, None)
    writeTextCenter(screen, width/2, height/2 - 200, f'{cplayer.name}\'s Screen', (0,0,0), 40, None)
    writeTextCenter(screen, width/2, height/2 - 180, f'Player Level: {cplayer.level}', (0,0,0), 30, None)
    
    DOORCARDCOLOR = (201,150,99)
    DOORCARDEDGE = (111,82,54)
    pygame.draw.rect(screen, DOORCARDEDGE, 
                    ((7,height/2 - 103),(126,206)))
    pygame.draw.rect(screen, DOORCARDCOLOR, 
                    ((10,height/2 - 100),(120,200)))

    doorText = 'Door'
    writeTextCenter(screen, 70, height/2, doorText, (0,0,0), 25, None)

    TREASURECARDCOLOR = (200,167,114)
    TREASURECARDEDGE = (100,76,53)
    pygame.draw.rect(screen, TREASURECARDEDGE, 
                    ((width - 133,height/2 - 103),(126,206)))
    pygame.draw.rect(screen, TREASURECARDCOLOR, 
                    ((width - 130,height/2 - 100),(120,200)))

    treasureText = 'Treasure'
    writeTextCenter(screen, width - 70, height/2, treasureText, (0,0,0), 25, None) 
    
    minutes = str(int(time/60000)).zfill(2)
    seconds = str(int((time%60000)/1000)).zfill(2)

    timeText = f'{minutes}:{seconds}'
    writeTextCenter(screen, width/2, 40, timeText, (0,0,0), 25, None)

    DRAWDOORCOLOR = (153,225,204)
    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 20, 'Draw', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 30, 'Card', (0,0,0), 15, None)
    
    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 60, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 20, 'Switch', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 30, 'Player', (0,0,0), 15, None)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 60, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 80, 'Next', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 90, 'Turn', (0,0,0), 15, None)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 120, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 120, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 20, 'Fight', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 30, 'Monster', (0,0,0), 15, None)

    USECARDCOLOR = DRAWDOORCOLOR

    if discardPhase:
        DRAWDOORCOLOR = (255,153,255)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 80, 'Discard', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 90, 'Card', (0,0,0), 15, None)

    if useCardMode:
        USECARDCOLOR = (255,153,255)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 120, 14*height/18-1 + 60), (52, 52)))
    pygame.draw.ellipse(screen, USECARDCOLOR, ((14*width/18 + 120, 14*height/18 + 60), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 80, 'Use', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 145, 14*height/18 + 90, 'Card', (0,0,0), 15, None)

    x0 = width/4
    y0 = 3*height/4 + 10
    for card in cplayer.hand:
        if card != None:
            drawCards(screen, x0, y0, card)
            x0 += 20

    x0 = 150
    y0 = 20
    for playCard in cardsInPlay:
        drawCards(screen, x0, y0, playCard)
        x0+=20
    
    x0 = 5
    y0 = 3*height/4 + 10
    for armourType in cplayer.armour:
        if cplayer.armour[armourType] != None:
            drawCards(screen, x0, y0, cplayer.armour[armourType])
            x0+=20

    drawCards(screen, 3*width/4 - 100, height - 20, playerRace)
    drawCards(screen, 3*width/4 - 70, height - 20, playerClass)

    if isinstance(cplayer, PassiveRobot) or isinstance(cplayer, AgroRobo) or isinstance(cplayer, StupidRobot) or isinstance(cplayer, OptimalRobo):
        pygame.draw.rect(screen, (0,0,0),((width/3-1, 4),(width/3+2, 22)))
        pygame.draw.rect(screen, (255,255,255),((width/3, 5),(width/3, 20)))
        pygame.draw.rect(screen, (160,160,160),((width/3, 5),((compTimer/interval)*width/3, 20)))


def drawRulesScreen(screen, width, height):
    
    text1 = 'Ok but for real though, most of the rules of Munchkin: 112 Edition are already built in automatically into the game. Keep note, however, that players are not allowed'
    text2 = 'to take any major action such as drawing a card, fighting a monster, or going onto the next player\'s turn until every player in the game has less than 5 cards in their hand.'
    text3 = 'For a full list of rules refer to https://munchkin.game/site-munchkin/assets/files/1138/munchkin_rules-1.pdf, although there are a couple of functionalities that are not yet '
    text4 = 'built into this game such as trading cards, unique monster consequences, etc. Additionally, class and race cards contribute a power level to combat.'
    writeTextCenter(screen, width/2, 3*height/4 + 40, text1, (0,0,0), 17, None)
    writeTextCenter(screen, width/2, 3*height/4 + 55, text2, (0,0,0), 17, None)
    writeTextCenter(screen, width/2, 3*height/4 + 70, text3, (0,0,0), 17, None)
    writeTextCenter(screen, width/2, 3*height/4 + 85, text4, (0,0,0), 17, None)

    writeTextCenter(screen, width/2, height/2, 'THERE ARE NONE', (0,0,0), 100, None)
    pygame.draw.rect(screen, (0,0,0), 
                    ((20, 20),(80, 80)))
    backButtonText = 'Go Back'
    writeTextCenter(screen, 60, 60, backButtonText, (255,255,255), 20, None)    

def drawSettingsScreen(screen, width, height):
    writeTextCenter(screen, width/2, height/2, 'Coming Soon!', (0,0,0), 100, None)
    pygame.draw.rect(screen, (0,0,0), 
                    ((20, 20),(80, 80)))
    backButtonText = 'Go Back'
    writeTextCenter(screen, 60, 60, backButtonText, (255,255,255), 20, None)

def drawWinScreen(screen, width, height, cplayer, winner):
    writeTextCenter(screen, width/2, height/2, f'{winner.name} Wins!!!', (0,0,0), 50, None)

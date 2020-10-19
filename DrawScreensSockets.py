#############################################
# Author: Pranay Gundam
#############################################

import pygame
from HelperFunction import *
from Players import *


def drawHomeScreen(screen, width, height):
    LIGHTYELLOW = (255,255,204)

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


def drawNameScreen(screen, width, height, name):
    writeTextCenter(screen, width/2, height/2 - 40, 'What\'s Your Name?', (0,0,0), 30, None)

    pygame.draw.rect(screen, (0,0,0), ((width/2 - 176, height/2 - 16),(352, 32)))
    pygame.draw.rect(screen, (255,255,255), ((width/2 - 175, height/2 - 15),(350, 30)))
    writeTextCenter(screen, width/2, height/2, name, (0,0,0), 30, None)

    pygame.draw.rect(screen, (0,0,0), 
                    ((20, 20),(80, 80)))
    backButtonText = 'Go Back'
    writeTextCenter(screen, 60, 60, backButtonText, (255,255,255), 20, None)

    pygame.draw.rect(screen, (0,0,0), 
                    ((3*width/8 - 2, height - 102),(width/4 + 4, 54)))
    pygame.draw.rect(screen, (153,255,204), 
                    ((3*width/8, height - 100),(width/4, 50)))
    
    writeTextCenter(screen, 4*width/8, height - 75, 'Start Game', (0,0,0), 32, None)

def drawGameScreen(screen, width, height, playerList, currentTurn, discardPhase,
                   useCardMode, ownPlayer, player1Show, player2Show, player3Show):

    if currentTurn:
        writeTextCenter(screen, width/2, height/2, 'It\'s Your Turn', (0,0,0), 40, None)
    else:
        writeTextCenter(screen, width/2, height/2, 'It\'s Not Your Turn', (0,0,0), 40, None)

    DOORCARDCOLOR = (201,150,99)
    DOORCARDEDGE = (111,82,54)

    TREASURECARDCOLOR = (200,167,114)
    TREASURECARDEDGE = (100,76,53)

    for index in range(len(playerList)):
        font = pygame.font.SysFont(None, 30) 
        if index == 0:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            text = pygame.transform.rotate(text, 270)
            rectText = text.get_rect()
            rectText.center = (80, height/2)
            screen.blit(text, rectText)
            x0 = 0
            y0 = 150

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0, y0),(60, 120)))
                y0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0, y0),(60, 120)))
                y0 += 20

        elif index == 1:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            rectText = text.get_rect()
            rectText.center = (width/2, 80)
            screen.blit(text, rectText)
            x0 = width/4 + 30
            y0 = 0

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0-3,y0),(126, 63)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0, y0),(120, 60)))
                x0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0-3,y0),(126, 63)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0, y0),(120, 60)))
                x0 += 20      

        elif index == 2:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            text = pygame.transform.rotate(text, 90)
            rectText = text.get_rect()
            rectText.center = (width - 80, height/2)
            screen.blit(text, rectText)
            x0 = width - 63
            y0 = 150

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0+3, y0),(60, 120)))
                y0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0+3, y0),(60, 120)))
                y0 += 20      


    
    DRAWDOORCOLOR = (153,225,204)
    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 20, 'Draw', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 30, 'Card', (0,0,0), 15, None)

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

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, USECARDCOLOR, ((14*width/18 + 60, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 20, 'Use', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 30, 'Card', (0,0,0), 15, None)


    # the next five lines of codes draw the cards in the player's hand
    x0 = width/4
    y0 = 3*height/4 + 10
    for card in ownPlayer.hand:
        if card != None:
            drawCards(screen, x0, y0, card)
            x0 += 20

    # the next six lines of codes draw the cards that the player has equiped as
    # armour
    x0 = 5
    y0 = 3*height/4 + 10
    for armourType in ownPlayer.armour:
        if ownPlayer.armour[armourType] != None:
            drawCards(screen, x0, y0, ownPlayer.armour[armourType])
            x0+=20

    drawCards(screen, 3*width/4 - 100, height - 20, ownPlayer.race)
    drawCards(screen, 3*width/4 - 70, height - 20, ownPlayer.playerClass)

    ONESHOW = (153,225,204)
    TWOSHOW = (153,225,204)
    THREESHOW = (153,225,204)
    if len(playerList) >= 1:
        name1 = playerList[0]['Name']
    if len(playerList) >= 2:
        name2 = playerList[1]['Name']
    if len(playerList) >= 3:
        name3 = playerList[2]['Name']
    
    writeTextCenter(screen, width/2, height - 175, f'Your level is {ownPlayer.level}', (0,0,0), 35, None)

    if player1Show:
        ONESHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[0]['Level']
        writeTextCenter(screen, 450, 40, f'{name1}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[0]['Race'] != None:
            drawCards(screen, 165, 80, playerList[0]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[0]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[0]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[0]['Armour']:
            if playerList[0]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[0]['Armour'][armourPiece])
                x0 += 132

    elif player2Show:
        TWOSHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[1]['Level']
        writeTextCenter(screen, 450, 40, f'{name2}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[1]['Race'] != None:
            drawCards(screen, 165, 80, playerList[1]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[1]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[1]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[1]['Armour']:
            if playerList[1]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[1]['Armour'][armourPiece])
                x0 += 132

    elif player3Show:
        THREESHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[2]['Level']
        writeTextCenter(screen, 450, 40, f'{name3}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[2]['Race'] != None:
            drawCards(screen, 165, 80, playerList[2]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[2]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[2]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[2]['Armour']:
            if playerList[2]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[2]['Armour'][armourPiece])
                x0 += 132


    for numPlayer in range(len(playerList)):
        if numPlayer == 0:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-165),(42,52)))
            pygame.draw.rect(screen, ONESHOW, ((width - 60, height-164),(40,50)))
            writeTextCenter(screen, width-40, height - 164 +20, 'Show', (0,0,0), 15, None)

            if len(name1) > 7:
                name1 = name1[:8]
            writeTextCenter(screen, width-40, height-164+30, f'{name1}', (0,0,0), 15, None)
        elif numPlayer == 1:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-113),(42,52)))
            pygame.draw.rect(screen, TWOSHOW, ((width - 60, height-112),(40,50)))
            writeTextCenter(screen, width-40, height - 112 +20, 'Show', (0,0,0), 15, None)

            if len(name1) > 7:
                name2 = name2[:8]
            writeTextCenter(screen, width-40, height -112 + 30, f'{name2}', (0,0,0), 15, None)
        elif numPlayer == 2:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-61),(42,52)))
            pygame.draw.rect(screen, THREESHOW, ((width - 60, height-60),(40,50)))
            writeTextCenter(screen, width-40, height - 60 +20, 'Show', (0,0,0), 15, None)

            if len(name3) > 7:
                name3 = name3[:8]
            writeTextCenter(screen, width-40, height - 60 + 30, f'{name3}', (0,0,0), 15, None)

def drawBattleCards(screen, width, height, monsterCard, cardsInPlay, 
                    useCardMode, discardPhase, currentTurn, playerList, ownPlayer, player1Show, player2Show, player3Show):

    if currentTurn:
        writeTextCenter(screen, width/2, height/4, 'It\'s Your Turn', (0,0,0), 30, None)
    else:
        writeTextCenter(screen, width/2, height/4, 'It\'s Not Your Turn', (0,0,0), 30, None)

    drawCards(screen, width/2 - 60, height/2 - 100, monsterCard)

    DOORCARDCOLOR = (201,150,99)
    DOORCARDEDGE = (111,82,54)

    TREASURECARDCOLOR = (200,167,114)
    TREASURECARDEDGE = (100,76,53)

    for index in range(len(playerList)):
        font = pygame.font.SysFont(None, 30) 
        if index == 0:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            text = pygame.transform.rotate(text, 270)
            rectText = text.get_rect()
            rectText.center = (80, height/2)
            screen.blit(text, rectText)
            x0 = 0
            y0 = 150

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0, y0),(60, 120)))
                y0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0, y0),(60, 120)))
                y0 += 20

        elif index == 1:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            rectText = text.get_rect()
            rectText.center = (width/2, 80)
            screen.blit(text, rectText)
            x0 = width/4 + 30
            y0 = 0

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0-3,y0),(126, 63)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0, y0),(120, 60)))
                x0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0-3,y0),(126, 63)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0, y0),(120, 60)))
                x0 += 20      

        elif index == 2:
            text = font.render(f"{playerList[index]['Name']}", True, (0,0,0))
            text = pygame.transform.rotate(text, 90)
            rectText = text.get_rect()
            rectText.center = (width - 80, height/2)
            screen.blit(text, rectText)
            x0 = width - 63
            y0 = 150

            for count in range(playerList[index]['DoorCards']):
                pygame.draw.rect(screen, DOORCARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, DOORCARDCOLOR, ((x0+3, y0),(60, 120)))
                y0 += 20
            for count in range(playerList[index]['TreasureCards']):
                pygame.draw.rect(screen, TREASURECARDEDGE, ((x0,y0-3),(63, 126)))
                pygame.draw.rect(screen, TREASURECARDCOLOR, ((x0+3, y0),(60, 120)))
                y0 += 20      

    DRAWDOORCOLOR = (153,225,204)

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 120 - 200, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18 + 120 - 200, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 145 - 200, 14*height/18 + 20, 'Fight', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 145 - 200, 14*height/18 + 30, 'Monster', (0,0,0), 15, None)
    

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, DRAWDOORCOLOR, ((14*width/18, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 20, 'Draw', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 25, 14*height/18 + 30, 'Card', (0,0,0), 15, None)

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

    pygame.draw.ellipse(screen, (0,0,0), ((14*width/18-1 + 60, 14*height/18-1), (52, 52)))
    pygame.draw.ellipse(screen, USECARDCOLOR, ((14*width/18 + 60, 14*height/18), (50, 50)))
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 20, 'Use', (0,0,0), 15, None)
    writeTextCenter(screen, 14*width/18 + 85, 14*height/18 + 30, 'Card', (0,0,0), 15, None)


    # the next five lines of codes draw the cards in the player's hand
    x0 = width/4
    y0 = 3*height/4 + 10
    for card in ownPlayer.hand:
        if card != None:
            drawCards(screen, x0, y0, card)
            x0 += 20

    # the next six lines of codes draw the cards that the player has equiped as
    # armour
    x0 = 5
    y0 = 3*height/4 + 10
    for armourType in ownPlayer.armour:
        if ownPlayer.armour[armourType] != None:
            drawCards(screen, x0, y0, ownPlayer.armour[armourType])
            x0+=20

    drawCards(screen, 3*width/4 - 100, height - 20, ownPlayer.race)
    drawCards(screen, 3*width/4 - 70, height - 20, ownPlayer.playerClass)

    ONESHOW = (153,225,204)
    TWOSHOW = (153,225,204)
    THREESHOW = (153,225,204)
    if len(playerList) >= 1:
        name1 = playerList[0]['Name']
    if len(playerList) >= 2:
        name2 = playerList[1]['Name']
    if len(playerList) >= 3:
        name3 = playerList[2]['Name']
    
    writeTextCenter(screen, width/2, height - 175, f'Your level is {ownPlayer.level}', (0,0,0), 35, None)

    if player1Show:
        ONESHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[0]['Level']
        writeTextCenter(screen, 450, 40, f'{name1}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[0]['Race'] != None:
            drawCards(screen, 165, 80, playerList[0]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[0]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[0]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[0]['Armour']:
            if playerList[0]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[0]['Armour'][armourPiece])
                x0 += 132

    elif player2Show:
        TWOSHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[1]['Level']
        writeTextCenter(screen, 450, 40, f'{name2}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[1]['Race'] != None:
            drawCards(screen, 165, 80, playerList[1]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[1]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[1]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[1]['Armour']:
            if playerList[1]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[1]['Armour'][armourPiece])
                x0 += 132

    elif player3Show:
        THREESHOW = (255,153,255)

        pygame.draw.rect(screen, (0,0,0), ((15,15),(910, 560)))
        pygame.draw.rect(screen, (204,204,255), ((20,20),(900, 550)))
        plevel = playerList[2]['Level']
        writeTextCenter(screen, 450, 40, f'{name3}: level {plevel}', (0,0,0), 35, None)

        writeTextCenter(screen, 225, 60, 'Race', (0,0,0), 30, None)
        if playerList[2]['Race'] != None:
            drawCards(screen, 165, 80, playerList[2]['Race'])
        else:
            writeTextCenter(screen, 225, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 675, 60, 'Player Class', (0,0,0), 30, None)
        if playerList[2]['PlayerClass'] != None:
            drawCards(screen, 615, 80, playerList[2]['PlayerClass'])
        else:
            writeTextCenter(screen, 675, 80, 'None Equipped', (0,0,0), 25, None)

        writeTextCenter(screen, 450, 320, 'Armour', (0,0,0), 30, None)
        x0 = 30
        y0 = 340
        for armourPiece in playerList[2]['Armour']:
            if playerList[2]['Armour'][armourPiece] != None:
                drawCards(screen, x0, y0, playerList[2]['Armour'][armourPiece])
                x0 += 132

    for numPlayer in range(len(playerList)):
        if numPlayer == 0:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-165),(42,52)))
            pygame.draw.rect(screen, ONESHOW, ((width - 60, height-164),(40,50)))
            writeTextCenter(screen, width-40, height - 164 +20, 'Show', (0,0,0), 15, None)

            if len(name1) > 7:
                name1 = name1[:8]
            writeTextCenter(screen, width-40, height-164+30, f'{name1}', (0,0,0), 15, None)
        elif numPlayer == 1:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-113),(42,52)))
            pygame.draw.rect(screen, TWOSHOW, ((width - 60, height-112),(40,50)))
            writeTextCenter(screen, width-40, height - 112 +20, 'Show', (0,0,0), 15, None)

            if len(name1) > 7:
                name2 = name2[:8]
            writeTextCenter(screen, width-40, height -112 + 30, f'{name2}', (0,0,0), 15, None)
        elif numPlayer == 2:
            pygame.draw.rect(screen, (0,0,0), ((width - 61, height-61),(42,52)))
            pygame.draw.rect(screen, THREESHOW, ((width - 60, height-60),(40,50)))
            writeTextCenter(screen, width-40, height - 60 +20, 'Show', (0,0,0), 15, None)

            if len(name3) > 7:
                name3 = name3[:8]
            writeTextCenter(screen, width-40, height - 60 + 30, f'{name3}', (0,0,0), 15, None)

    


    x0 = 150
    y0 = 20
    for playCard in cardsInPlay:
        drawCards(screen, x0, y0, playCard)
        x0+=20

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
    writeTextCenter(screen, width/2, height/2, f'{winner} Wins!!!', (0,0,0), 50, None)
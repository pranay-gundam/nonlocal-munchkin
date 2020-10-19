#############################################
# Author: Pranay Gundam
#############################################

# This file contains some helper functions that are used a lot in all the other
# files
import pygame

def writeTextCenter(screen, cx, cy, text, color, fontSize, fontType):
    font = pygame.font.SysFont(fontType, fontSize) 
    renderText = font.render(text, True, color)
    rectText = renderText.get_rect()
    rectText.center = (cx, cy)
    screen.blit(renderText, rectText)

def writeTextTopLeft(screen, x0, y0, text, color, fontSize, fontType):
    font = pygame.font.SysFont(fontType, fontSize) 
    renderText = font.render(text, True, color)
    rectText = renderText.get_rect()
    rectText.top = y0
    rectText.left = x0
    screen.blit(renderText, rectText)

def drawPicture(screen, cx, cy, dims, picture):
    pictureTrans = pygame.transform.scale(picture, dims)
    pictureRect = pictureTrans.get_rect()
    pictureRect.center = (cx, cy)
    screen.blit(pictureTrans, pictureRect)

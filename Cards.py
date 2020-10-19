#############################################
# Author: Pranay Gundam
#############################################

# this file contains all the code that concerns a card of any kind

import pygame
import random
from HelperFunction import *

# This function formats a string into a list with elements of the proper length
# to fit into a card
def stringFormatting(s):
    formattedList = []
    pastCut = 0
    for index in range(1,len(s)+1):
        if index % 27 == 0 or index == len(s):
            sliced = s[pastCut:index]
            if index < len(s) and s[index].isalpha():
                sliced += '-'
            formattedList.append(sliced)
            pastCut = index
    return formattedList

# This function draws a card based on the type of card that it is.
def drawCards(screen, x0, y0, card):
    if isinstance(card, Monster):
        card.drawMonster(screen, x0, y0)
    elif isinstance(card, Curse):
        card.drawCurse(screen, x0, y0)
    elif isinstance(card, Consumable):
        card.drawConsumable(screen, x0, y0)
    elif isinstance(card, Armour):
        card.drawArmour(screen, x0, y0)
    elif isinstance(card, Race):
        card.drawRace(screen, x0, y0)
    elif isinstance(card, PlayerClass):
        card.drawClass(screen, x0, y0)

#this function returns an instance of an object based on what string it is given
def returnObject(name):
    if name == 'Midterm':
        return Midterm()
    elif name == 'Final':
        return Final()
    elif name == 'Ann':
        return Ann()
    elif name == 'Phi':
        return Phi()
    elif name == 'Kosbie':
        return Kosbie()
    elif name == 'Rahul':
        return Rahul()
    elif name == 'Kian':
        return Kian()
    elif name == 'Alan':
        return Alan()
    elif name == 'Udit':
        return Udit()
    elif name == 'Asad':
        return Asad()
    elif name == 'Dina':
        return Dina()
    elif name == 'Emily':
        return Emily()
    elif name == 'Prithvi':
        return Prithvi()
    elif name == 'Austin':
        return Austin()
    elif name == 'ThunderThighsTaylor':
        return Taylor()
    elif name == 'SmallGroupSessions':
        return SmallGroupSessions()
    elif name == 'OfficeHours':
        return OfficeHours()
    elif name == 'Autolab':
        return Autolab()
    elif name == 'Piazza':
        return Piazza()
    elif name == 'Pass/Fail':
        return PassFail()
    elif name == 'TermProjectGallery':
        return Gallery()
    elif name == 'Schedule':
        return Schedule()
    elif name == 'HomeScreen':
        return HomeScreen()
    elif name == 'Syllabus':
        return Syllabus()
    elif name == 'Map':
        return AMap()
    elif name == 'Loop':
        return ALoop()
    elif name == 'Function':
        return AFunction()
    elif name == 'Set':
        return ASet()
    elif name == 'Tuple':
        return ATuple()
    elif name == 'Dictionary':
        return ADictionary()
    elif name == 'Float':
        return AFloat()
    elif name == 'Int':
        return AInt()
    elif name == 'List':
        return AList()
    elif name == 'String':
        return AString()
    elif name == 'Exception':
        return AException()
    elif name == 'Error':
        return AError()
    elif name == 'Boolean':
        return ABoolean()
    elif name == 'Professor':
        return Professor()
    elif name == 'Dean':
        return Dean()
    elif name == 'Student':
        return Student()
    elif name == 'President':
        return President()
    elif name == 'TA':
        return TA()
    elif name == 'CSBoi':
        return CSBoi()
    elif name == 'TepperBoi':
        return TepperBoi()
    elif name == 'DCBoi':
        return DCBoi()
    elif name == 'CFABoi':
        return CFABoi()
    elif name == 'MCSBoi':
        return MCSBoi()
    elif name == 'HeinzBoi':
        return HeinzBoi()

def returnString(card):
    if isinstance(card, HeinzBoi):
        return 'HeinzBoi'
    elif isinstance(card, MCSBoi):
        return 'MCSBoi'
    elif isinstance(card, DCBoi):
        return 'DCBoi'
    elif isinstance(card, TepperBoi):
        return 'TepperBoi'
    elif isinstance(card, CSBoi):
        return 'CSBoi'
    elif isinstance(card, TA):
        return 'TA'
    elif isinstance(card, President):
        return 'President'
    elif isinstance(card, Student):
        return 'Student'
    elif isinstance(card, Dean):
        return 'Dean'
    elif isinstance(card, Professor):
        return 'Professor'
    elif isinstance(card, ABoolean):
        return 'ABoolean'
    elif isinstance(card, AError):
        return 'AError'
    elif isinstance(card, AException):
        return 'AException'
    elif isinstance(card, AString):
        return 'AString'
    elif isinstance(card, AList):
        return 'AList'
    elif isinstance(card, AInt):
        return 'AInt'
    elif isinstance(card, AFloat):
        return 'AFloat'
    elif isinstance(card, ADictionary):
        return 'ADictionary'
    elif isinstance(card, ATuple):
        return 'ATuple'
    elif isinstance(card, ASet):
        return 'ASet'
    elif isinstance(card, AFunction):
        return 'AFunction'
    elif isinstance(card, ALoop):
        return 'ALoop'
    elif isinstance(card, AMap):
        return 'AMap'
    elif isinstance(card, SmallGroupSessions):
        return 'Small Group Sessions'
    elif isinstance(card, OfficeHours):
        return 'Office Hours'
    elif isinstance(card, Autolab):
        return 'Autolab'
    elif isinstance(card, Piazza):
        return 'Piazza'
    elif isinstance(card, Gallery):
        return 'Gallery'
    elif isinstance(card, PassFail):
        return 'PassFail'
    elif isinstance(card, Schedule):
        return 'Schedule'
    elif isinstance(card, HomeScreen):
        return 'HomeScreen'
    elif isinstance(card, Syllabus):
        return 'Syllabus'
    elif isinstance(card, Midterm):
        return 'Midterm'
    elif isinstance(card, Final):
        return 'Final'
    elif isinstance(card, Ann):
        return 'Ann'
    elif isinstance(card, Phi):
        return 'Phi'
    elif isinstance(card, Kosbie):
        return 'Kosbie'
    elif isinstance(card, Rahul):
        return 'Rahul'
    elif isinstance(card, Kian):
        return 'Kian'
    elif isinstance(card, Alan):
        return 'Alan'
    elif isinstance(card, Udit):
        return 'Udit'
    elif isinstance(card, Asad):
        return 'Asad'
    elif isinstance(card, Taylor):
        return 'Taylor'
    elif isinstance(card, Dina):
        return 'Dina'
    elif isinstance(card, Emily):
        return 'Emily'
    elif isinstance(card, Prithvi):
        return 'Prithvi'
    elif isinstance(card, Austin):
        return 'Austin'

# Each monster has a text description, title, power level, (and attack 
# description, weakness and strength - stuff that I will add in later)
class Monster(object):
    def __init__(self, title, text, power, reward):
        self.description = text
        self.power = power
        self.title = title
        self.reward = reward
    
    def drawMonster(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        monsterCardBg = (192,192,192)
        pygame.draw.rect(screen, monsterCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)

        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)

        #this section draws the power level of the card
        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

class Ann(Monster):
    def __init__(self):
        text = 'Is renown for erasing whiteboards and chalkboards with her bare hands but has stopped recently due to complaints. Known as the god of 112 munchkins.'
        super().__init__('Ann', text, 20, 4)

    # picture from https://www.cs.cmu.edu/~112/staff.html
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('aazhang.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Kosbie(Monster):
    def __init__(self):
        text = 'Will abstain from discussing lecture material to motivate your ass into coding well.'
        super().__init__('Kosbie', text, 17, 2)

    # picture from http://www.kosbie.net/cmu/
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('dkosbie.png').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Phi(Monster):
    def __init__(self):
        text = 'Is a long legged boi, will run his hand through his hair until you faint from his sex appeal.'
        super().__init__('Phi', text, 18, 3)

    # picture from https://www.cs.cmu.edu/~112/staff.html
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('hpnguyen.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Rahul(Monster):
    def __init__(self):
        text = 'Will serenade you with the official 112 violin.'
        super().__init__('Rahul', text, 10, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('raahuja.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Kian(Monster):
    def __init__(self):
        text = 'Is a zappy boi, will electrify you while screaming \"NOOOOOOOOO!\"'
        super().__init__('Kian', text, 8, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('knassre.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Alan(Monster):
    def __init__(self):
        text = 'Is a master of the art of YO-YOs; no one else in the land has mastered this power.'
        super().__init__('Alan', text, 2, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('alanhsu.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Udit(Monster):
    def __init__(self):
        text = 'Known as the mysterious puzzler. Very little other than that is know about him.'
        super().__init__('Udit', text, 3, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('uar.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Asad(Monster):
    def __init__(self):
        text = 'Is commonly known as \"mindfulness\" man and is notorious for killing people with kindness.'
        super().__init__('Asad', text, 12, 2)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('asadalis.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Taylor(Monster):
    def __init__(self):
        text = 'Has a pet dragon-axolotl crossbreed that is known throughout the land as the fierce kimchee.'
        super().__init__('Thunder Thighs Taylor', text, 17, 2)

    # picture from https://www.cmu.edu/news/stories/archives/2017/july/idea-for-good.html
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('mtaylor.png').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

    def __repr__(self):
        return 'ThunderThighsTaylor'

class Dina(Monster):
    def __init__(self):
        text = 'Cool. Cool. Cool. wait, omg help.'
        super().__init__('Dina', text, 7, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('drazek.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Emily(Monster):
    def __init__(self):
        text = 'The pristine boots that she wears will blind you.'
        super().__init__('Emily', text, 5, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('ejzhang.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

class Prithvi(Monster):
    def __init__(self):
        text = 'Using her tech skillz, Prithvi will zoom you to hell.'
        super().__init__('Prithvi', text, 15, 1)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('pokade.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)
    
class Austin(Monster):
    def __init__(self):
        text = 'If you let Austin live long enough, he will evolve into a professor-type demon.'
        super().__init__('Austin', text, 17, 2)

    # picture from https://www.cs.cmu.edu/~112/staff.html    
    def drawMonster(self,screen, x0, y0):
        picture = pygame.image.load('aschick.jpg').convert_alpha()
        super().drawMonster(screen, x0, y0, picture)

monsterList = [Ann(), Phi(), Kosbie(), Rahul(), Kian(), Alan(), Udit(), Asad(),
                Taylor(), Dina(), Emily(), Prithvi(), Austin()]

class Curse(object):
    def __init__(self, title, power, text):
        self.title = title
        self.power = power
        self.description = text
    
    def drawCurse(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        curseCardBg = (192,192,192)
        pygame.draw.rect(screen, curseCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)
    
        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)
        
        #this section draws the power level of the card
        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

class Midterm(Curse):
    def __init__(self):
        text = 'Get cast down from providence with a curse from hell. Suffer minus two from your combat level.'
        super().__init__('Midterm', -3, text)

    # picture from https://www.cs.cmu.edu/~112/schedule.html
    def drawCurse(self, screen, x0, y0):
        picture = pygame.image.load('midterm.png').convert_alpha()
        super().drawCurse(screen, x0, y0, picture)

class Final(Curse):
    def __init__(self):
        text = 'If you thought the last one was harsh then get a load of this.'
        super().__init__('Final', -6, text)

    # picture from https://www.cs.cmu.edu/~112/schedule.html
    def drawCurse(self, screen, x0, y0):
        picture = pygame.image.load('final.png').convert_alpha()
        super().drawCurse(screen, x0, y0, picture)

curseList = [Midterm(), Midterm(), Final(), Final()]

class Consumable(object):
    def __init__(self, title, power, text):
        self.title = title
        self.description = text
        self.power = power

    def drawConsumable(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        curseCardBg = (192,192,192)
        pygame.draw.rect(screen, curseCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)
    
        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)
        
        #this section draws the power level of the card
        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

class SmallGroupSessions(Consumable):
    def __init__(self):
        text = 'Turn TAs onto your side with nothing but a scheduler.'
        super().__init__('Small Group Sessions', 1, text)

    # picture from https://doodle.com/poll/cfgayc4at2epusau
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('smallgroup.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

    def __repr__(self):
        return 'SmallGroupSessions'

class OfficeHours(Consumable):
    def __init__(self):
        text = 'This is your life on Saturdays. Embrace it.'
        super().__init__('Office Hours', 3, text)

    # picture from https://cmu.ohqueue.com/#/courses
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('officehours.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)
    
    def __repr__(self):
        return 'OfficeHours'

class Autolab(Consumable):
    def __init__(self):
        text = 'I dare you to try to cheat.'
        super().__init__('Autolab', 3, text)

    # picture from https://autolab.andrew.cmu.edu/
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('autolab.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

class Piazza(Consumable):
    def __init__(self):
        text = 'MAKE YOUR POSTS PRIVATE'
        super().__init__('Piazza', 2, text)

    # picture from https://piazza.com/class/k4cogezbi4h3jk
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('piazza.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

class Gallery(Consumable):
    def __init__(self):
        text = 'Anxiety Approaches'
        super().__init__('Term Project Gallery', -10, text)

    # picture from https://www.cs.cmu.edu/~112/gallery.html
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('tpgallery.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

    def __repr__(self):
        return 'TermProjectGallery'

class PassFail(Consumable):
    def __init__(self):
        text = 'Effective immediately, all undergraduate and graduate students will be permitted to convert any of your courses to pass/no-pass grading for this semester.'
        super().__init__('Pass/Fail', 10, text)

    # picture from https://www.cmu.edu/alert/coronavirus/communications/mar-16b-2020.html
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('passfail.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

class Schedule(Consumable):
    def __init__(self):
        text = 'It is what it is.'
        super().__init__('Schedule', 1, text)

    # picture from https://www.cs.cmu.edu/~112/schedule.html
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('schedule.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

class HomeScreen(Consumable):
    def __init__(self):
        text = 'What am I even doing'
        super().__init__('Home Screen', 0, text)

    # picture from https://www.cs.cmu.edu/~112/index.html
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('homescreen.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

    def __repr__(self):
        return 'HomeScreen'

class Syllabus(Consumable):
    def __init__(self):
        text = 'Bro, I need more card description ideas.'
        super().__init__('Syllabus', -3, text)

    # picture from https://www.cs.cmu.edu/~112/syllabus.html
    def drawConsumable(self, screen, x0, y0):
        picture = pygame.image.load('homescreen.png').convert_alpha()
        super().drawConsumable(screen, x0, y0, picture)

consumableList = [SmallGroupSessions(), OfficeHours(), Autolab(), 
                  Piazza(), Gallery(), PassFail(),
                  Schedule(), HomeScreen(), Syllabus()]

class Armour(object):
    def __init__(self, title, power, text, armourType):
        self.title = title
        self.description = text
        self.power = power
        self.armourType = armourType
    
    def drawArmour(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        curseCardBg = (192,192,192)
        pygame.draw.rect(screen, curseCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)
    
        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)
        
        #this section draws the power level of the card
        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

# As a note for all Armour subclass objects, a lot of the data type descriptions
# are from https://www.tutorialsteacher.com/python/python-data-types
class ADictionary(Armour):
    def __init__(self):
        text = 'Left Hand: Dictionaries are unordered collections of data in a key:value pair form. A collection of such pairs is enclosed in curly brackets.'
        super().__init__('Dictionary', 2, text, 'LeftH')

    # picture from https://www.collinsdictionary.com/us/dictionary/english/dictionary
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('dictionary.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)    

class AList(Armour):
    def __init__(self):
        text = 'Left Hand: Lists are ordered collections of one or more data items, not necessarily of the same type, put in square brackets.'
        super().__init__('List', 1, text, 'LeftH')

    # picture from https://www.computerhope.com/jargon/l/list.htm
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('list.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AInt(Armour):
    def __init__(self):
        text = 'Right Hand: Ints are positive or negative whole numbers'
        super().__init__('Int', 1, text, 'RightH')

    # picture from https://www.cnn.com/2019/10/17/world/record-breaking-ants-scli-intl-scn/index.html    
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('ant.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AFloat(Armour):
    def __init__(self):
        text = 'Right Hand: Any real number with a floating point representation in which a fractional component is denoted by a decimal symbol or scientific notation'
        super().__init__('Float', 2, text, 'RightH')

    # picture from https://bokunoheroacademia.fandom.com/wiki/Nana_Shimura 
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('float.png').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class ASet(Armour):
    def __init__(self):
        text = 'Boots: Sets are a collection of data types in Python, same as the list and tuple. However, it is not an ordered collection of objects.'
        super().__init__('Set', 1, text, 'Boots')

    # picture from https://www.darkknightarmoury.com/product/edward-steel-armour-set/ 
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('set.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class ATuple(Armour):
    def __init__(self):
        text = 'Boots: A Tuple is a collection of items of any Python data type, same as the list type. Unlike the list, tuple is immutable.'
        super().__init__('Tuple', 2, text, 'Boots')

    # picture from https://www.britannica.com/science/twin0    
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('tuple.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class ABoolean(Armour):
    def __init__(self):
        text = 'Headgear: A boolean is a data type that confers a truthy or falsy value to a variable'
        super().__init__('Boolean', 3, text, 'Headgear')

    # picture from https://en.wikipedia.org/wiki/Love_of_God_in_Christianity   
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('boolean.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AFunction(Armour):
    def __init__(self):
        text = 'Headgear: This doesn\'t belong here'
        super().__init__('Function', 3, text, 'Headgear')

    # picture from https://www.history.com/topics/folklore/history-of-the-devil 
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('function.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AMap(Armour):
    def __init__(self):
        text = 'Chest: Too complicated, nodes and edges.'
        super().__init__('Map', 4, text, 'Chest')

    # picture from https://www.mapsofworld.com/world-map-image.html  
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('map.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class ALoop(Armour):
    def __init__(self):
        text = 'Chest: We go on, and on, and on, and on, and on, and on, and on, and ...'
        super().__init__('Loop', 5, text, 'Chest')

    # picture from https://blog.hubspot.com/blog/tabid/6307/bid/32019/why-every-marketer-needs-closed-loop-reporting.aspx  
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('loop.png').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AException(Armour):
    def __init__(self):
        text = 'Misc: Raise the Roof'
        super().__init__('Exception', 1, text, 'Misc')

    # picture from https://commons.wikimedia.org/wiki/File:NYCS-bull-trans-2.svg   
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('exception.png').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AError(Armour):
    def __init__(self):
        text = 'Misc: The code don\'t work bro'
        super().__init__('Error', 1, text, 'Misc')

    # picture from https://www.amazon.com/Its-My-Life-Dav1d/dp/B07GZCWHSH  
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('error.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

class AString(Armour):
    def __init__(self):
        text = 'Misc: A string is an immutable sequence of Unicode characters. String literals are written by enclosing a sequence of characters in quotes.'
        super().__init__('String', 2, text, 'Misc')

    # picture from https://en.wikipedia.org/wiki/File:Spool_of_string.jpg   
    def drawArmour(self, screen, x0, y0):
        picture = pygame.image.load('string.jpg').convert_alpha()
        super().drawArmour(screen, x0, y0, picture)   

armourList = [AMap(), ALoop(), AFunction(), ASet(), ATuple(),
              ADictionary(), AFloat(), AInt(), AList(), AString(), 
              AException(), AError(), ABoolean()]

class PlayerClass(object):
    def __init__(self, title, text, power):
        self.title = title
        self.description = text
        self.power = power
    
    def drawClass(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        curseCardBg = (192,192,192)
        pygame.draw.rect(screen, curseCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)
        yStart = y0+120

        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)

        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

class Professor(PlayerClass):
    def __init__(self):
        text = 'Professors, some are cool, some are fool, most are poor.'
        super().__init__('Professor', text, 3)

    # picture from https://en.wikipedia.org/wiki/Randy_Pausch#/media/File:RandyPausch_Wiki_2.jpg    
    def drawClass(self, screen, x0, y0):
        picture = pygame.image.load('randypausch.jpg').convert_alpha()
        super().drawClass(screen, x0, y0, picture)

class Student(PlayerClass):
    def __init__(self):
        text = 'the lowest of the low'
        super().__init__('Student', text, 1)

    # picture from https://www.cmu.edu/student-experience/
    def drawClass(self, screen, x0, y0):
        picture = pygame.image.load('undergrad.jpg').convert_alpha()
        super().drawClass(screen, x0, y0, picture)

class TA(PlayerClass):
    def __init__(self):
        text = 'TAs are friends with many of the monsters. Nevertheless, the must still fight them off.'
        super().__init__('TA', text, 2)

    # picture from http://math.cmu.edu/~aremondt/
    def drawClass(self, screen, x0, y0):
        picture = pygame.image.load('TA.jpg').convert_alpha()
        super().drawClass(screen, x0, y0, picture)

class Dean(PlayerClass):
    def __init__(self):
        text = 'Somewhere, I heard only once that Mark Stehlik is an above average kinda guy.'
        super().__init__('Dean', text, 2)

    # picture mode https://www.cmu.edu/dietrich/philosophy/people/faculty/scheines.html
    def drawClass(self, screen, x0, y0):
        picture = pygame.image.load('Dean.jpg').convert_alpha()
        super().drawClass(screen, x0, y0, picture)
    
class President(PlayerClass):
    def __init__(self):
        text = 'Presidents are considered by most to be the ultimate class. They have the power of Thor himself.'
        super().__init__('President', text, 3)

    # picture from https://www.cs.cmu.edu/~farnam/
    def drawClass(self, screen, x0, y0):
        picture = pygame.image.load('president.jpg').convert_alpha()
        super().drawClass(screen, x0, y0, picture)

playerClassList = [Professor(), Professor(), Dean(), Dean(), Student(),
                    Student(), President(), President(), TA(), TA()]

class Race(object):
    def __init__(self, title, text, power):
        self.title = title
        self.description = text
        self.power = power
    
    def drawRace(self, screen, x0, y0, picture):
        pygame.draw.rect(screen, (0,0,0), ((x0-3,y0-3), (126, 206)))
        curseCardBg = (192,192,192)
        pygame.draw.rect(screen, curseCardBg, ((x0,y0), (120, 200)))
        drawPicture(screen, x0+60, y0+60, (100,100), picture)
        yStart = y0 + 120
        stringList = stringFormatting(self.description)
        # the idea for making multiline text was adapted from
        # https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
        for count in range(len(stringList)): 
            line = stringList[count]
            yStart = y0 + 120 + 10*count
            writeTextTopLeft(screen, x0 + 8, yStart, line, (0,0,0), 12, None)

        powerText = f'Power: {self.power}'
        writeTextTopLeft(screen, x0+8, yStart + 10, powerText, (0,0,0), 12, None)

        #draws the title of the card
        writeTextCenter(screen, x0 + 60, y0+5, f'{self.title}', (0,0,0), 15, None)

    def __repr__(self):
        return self.title

class CSBoi(Race):
    def __init__(self):
        text = 'I have a CS friend. He\'s kind of a dumbass to be honest.'
        super().__init__('CS Boi', text, 1)

    # picture from http://www.cs.cmu.edu/~jhclark/logos.htm
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('cslogo.png').convert_alpha()
        super().drawRace(screen, x0, y0, picture)
    
    def __repr__(self):
        return 'CSBoi'

class TepperBoi(Race):
    def __init__(self):
        text = 'I also have a Tepper friend too. He\'s also kind of a dumbass'
        super().__init__('Tepper Boi', text, 3)

    # picture from https://www.cmu.edu/tepper/
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('tepperlogo.png').convert_alpha()
        super().drawRace(screen, x0, y0, picture)
    
    def __repr__(self):
        return 'TepperBoi'

class DCBoi(Race):
    def __init__(self):
        text = 'I am a dietrich boi.'
        super().__init__('Dietrich Boi', text, 4)

    # picture from http://www.stat.cmu.edu/
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('dietrichlogo.png').convert_alpha()
        super().drawRace(screen, x0, y0, picture)

    def __repr__(self):
        return 'DietrichBoi'

class CFABoi(Race):
    def __init__(self):
        text = 'I have a CFA friend as well. She is obsessed - as am I - with the integrity of my water bottle collection.'
        super().__init__('CFA Boi', text, 2)

    # picture from https://www.flickr.com/photos/photo-architect/3511723330
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('cfalogo.jpg').convert_alpha()
        super().drawRace(screen, x0, y0, picture)

    def __repr__(self):
        return 'CFABoi'

class MCSBoi(Race):
    def __init__(self):
        text = 'I feel like the rest of my friends are all in MCS.'
        super().__init__('MCS Boi', text, 1)

    # picture from https://www.cmu.edu/mcs/news-events/2013/index.html
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('mcslogo.jpg').convert_alpha()
        super().drawRace(screen, x0, y0, picture)

    def __repr__(self):
        return 'MCSBoi'

class HeinzBoi(Race):
    def __init__(self):
        text = 'Rip I forgot to add the CIT boi.'
        super().__init__('Heinz Boi', text, 2)

    # picture from https://switchboardhub.org/record/cmu-heinz-college/
    def drawRace(self, screen, x0, y0):
        picture = pygame.image.load('heinzlogo.jpg').convert_alpha()
        super().drawRace(screen, x0, y0, picture)

    def __repr__(self):
        return 'HeinzBoi'

raceList = [CSBoi(), CSBoi(), TepperBoi(), TepperBoi(), DCBoi(), DCBoi(),
            CFABoi(), CFABoi(), MCSBoi(), MCSBoi(), HeinzBoi(), HeinzBoi()]

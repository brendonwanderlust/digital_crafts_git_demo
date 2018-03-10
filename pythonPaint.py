from random import *

def drawTriangle():
    star = '*'
    space = ' '
    tHeight = int(raw_input("Height? "))
    base = (tHeight * 2) - 1
    for row in range(1, tHeight + 1):
        spaces = tHeight - row
        stars = (row * 2) - 1
        print (space * spaces) + (star * stars)

def drawBox():
    star = '*'
    space = ' '
    squareHeight = int(raw_input("Height? "))
    squareWidth = int(raw_input("Width? "))
    for height in range(squareHeight):
        if (height == 0 or height + 1 == squareHeight):
            print star * squareWidth
        else:
            print star + (space * (squareWidth - 2)) + star   

def drawSquare():
    stars = '*****'
    squareSize = int(raw_input("How big of a square would you like? "))
    for x in range(squareSize):
        print stars

def insult():
    insult1 = 'Jesus Christ, do you know how to type?'
    insult2 = 'Hey, dummy! Try selecting a valid response'
    insult3 = 'So, yeeaaaaa....that won\'t work' 
    insultList = [insult1, insult2, insult3]
    print insultList[randint(0, len(insultList) - 1)]


def letsPaint():
    def playAgain():
        replayResponse = raw_input("Would you like to play again? [yes/no] ").lower()
        if replayResponse == 'yes':
            letsPaint()
        elif replayResponse == 'no':
            print "Bye, Felecia! Thanks for playing!"
        else:
            print "Please, type 'yes' or 'no'"
    userChoice = raw_input("Would you like to draw a box, triangle, or square? ").lower()
    if userChoice == 'box':
        drawBox()
    elif userChoice == 'triangle':
        drawTriangle()
    elif userChoice == 'square':
        drawSquare()
    else:
        insult()
        letsPaint()
    playAgain()

letsPaint()
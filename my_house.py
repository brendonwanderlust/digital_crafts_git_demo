from turtle import *

speed(10)
def house():
    for i in range(4):
        if (i % 2 == 0):
            forward(200)
            right(90)
        else:
            forward(100)
            right(90)

def roof():
    seth(30)
    forward(115.47)
    seth(330)
    forward(115.47)

def door():
    seth(270)
    forward(100)
    right(90)
    forward(85)
    right(90)
    forward(75)
    right(90)
    forward(35)
    right(90)
    forward(75)
    right(180)
    forward(25)
    penup()
    left(90)
    forward(5)
    pendown()
    color('black', 'white')
    begin_fill()
    circle(3)
    end_fill()
    penup() 
    right(180)   
    forward(5)
    right(90)
    forward(25)


def firstFloorWindow():
    right(90)
    forward(100)
    up()
    right(90)
    forward(25)
    pendown()
    right(90)
    forward(45)
    left(90)
    forward(35)
    left(90)
    forward(75)
    left(90)
    forward(35)
    left(90)
    forward(30)
    left(180)
    forward(5)
    right(90)
    forward(35)
    right(90)
    forward(25)
    right(90)
    forward(35)
    left(90)
    forward(25)
    left(90)
    forward(17.5)
    left(90)
    forward(75)

house()
roof()
door()
firstFloorWindow()

mainloop()
from turtle import *
from random import randint
from star import *
       

def randomForward():
    forward(randint(5, 150))

def randomHeading():
    seth(randint(0, 360))
    
def numberOfStars(x):
    speed(10)
    for index in range(x):
        penup()
        randomHeading()
        randomForward()
        pendown()
        star(randint(5, 25), "white", "white")
    mainloop()
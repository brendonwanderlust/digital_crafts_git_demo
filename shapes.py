from turtle import *

def square(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

def triangle(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(3):
        forward(size)
        right(120)
    end_fill()
        

def pentagon(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(5):
        forward(size)
        right(72)
    end_fill()

def octogon(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(8):
        forward(size)
        right(45)
    end_fill()

def hexagon(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(6):
        forward(size)
        right(60)
    end_fill()

def star(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()

def circle1(radius, color1, color2):
    color(color2, color1)
    begin_fill()
    circle(radius)
    end_fill()


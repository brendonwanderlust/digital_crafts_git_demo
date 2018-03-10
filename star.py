from turtle import *

def star(size, color1, color2):
    color(color2, color1)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
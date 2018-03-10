from turtle import *

def hexagon(size):
    for i in range(6):
        forward(size)
        right(60)

hexagon(60)

mainloop()
from turtle import *

def octogon(size):
    for i in range(8):
        forward(size)
        right(45)

octogon(100)

mainloop()
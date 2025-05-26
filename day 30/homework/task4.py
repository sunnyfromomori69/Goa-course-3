from turtle import *

def draw_square(x, y, size=100):
    penup()         
    goto(x, y)      
    pendown()       

    for _ in range(4):  
        forward(size)
        right(90)

    done()
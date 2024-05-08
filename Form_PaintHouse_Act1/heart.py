import turtle
import math 
colors = ["pink", "purple"]

def draw_heart(w, h, iteration = 0):

    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2.5)
    a = 0
    t.up()
    t.fillcolor(colors[iteration % len(colors)])
    t.begin_fill()
    while a < 2 * math.pi :
        x = (16 * math.sin(a) ** 3 ) * w
        y = (13 * math.cos(a) -5*math.cos(2*a)-2*math.cos(3*a)-2*math.cos(3*a)-math.cos(4*a)) * h
        t.goto(x,y)
        a+=0.02
        t.down()
    t.end_fill()
    

    #text
    t.up()
    t.setpos(0,0)
    t.write("MICA TROLA <3",align="center",font=("verdana",21,"bold"))
    t.down()
    
    draw_heart(w-3,h-2,iteration+1)
draw_heart(18,15,2)




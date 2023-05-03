#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import turtle as t
import random as r

def sapin():
    t.colormode(255)
    couleur = "brown"
    t.color(couleur)
    t.begin_fill()
    for i in range(3):
        t.fd(10)
        t.left(90)
        t.fd(30)
        t.left(90)
    t.end_fill()

    t.up()
    t.fd(20)
    t.down()
    t.left(-120)
    for j in range(3):
        t.color(120, 194, 64)
        t.begin_fill()
        for x in range(3):
            t.fd(30)
            t.right(120)
        t.end_fill()

        t.fd(30)
        t.up()
        t.left(120)
        t.fd(15)
        t.down()
        t.right(120)
    
    t.right(60)

def bg():
    t.speed(10)
    t.bgcolor("blue")
    t.pencolor("green")
    t.color("green")
    t.begin_fill()
    t.goto(-1000, 0)
    t.goto(-1000,-1000)
    t.goto(1000, -1000)
    t.goto(1000, 0)
    t.goto(0,0)
    t.end_fill()

def start():
    x=r.randint(-1000, 1000)
    y=r.randint(50, 500)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(5)
    t.end_fill()


def maison():
    couleur = "brown"
    t.color(couleur)
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.left(90)
        t.fd(300)
        t.left(90)
    t.end_fill()


#bg()
for i in range(100):
    #start()
    pass

t.up()
t.goto(0,-1000)
t.down()


for i in range(15):
    t.up()
    x=r.randint(-800,800)
    y=r.randint(-300,0)
    t.goto(x,y)
    t.down()
    #sapin()

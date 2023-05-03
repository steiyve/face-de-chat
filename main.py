#creer par nicolas
#creer le 2023-04-26
#dessiner une face de chat

import turtle as t

t.speed(0)
t.pensize(10)
#dessine la partie principale de la face
def face():
    t.color("orange")
    t.begin_fill()
    for i in range(3):
        t.fd(100*2)
        t.right(120)
        print(t.pos())
    t.end_fill()


face()

#dessine l'oreilles droite
t.goto(140,0)
t.begin_fill()
for i in range(3):
    t.fd(60)
    t.left(120)

t.end_fill()

#dessine l'oreilles gauche
t.goto(0,0)
t.begin_fill()
for i in range(3):
    t.fd(60)
    t.left(120)

t.end_fill()


#dessiner leouille gauche
t.penup()
t.goto(50,-50)
t.pendown()
t.color("grey")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(50,-45)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(10)
t.end_fill()

#dessiner leouille droit
t.penup()
t.goto(140,-50)
t.pendown()
t.color("grey")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(140,-45)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(10)
t.end_fill()

#dessiner les moustache
t.penup()
t.goto(90, -70)
t.color("pink")
t.pendown()
t.begin_fill()
for i in range(3):
    t.fd(20)
    t.right(120)
    print(t.pos())
t.end_fill()
t.goto(100, -87.32)
t.right(120)
t.pensize(5)
t.fd(25)
t.penup()
t.goto(90,-70)
t.pendown()
t.goto(100, -87.32)
t.left(60)
t.pensize(5)
t.fd(25)


while (True):
    pass

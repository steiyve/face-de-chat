#creer par nicolas
#creer le 2023-04-26
#dessiner une face de chat

import turtle as t

#dessine la partie principale de la face
def face():
    t.color("orange")
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.right(120)
        print(t.pos())
    t.end_fill()


face()

#dessine l'oreilles droite
t.goto(70,0)
t.begin_fill()
for i in range(3):
    t.fd(30)
    t.left(120)

t.end_fill()

#dessine l'oreilles gauche
t.goto(0,0)
t.begin_fill()
for i in range(3):
    t.fd(30)
    t.left(120)

t.end_fill()


#dessiner leouille gauche
t.penup()
t.goto(30,-30)
t.color("grey")
t.circle(10)

while (True):
    pass

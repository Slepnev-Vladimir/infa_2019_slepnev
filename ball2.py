from tkinter import Tk, Canvas, ALL, BOTH, mainloop, CENTER

from random import randrange as rnd, choice

import math

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
global speed_x, speed_y, x, y, r, color, score, T, dT, speed, ampl, y0
speed_x = [1, 1, 1, 1]  # the speed of the individual object
speed_y = [1, 1, 1, 1]
x = [0, 0, 0, 0]        # the coordinate of an individual object
y = [0, 0, 0, 0]

y0 = [0, 0, 0, 0]       # the trajectory of a super object is
ampl = [0, 0, 0, 0]     # ampl * Sin(ax) + y0, where a is some constant

r = [0, 0, 0, 0]        # the radius
color = [0, 0, 0, 0]

score = 0
T = 5000                # the lifetame of all objects, ms
dT = 0
speed = 30              # the speed of all objects


# creating objects


def appearsup(numb):
    """responsible for creating a super object"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    x[numb] = rnd(100, 700)
    y0[numb] = rnd(100, 500)
    r[numb] = rnd(20, 40)
    ampl[numb] = rnd(100, 200)
    color[numb] = choice(colors)
    canv.create_rectangle(
            x[numb] - r[numb],
            y0[numb] - r[numb],
            x[numb] + r[numb],
            y0[numb] + r[numb],
            fill=color[numb],
            width=0)


def appear(numb):
    """responsible for creating an object"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    x[numb] = rnd(100, 700)
    y[numb] = rnd(100, 500)
    r[numb] = rnd(30, 50)
    color[numb] = choice(colors)
    canv.create_oval(
            x[numb] - r[numb],
            y[numb] - r[numb],
            x[numb] + r[numb],
            y[numb] + r[numb],
            fill=color[numb],
            width=0)


def new_ball():
    """responsible for creating"""
    global score
    canv.delete(ALL)
    canv.create_text(100, 100, text=score, justify=CENTER, font="Verdana 100")
    appear(0)
    appear(1)
    appear(2)
    appearsup(3)
    root.after(T, new_ball)
    if score > 3:
        score -= 3


# moving objects


def brainsup(numb):
    """responsible for calculation a super object trajectory"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    if x[numb] > 700 or x[numb] < 100:
        speed_x[numb] *= -1

    x[numb] += 3 * speed * dT / T * speed_x[numb]
    y[numb] = ampl[numb] * math.sin(3 * x[numb] / ampl[numb]) + y0[numb]

    if y[numb] < 100:
        y[numb] = 200 - y[numb]

    if y[numb] > 500:
        y[numb] = 1000 - y[numb]

    canv.create_rectangle(
            x[numb] - r[numb],
            y[numb] - r[numb],
            x[numb] + r[numb],
            y[numb] + r[numb],
            fill=color[numb],
            width=0)
    canv.create_text(100, 100, text=score, justify=CENTER, font="Verdana 100")


def brain(numb):
    """responsible for calculation an object trajectory"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    if x[numb] > 700 or x[numb] < 100:
        speed_x[numb] *= rnd(1, 10) / (-5)

    if y[numb] > 500 or y[numb] < 100:
        speed_y[numb] *= -1

    x[numb] += speed * dT / T * speed_x[numb]
    y[numb] += speed * dT / T * speed_y[numb]

    canv.create_oval(
            x[numb] - r[numb],
            y[numb] - r[numb],
            x[numb] + r[numb],
            y[numb] + r[numb],
            fill=color[numb],
            width=0)
    canv.create_text(100, 100, text=score, justify=CENTER, font="Verdana 100")


def move():
    """responsible for movement"""
    canv.delete(ALL)
    brain(0)
    brain(1)
    brain(2)
    brainsup(3)
    canv.create_text(100, 100, text=score, justify=CENTER, font="Verdana 100")
    root.after(50, move)


# players actions


def check(numb, event):
    """responsible for checking the hit in the object"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    global score, dT

    if (event.x - x[numb]) ** 2 + (event.y - y[numb]) ** 2 < r[numb] ** 2:
        score += 1
        dT = 10 * score
        canv.delete(ALL)
        appear(numb)


def checksup(numb, event):
    """responsible for checking the hit in the super object"""
    """BE CAREFUL!"""
    """don't use supfunctions and not supfunctions for the same object"""
    global score, dT

    if abs(event.x - x[numb]) + abs(event.y - y[numb]) < 2 * r[numb]:
        score += 3
        dT = 10 * score
        canv.delete(ALL)
        appearsup(numb)


def click(event):
    """responsible for the actions of the player"""
    check(0, event)
    check(1, event)
    check(2, event)
    checksup(3, event)
    canv.delete(ALL)
    canv.create_text(100, 100, text=score, justify=CENTER, font="Verdana 100")


new_ball()
move()
canv.bind('<Button-1>', click)
mainloop()

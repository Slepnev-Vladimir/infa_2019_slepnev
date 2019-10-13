from tkinter import Tk, Canvas, ALL, BOTH, mainloop, CENTER

from random import randrange as rnd, choice

import math

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
global dirx, diry, x, y, r, color, i, T, dT, V, ampl, y0
dirx = [1, 1, 1, 1]
diry = [1, 1, 1, 1]
x = [0, 0, 0, 0]
y = [0, 0, 0, 0]
y0 = [0, 0, 0, 0]
r = [0, 0, 0, 0]
color = [0, 0, 0, 0]
ampl = [0, 0, 0, 0]
i = 0
T = 5000
dT = 0
V = 30


def appearsup(numb):
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


def brainsup(numb):
    if x[numb] > 700 or x[numb] < 100:
        dirx[numb] *= -1

    x[numb] += 3 * V * dT / T * dirx[numb]
    canv.create_text(100, 100, text=i, justify=CENTER, font="Verdana 100")
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


def brain(numb):
    if x[numb] > 700 or x[numb] < 100:
        dirx[numb] *= -1

    if y[numb] > 500 or y[numb] < 100:
        diry[numb] *= -1

    x[numb] += V * dT / T * dirx[numb]
    canv.create_text(100, 100, text=i, justify=CENTER, font="Verdana 100")
    y[numb] += V * dT / T * diry[numb]
    canv.create_oval(
            x[numb] - r[numb],
            y[numb] - r[numb],
            x[numb] + r[numb],
            y[numb] + r[numb],
            fill=color[numb],
            width=0)


def appear(numb):
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


def move():
    canv.delete(ALL)
    brain(0)
    brain(1)
    brain(2)
    brainsup(3)
    canv.create_text(100, 100, text=i, justify=CENTER, font="Verdana 100")
    root.after(50, move)


def new_ball():
    global i
    canv.delete(ALL)
    canv.create_text(100, 100, text=i, justify=CENTER, font="Verdana 100")
    appear(0)
    appear(1)
    appear(2)
    appearsup(3)
    root.after(T, new_ball)
    if i > 3:
        i -= 3


def check(numb, event):
    global i, dT

    if (event.x - x[numb]) ** 2 + (event.y - y[numb]) ** 2 < r[numb] ** 2:
        i += 1
        dT = 10 * i
        canv.delete(ALL)
        appear(numb)


def checksup(numb, event):
    global i, dT

    if abs(event.x - x[numb]) + abs(event.y - y[numb]) < 2 * r[numb]:
        i += 3
        dT = 10 * i
        canv.delete(ALL)
        appearsup(numb)


def click(event):
    check(0, event)
    check(1, event)
    check(2, event)
    checksup(3, event)
    canv.delete(ALL)
    canv.create_text(100, 100, text=i, justify=CENTER, font="Verdana 100")


new_ball()
move()
canv.bind('<Button-1>', click)
mainloop()

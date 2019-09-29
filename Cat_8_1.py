from graph import *

import math

def blik (x0, y0, szx, szy):
    "dlya glaza. (x0; y0) - koordinati verha"

    penColor ("white")
    brushColor("white")
    points = []
    points.append ((x0, y0))
    points.append ((x0 + 0.5 * szx, y0))
    points.append ((x0 + 1.1 * szx, y0 + 0.6 * szy))
    points.append ((x0 + 1.5 * szx, y0 + szy))
    points.append ((x0 + 1.9 * szx, y0 + 2.0 * szy))
    points.append ((x0 + 1.9 * szx, y0 + 2.4 * szy))
    points.append ((x0 + 1.4 * szx, y0 + 2.4 * szy))
    points.append ((x0 + 0.7 * szx, y0 + 1.7 * szy))
    points.append ((x0, y0 + 0.4 * szy))
    points.append ((x0, y0))
    return polygon(points)

def cat (x0, y0, szx, szy):
    "(x0; y0) - koordinati konchika yha"
    
    penColor("black")
    brushColor(200,113,55)

    "hvost"
    points = []
    points.append((70 * szx + x0, 21 * szy + y0))
    points.append((76 * szx + x0, 24 * szy + y0))
    points.append((82 * szx + x0, 27 * szy + y0))
    points.append((85 * szx + x0, 28 * szy + y0))
    points.append((91 * szx + x0, 28.5 * szy + y0))
    points.append((93 * szx + x0, 28 * szy + y0))
    points.append((94.5 * szx + x0, 26 * szy + y0))
    points.append((95 * szx + x0, 24 * szy + y0))
    points.append((94 * szx + x0, 21.5 * szy + y0))
    points.append((92 * szx + x0, 18.5 * szy + y0))
    points.append((90 * szx + x0, 16.5 * szy + y0))
    points.append((84 * szx + x0, 13 * szy + y0))
    points.append((77 * szx + x0, 10 * szy + y0))
    points.append((70 * szx + x0, 8 * szy + y0))
    points.append((62 * szx + x0, 6 * szy + y0))
    polygon(points)

    "telo"
    circle_base = circle(374, 668, 250)
    changeCoords(circle_base, [(11 * szx + x0, -2 * szy + y0), (69 * szx + x0, 29 * szy + y0)])

    "lapa 1"
    circle_base = circle(191, 777, 70)
    changeCoords(circle_base, [(6 * szx + x0, 17 * szy + y0), (13 * szx + x0, 26 * szy + y0)])

    "lapa 2"
    circle_base = circle(98, 723, 100)
    changeCoords(circle_base, [(13 * szx + x0, 22 * szy + y0), (27 * szx + x0, 30 * szy + y0)])

    "lapa 3"
    circle(60 * szx + x0, 22 * szy + y0, 10 * szy)
    circle_base = circle(621, 826, 80)
    changeCoords(circle_base, [(66 * szx + x0, 24 * szy + y0), (73 * szx + x0, 40 * szy + y0)])

    "golova"
    circle_base = circle(132, 646, 100)
    changeCoords(circle_base, [(0.8 * szx + x0, 0.6 * szy + y0),
    (25.6 * szx + x0, 22.6 * szy + y0)])

    "yshi"
    polygon([(x0, y0), (6.4 * szx + x0, 3 * szy + y0), (1.8 * szx + x0, 8 * szy + y0)])
    polygon([(23.8 * szx + x0, -1 * szy + y0), (17.8 * szx + x0, 2.6 * szy + y0),
    (22.6 * szx + x0, 7.4 * szy + y0)])

    penSize(0.5)
    brushColor(222,170,135)
    polygon([(szx + x0, szy + y0), (5.4 * szx + x0, 3 * szy + y0),
    (2.2 * szx + x0, 6.6 * szy + y0)])
    polygon([(23 * szx + x0, y0), (18.6 * szx + x0, 2.8 * szy + y0),
    (22.4 * szx + x0, 6 * szy + y0)])

    "glaza"
    penSize(1)
    brushColor(136,170,0)
    circle(8 * szx + x0, 12.6 * szy + y0, 3 * szy)
    circle(18.6 * szx + x0 , 12.6 * szy + y0, 3 * szy)

    "zrachki"
    brushColor("black")
    circle_base = circle(185, 646, 30)
    changeCoords(circle_base, [(8.4 * szx + x0, 9.5 * szy + y0),
    (9.2 * szx + x0, 15.5 * szy + y0)])
    circle_base = circle(185, 646, 30)
    changeCoords(circle_base, [(19 * szx + x0, 9.5 * szy + y0),
    (19.8 * szx + x0, 15.5 * szy + y0)])

    "bliki"
    blik(6.6 * szx + x0, 10 * szy + y0, 0.9 * szx, 0.9 * szy)
    blik(17.2 * szx + x0, 10 * szy + y0, 0.9 * szx, 0.9 * szy)

    "nos"
    penColor("black")
    brushColor(222, 170, 135)
    polygon([(12 * szx + x0, 16.6 * szy + y0), (14.2 * szx + x0, 16.6 * szy + y0),
    (13.2 * szx + x0, 17.8 * szy + y0)])

    "rot"
    points = []
    points.append((13.2 * szx + x0, 17.8 * szy + y0))
    points.append((13.2 * szx + x0, 19.4 * szy + y0))
    points.append((12.6 * szx + x0, 20.2 * szy + y0))
    points.append((11.6 * szx + x0, 20.2 * szy + y0))
    points.append((11.4 * szx + x0, 20 * szy + y0))
    polyline(points)

    points = []
    points.append((13.2 * szx + x0, 19.4 * szy + y0))
    points.append((13.8 * szx + x0, 20.2 * szy + y0))
    points.append((14.8 * szx + x0, 20.2 * szy + y0))
    points.append((15 * szx + x0, 20 * szy + y0))
    polyline(points)

    "ysi"
    points = []
    points.append((16.4 * szx + x0, 17.8 * szy + y0))
    points.append((21.8 * szx + x0, 16.8 * szy + y0))
    points.append((27 * szx + x0, 16.2 * szy + y0))
    points.append((31.2 * szx + x0, 16.8 * szy + y0))
    polyline(points)

    points = []
    points.append((16.4 * szx + x0, 18.4 * szy + y0))
    points.append((21.4 * szx + x0, 17.8 * szy + y0))
    points.append((26.8 * szx + x0, 17.8 * szy + y0))
    points.append((31.2 * szx + x0, 18.6 * szy + y0))
    polyline(points)

    points = []
    points.append((16.4 * szx + x0, 19 * szy + y0))
    points.append((21.6 * szx + x0, 19 * szy + y0))
    points.append((27 * szx + x0, 19.8 * szy + y0))
    points.append((31 * szx + x0, 21 * szy + y0))
    polyline(points)

    points = []
    points.append((10 * szx + x0, 17.8 * szy + y0))
    points.append((4.6 * szx + x0, 16.8 * szy + y0))
    points.append((-0.6 * szx + x0, 16.2 * szy + y0))
    points.append((-4.8 * szx + x0, 16.8 * szy + y0))
    polyline(points)

    points = []
    points.append((10 * szx + x0, 18.4 * szy + y0))
    points.append((5 * szx + x0, 17.8 * szy + y0))
    points.append((-0.4 * szx + x0, 17.8 * szy + y0))
    points.append((-4.8 * szx + x0, 18.6 * szy + y0))
    polyline(points)

    points = []
    points.append((10 * szx + x0, 19 * szy + y0))
    points.append((4.8 * szx + x0, 19 * szy + y0))
    points.append((-0.6 * szx + x0, 19.8 * szy + y0))
    points.append((-4.6 * szx + x0, 21 * szy + y0))
    polyline(points)

def ball(x0, y0, szx, szy):
    "(x0; y0) - koordinati centra klybka"
    
    penSize(1)
    penColor("black")
    brushColor(153,153,153)
    circle(x0, y0, -10.2 * szy)

    "polosi na share (sverhy vniz)"
    points = []
    points.append((2 * szx + x0, -6.6 * szy + y0))
    points.append((5.8 * szx + x0, -4.6 * szy + y0))
    points.append((8 * szx + x0, -1.2 * szy + y0))
    points.append((8.6 * szx + x0, 3.4 * szy + y0))
    polyline(points)

    points = []
    points.append((-3.6 * szx + x0, -6.8 * szy + y0))
    points.append((1.4 * szx + x0, -4 * szy + y0))
    points.append((5.2 * szx + x0, -1.8 * szy + y0))
    points.append((7.4 * szx + x0, 4.6 * szy + y0))
    polyline(points)

    points = []
    points.append((-6 * szx + x0, -5 * szy + y0))
    points.append((0.6 * szx + x0, -3.2 * szy + y0))
    points.append((4.8 * szx + x0, 1.2 * szy + y0))
    points.append((6.4 * szx + x0, 6.6 * szy + y0))
    polyline(points)

    points = []
    points.append((-2.6 * szx + x0, -0.8 * szy + y0))
    points.append((-3.6 * szx + x0, -0.4 * szy + y0))
    points.append((-5 * szx + x0, 3 * szy + y0))
    points.append((-5 * szx + x0, 6.4 * szy + y0))
    polyline(points)

    points = []
    points.append((0.2 * szx + x0, -0.8 * szy + y0))
    points.append((-2 * szx + x0, 2 * szy + y0))
    points.append((-3 * szx + x0, 4.4 * szy + y0))
    points.append((-3 * szx + x0, 7.6 * szy + y0))
    polyline(points)

    points = []
    points.append((3.2 * szx + x0, 1.6 * szy + y0))
    points.append((1.4 * szx + x0, 3.4 * szy + y0))
    points.append((0.8 * szx + x0, 5.6 * szy + y0))
    points.append((0.8 * szx + x0, 8.6 * szy + y0))
    polyline(points)

    "nitka (zatyhayshaya sinysoida)"
    X0 = -37.4 * szx + x0;
    Y0 = 7.4 * szy + y0
    k = 0.4 * szx #      masshtab
    Ps = 80 #             razmer massiva
    f = 3 #               chastota kolebaniy
    x = 1;
    xmax = Ps; #          diapazon po x
    h = 1 #               shag po х
    points = []
    
    while x <= xmax:
        y = math.sin(2 * math.pi * f *(x / Ps)) / (x / Ps)
        xe = X0 + k * x
        ye = Y0 + k * y
        points.append((xe, ye))
        x += h

    penSize(2)
    penColor(153,153,153)
    polyline(points)

def window(x1, y1, x2, y2):
    penColor(255,255,255)
    brushColor(255,255,255)
    rectangle(x1, y1, x2, y2)

    penColor(0,231,255)
    brushColor(141,207,255)
    rectangle(0.95 * x1 + 0.05 * x2, 0.95 *y1 + 0.05 * y2,
    0.55 * x1 + 0.45 * x2, 0.75 * y1 + 0.25 * y2)

    penColor(0,231,255)
    brushColor(141,207,255)
    rectangle(0.45 * x1 + 0.55 * x2, 0.95 *y1 + 0.05 * y2,
    0.05 * x1 + 0.95 * x2, 0.75 * y1 + 0.25 * y2)

    penColor(0,231,255)
    brushColor(141,207,255)
    rectangle(0.95 * x1 + 0.05 * x2, 0.67 *y1 + 0.33 * y2,
    0.55 * x1 + 0.45 * x2, 0.05 * y1 + 0.95 * y2)

    penColor(0,231,255)
    brushColor(141,207,255)
    rectangle(0.45 * x1 + 0.55 * x2, 0.67 *y1 + 0.33 * y2,
    0.05 * x1 + 0.95 * x2, 0.05 * y1 + 0.95 * y2)

windowSize(500,650)

penColor(85,68,0)
brushColor(85,68,0)
rectangle(0, 0, 500, 200)

penColor(128,102,0)
brushColor(128,102,0)
rectangle(0, 200, 500, 650)

window(250, 15, 450, 185)
cat(8, 216, 5, 5)
ball(274, 467, 5, 5)

run()

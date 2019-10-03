import math

M = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
x01 = M[0][0]
x02 = M[1][0]
x03 = M[2][0]
x04 = M[3][0]
y01 = M[0][1]
y02 = M[1][1]
y03 = M[2][1]
y04 = M[3][1]
angle = math.pi / 4
xc = (x01 + x03) / 2
yc = (y01 + y03) / 2
R = ((xc - x01) ** 2 + (yc - y01) ** 2) ** 0.5
i = 0

while i < 4:
    j = 0
    p = 0

    while j < 2:
        if M[i][j] > 0:
            p += 1

        j += 1
    
    if p == 2:
        nxp = i
        nyp = j

    i += 1

angle0 = math.acos(M[nxp][0] / R)
angle_new = angle - angle0
Mn = [(R * math.cos(angle_new),
       R * math.sin(angle_new)),
      (R * math.cos(angle_new + math.pi / 2),
       R * math.sin(angle_new + math.pi / 2)),
      (R * math.cos(angle_new + math.pi),
       R * math.sin(angle_new + math.pi)),
      (R * math.cos(angle_new + 3 * math.pi / 2),
       R * math.sin(angle_new + 3 * math.pi / 2))]

print(Mn)



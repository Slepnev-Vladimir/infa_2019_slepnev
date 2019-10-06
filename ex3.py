import math

M = [(5, 4), (4, 3), (3, 4), (4, 5)]
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

    if M[i][0] - xc >= 0:
        p += 1

    if M[i][1] - yc >= 0:
        p += 1

    if p == 2:
        nxp = i
        nyp = j

    i += 1

angle0 = math.acos((M[nxp][0] - xc) / R)
angle_new = angle - angle0
Mn = [(R * math.cos(angle_new) + xc,
       R * math.sin(angle_new) + yc),
      (R * math.cos(angle_new + math.pi / 2) + xc,
       R * math.sin(angle_new + math.pi / 2) + yc),
      (R * math.cos(angle_new + math.pi) + xc,
       R * math.sin(angle_new + math.pi) + yc),
      (R * math.cos(angle_new + 3 * math.pi / 2) + xc,
       R * math.sin(angle_new + 3 * math.pi / 2) + yc)]

print(Mn)

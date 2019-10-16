# program contains a function that rotates a square by a given angle

import math

square = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
angle = math.pi / 8


def rotate_square(square, angle):
    x01 = square[0][0]
    x03 = square[2][0]
    y01 = square[0][1]
    y03 = square[2][1]
    x_center = (x01 + x03) / 2
    y_center = (y01 + y03) / 2
    R = ((x_center - x01) ** 2 + (y_center - y01) ** 2) ** 0.5  # radius of the circumscribed circle
    angle0 = math.acos((x01 - x_center) / R)                    # angle between r(x0, y0) vector and OX
    angle_new = angle - angle0
    rotated = [(R * math.cos(angle_new) + x_center,
                R * math.sin(angle_new) + y_center),
               (R * math.cos(angle_new + math.pi / 2) + x_center,
                R * math.sin(angle_new + math.pi / 2) + y_center),
               (R * math.cos(angle_new + math.pi) + x_center,
                R * math.sin(angle_new + math.pi) + y_center),
               (R * math.cos(angle_new + 3 * math.pi / 2) + x_center,
                R * math.sin(angle_new + 3 * math.pi / 2) + y_center)]
    return(rotated)


print(rotate_square(square, angle))

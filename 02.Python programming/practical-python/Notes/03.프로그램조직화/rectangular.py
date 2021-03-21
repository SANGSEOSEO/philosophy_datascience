from math import cos, sin
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y


def rectangular_t(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)

    return x, y
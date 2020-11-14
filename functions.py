from math import*

def f(x, y):
    return 1/cos(x) - y * tan(x)

def const(x, y):
    return (y - sin(x))/cos(x)

def y(x, x0, y0):
    return sin(x) + const(x0, y0)*cos(x)



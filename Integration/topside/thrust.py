from math import sqrt

# deadzone radii

d_s = 0.155
d_t = 0.125

t_sens = 1.0

u = 0
v = 0
j = 0

def thrust_vectoring(x, y, turn):
    if x**2 + y**2 <= d_s**2:
        u = 0
    else:
        u = (sqrt(x**2 + y**2) - d_s)/(1 - d_s)
    if y >= 0:
        if x < 0:
            u *= (y + x)/(y - x)
    else:
        if x >= 0:
            u *= (x + y)/(x - y)
        else:
            u = -u
    # print (str(u) + " such")

    if x**2 + y**2 <= d_s**2:
        v = 0
    else:
        v = (sqrt(x**2 + y**2) - d_s)/(1 - d_s)
    if y > 0:
        if x >= 0:
            v *= (y - x)/(y + x)
    else:
        if x >= 0:
            v = -v
        else:
            v *= (x - y)/(x + y)
    # print (str(v) + " such")

    if abs(turn) > d_t:
        j = t_sens * (turn / abs(turn)) * (abs(turn) - d_t) / (1 - d_t)
    else:
        j = 0
    # print (str(j) + " such")

    T = (((v - j) / abs(v - j)) if abs(v - j) >= 1 else (v - j), ((u + j) / abs(u + j)) if abs(u + j) >= 1 else (u + j), ((v + j) / abs(v + j)) if abs(v + j) >= 1 else (v + j), ((u - j) / abs(u - j)) if abs(u - j) >= 1 else (u - j))

    return T

import math

# deadzone radii
DR = 0.155
DR_TURN = 0.126
# sensitivity
SENSITIVITY = 1

def sgn(x):
    if x >= 0:
        return 1
    return -1

def get_turn(x):
    if abs(x) > DR_TURN:
        turn = SENSITIVITY * sgn(x) * (abs(x) - DR_TURN) / (1 - DR_TURN)
        return turn
    return 0

def get_thrust(u, v, turn):
    T = [sgn(v - turn) * min(1, abs(v - turn)), sgn(u + turn) * min(1, abs(u + turn)), sgn(v + turn) * min(1, abs(v + turn)), sgn(u - turn) * min(1, abs(u - turn))]
    return T

# returns (fr, fl, bl, br)
def uniform_thrust_vectoring(x, y, turn_x = 0):
    radius = math.sqrt(x**2 + y**2)
    # handling invalid input
    bad = []
    if abs(x) > 1:
        bad.append("left/right thruster movement")
    if abs(y) > 1:
        bad.append("up/down thruster movement")
    if abs(y) > 1:
        bad.append("turning movement")
    if len(bad) > 0:
        raise ValueError(f"{bad} must be in the range [-1, 1]")
    # deadzoning
    if radius < DR:
        return (0, 0)

    angle = math.pi / 2
    if x != 0:
        angle = math.atan(y / x)
    u = radius * math.cos(angle - (math.pi / 4))
    v = radius * math.sin(angle - (math.pi / 4))
    turn = get_turn(turn_x)
    T = get_thrust(u, v, turn)
    return T
    #return u, v

# returns (fr, fl, bl, br)
def maximized_thrust_vectoring(x, y, turn_x = 0):
    radius = math.sqrt(x**2 + y**2)
    # handling invalid input
    bad = []
    if abs(x) > 1:
        bad.append("left/right thruster movement")
    if abs(y) > 1:
        bad.append("up/down thruster movement")
    if abs(y) > 1:
        bad.append("turning movement")
    if len(bad) > 0:
        raise ValueError(f"{bad} must be in the range [-1, 1]")
    # deadzoning
    if radius <= DR:
        return (0, 0, 0, 0)

    u = (radius - DR) / (1 - DR)
    if sgn(x) == sgn(y):
        u *= sgn(x)
    else:
        u *= (x + y) / (x - y) * sgn(x)
    v = (radius - DR) / (1 - DR)
    if sgn(x) == sgn(y):
        v *= (y - x) / (x + y) * sgn(x)
    else:
        v *= sgn(y)
    turn = get_turn(turn_x)
    T = get_thrust(u, v, turn)
    return T[0], T[1], T[2], T[3]
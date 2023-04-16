import pygame
import thrust
import atexit
import time

LEFT_JOYSTICK_X = 0
LEFT_JOYSTICK_Y = 1
RIGHT_JOYSTICK_X = 2
RIGHT_JOYSTICK_Y = 3


pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)

def _stop():
    controller.quit()

atexit.register(_stop)

def decode_controller_input():
    pygame.event.pump()
    x = round(controller.get_axis(RIGHT_JOYSTICK_X), 2)
    y = -round(controller.get_axis(RIGHT_JOYSTICK_Y), 2)
    turn = round(controller.get_axis(LEFT_JOYSTICK_X), 2)
    vert = -round(controller.get_axis(LEFT_JOYSTICK_Y), 2)

    (fr, fl, bl, br) = thrust.maximized_thrust_vectoring(x, y, turn) # No need for assignment here just have it to remember what it returns
    return (fr, fl, bl, br, vert)

if __name__ == '__main__':
    # while True:
    #     (fr, fl, bl, br) = decode_controller_input()
    #     print(f"{fl} {fr}\n{bl} {br}\n")
    #     time.sleep(1)
    pass
import pygame
import thrust
import atexit

LEFT_JOYSTICK_X = 0
LEFT_JOYSTICK_Y = 1
RIGHT_JOYSTICK_X = 2
RIGHT_JOYSTICK_Y = 3

GAMEPAD_RIGHT = 14
GAMEPAD_LEFT = 13
GAMEPAD_UP = 11
GAMEPAD_DOWN = 12

A_BUTTON = 0
B_BUTTON = 1
X_BUTTON = 2
Y_BUTTON = 3

CAMERA_TURN = 1
ARM_SPIN = 1
CLAW_PERCENT = 0.1

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)

def _stop():
    controller.quit()

atexit.register(_stop)

def decode_controller_input():
    pygame.event.pump()

    # THRUSTER CONTROL
    x = round(controller.get_axis(RIGHT_JOYSTICK_X), 2)
    y = -round(controller.get_axis(RIGHT_JOYSTICK_Y), 2)
    turn = round(controller.get_axis(LEFT_JOYSTICK_X), 2)
    vert = -round(controller.get_axis(LEFT_JOYSTICK_Y), 2)

    # CAMERA CONTROL
    camera = 0
    if controller.get_button(GAMEPAD_RIGHT):
        camera = CAMERA_TURN
    elif controller.get_button(GAMEPAD_LEFT):
        camera = -CAMERA_TURN

    # ARM CONTROL
    arm_angle = 0
    claw = 0
    if controller.get_button(B_BUTTON):
        arm_angle = ARM_SPIN
    elif controller.get_button(X_BUTTON):
        arm_angle = -ARM_SPIN
    
    if controller.get_button(Y_BUTTON):
        claw = CLAW_PERCENT
    elif controller.get_button(A_BUTTON):
        claw = -CLAW_PERCENT

    (fr, fl, bl, br) = thrust.thrust_vectoring(x, y, turn)
    return (-fr, -fl, bl, br, -vert, camera, claw, arm_angle)

# A: 0
# B: 1
# X: 2
# Y: 3
# GR: 14
# GL: 13
# GU: 11
# GD: 12
# RB: 10
# LB: 9

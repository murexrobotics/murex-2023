import pygame
from pygame.locals import *
import numpy as np
import thrust

pygame.init()

pygame.joystick.init()
pygame.joystick.Joystick(0).init()

def controller():
    joystick = pygame.joystick.Joystick(0)
    # front-right, front-left, back-left, back-right, front-up, back-up, arm1, arm2, claw, camerax, cameray
    array = np.empty(11, dtype = bytes)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        strafe = thrust.uniform_thrust_vectoring(joystick.get_axis(2), joystick.get_axis(3), turn_x = joystick.get_axis(0))
        for i in range(len(strafe)):
            array[i] = int(strafe[i] * 100 + 100).to_bytes()
        array[4] = array[5] = int(-(joystick.get_axis(1)) * 100 + 100).to_bytes()

        temp = 0
        if joystick.get_axis(4) >= 0.4:
            temp = 1
        else:
            temp = 0
        array[6] = int((joystick.get_button(4) - temp) * 100 + 100).to_bytes()

        if joystick.get_axis(5) >= 0.4:
            temp = 1
        else:
            temp = 0
        array[7] = int((joystick.get_button(5) - temp) * 100 + 100).to_bytes()

        array[8] = int((joystick.get_button(2) - joystick.get_button(3)) * 100 + 100).to_bytes()

        array[9] = int(joystick.get_hat(0)[0] * 100 + 100).to_bytes()

        array[10] = int(joystick.get_hat(0)[1] * 100 + 100).to_bytes()

        string = ""
        for n in range(len(array)):
            string += str((int.from_bytes(array[n]) - 100) / 100) + " "
        print(string)
if __name__ == "__main__":
    controller()
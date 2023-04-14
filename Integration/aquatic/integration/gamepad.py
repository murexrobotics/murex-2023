import logging
import numpy as np


class Gamepad():
    def __init__(self):
        logging.info("Initializing Gamepad")
        self._hid_code = None
        self._game_state = None
        self._left_joystick = [0, 0]
        self._right_joystick = [0, 0]

    def get_new_input(self, server, port=4096):
        data, address = server.recvfrom(port)
        message = data.decode() # UTF-8 is used by default
        server.sendto(
            f"Received: {message}".encode(),
            address
        )

        gamepad_stream = message.split()

        #! This is the original code but it does not play well with the rest of the original code
        #! Would cause the code to crash in the next step
        #! Added extra error handling but this entire function needs to be refactored again
        # x = x.split()
        # if (x[0] == 'SYN_REPORT'):
        #     return ('SYN_REPORT')
        # else:
        #     return (x)

        try:
            self._hid_code = str(gamepad_stream[0])
            self._game_state = int(gamepad_stream[1])

        except IndexError | ValueError:
            # This is a SYN report
            # TODO: Make this more robust
            return 'SYN REPORT', None


        # I know this looks goofy but it calls the setter methods
        self.right_joystick = self.right_joystick
        self.left_joystick = self.left_joystick

        return self._hid_code, self._game_state

    @property
    def left_joystick(self):
        return self._left_joystick

    @left_joystick.setter
    def left_joystick(self, position):
        interpolated_game_state = int(np.interp(self.game_state, [-32768,32767], [-1,1]))

        if (self.hid_code == "ABS_Y"):
            self._left_joystick = [position[0], interpolated_game_state]

        if (self.hid_code == "ABS_X"):
            self._left_joystick = [interpolated_game_state, position[1]]

    @property
    def right_joystick(self):
        return self._right_joystick

    @right_joystick.setter
    def right_joystick(self, position):
        interpolated_game_state = int(np.interp(self.game_state, [-32768,32767], [-1,1]))

        if (self.hid_code == "ABS_RY"):
            self._right_joystick = [position[0], interpolated_game_state]

        if (self.hid_code == "ABS_RX"):
            self._right_joystick = [interpolated_game_state, position[1]]

    @property
    def turn(self):
        # TODO: This is a bit hacky, I'm not sure if this is the best way to do this
        turn_left, turn_right = 0

        if (self.right_joystick[0] > 0.2 or self.right_joystick[0] < -0.2):
            if (self.right_joystick[0] > 0):
                turn_right = self.right_joystick[0]

            elif (self.right_joystick[0] < 0):
                turn_left = self.right_joystick[0]

        return turn_right, turn_left
    
    def telemetry(self):
        return {
            "gamepad": {
                "hid_code": self.hid_code,
                "game_state": self.game_state,
                "left_joystick": self.left_joystick,
                "right_joystick": self.right_joystick
            }
        }
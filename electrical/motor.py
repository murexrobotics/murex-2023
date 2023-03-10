import pigpio
import time

cw = 4
pwm = 18

pi1 = pigpio.pi()
time.sleep(7)
pi1.set_mode(pwm, pigpio.OUTPUT)
time.sleep(1)
pi1.set_servo_pulsewidth(pwm, 1500)
time.sleep(1)
pi1.set_servo_pulsewidth(pwm, 1600)
time.sleep(1)
pi1.set_servo_pulsewidth(pwm, 1500)
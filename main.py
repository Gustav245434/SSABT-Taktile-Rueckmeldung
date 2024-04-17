import machine
import utime
import time
import math
# Code zur Vibration

vibrationsmotor = machine.PWM(5)

class Muster:
    def m1(self, delay):
        vibrationsmotor.freq(9000)
        vibrationsmotor.duty(1000)
        utime.sleep(delay)
        vibrationsmotor.freq(5)
        vibrationsmotor.duty(0)
        utime.sleep(delay)
        
muster=Muster()

muster.m1(0.5)
muster.m1(1)
muster.m1(0.5)

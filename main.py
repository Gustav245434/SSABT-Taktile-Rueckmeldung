import machine
import utime
import time
import math
#Setup the onboard LED Pin as an output
LED = machine.Pin(5)

vibrationsmotor = machine.PWM(5)




vibrationsmotor.duty(1000)

for num in range(1,6):
if vibrationsmotor.freq < 9000:
vibrationsmotor.freq(0)

else:
vibrationsmotor.freq(9000)
import machine
import utime
import time
import math
#Setup the onboard LED Pin as an output
LED = machine.Pin(5)

led2 = machine.PWM(5)




led2.duty(1000)

for num in range(1,6):
if led2.freq < 9000:
led2.freq(0)

else:
led2.freq(9000)
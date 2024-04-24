import machine
import utime
import time
import math

LED = machine.Pin(5)
led2 = machine.PWM(5)


class Motor:
    
    def __innit__(self, default):
        self.__default = default
        
    def set_default(self, default):
        self.__default = default
        
    def vibrate(value):
        match value:
            case 1:
                __m1()
            case 2:
                __m2()
            case 3:
                __m3()
                
    def vibrate():
        vibrate(self.__default)
            
    def __m1():
        led2.freq(9000)
        led2.duty(1000)
        utime.sleep(1)
        led2.freq(5)
        led2.duty(0)
        utime.sleep(1)
        
    def __m2():
        ###
        
    def __m3():
        ###


m = Motor(1)
m.vibrate()


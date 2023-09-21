from machine import Pin
import time

gy53 = Pin(19, Pin.IN)

def getdistancegy53():
    while gy53.value() == True:
        pass
    while gy53.value() == False:
        pass
    starttime = time.ticks_us()
    while gy53.value() == True:
        pass
    endtime = time.ticks_us()
    microsec_diff = endtime - starttime
    millimeterdistance = microsec_diff / 10
    distance = millimeterdistance / 10
    print(f"Distance to surface: {distance} cm")
    return distance
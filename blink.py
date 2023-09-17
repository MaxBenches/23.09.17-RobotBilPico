import machine
import time

led00 = machine.Pin("LED", machine.Pin.OUT)

"""Blink onboard LED"""
# For MicroPython. Needs 'machine' and 'time' modules,
# as well as the led00 variable
# The functions blinks the onboard LED a specified
# (x) amount of times, when Pico boots.
def blink_pico(amount):
    for i in range(amount):
        led00.on()
        time.sleep(.2)
        led00.off()
        time.sleep(.2)
import machine
import time

# Assign buzzer to pin
buzzer = machine.PWM(machine.Pin(11))
# Set duty cycle to 0 to turn off buzzer
buzzer.duty_u16(0)

def honk():
    buzzer.duty_u16(0)
    # Set a 50% duty cycle for the buzzer to produce a consistent tone
    buzzer.duty_u16(32767)
    # Play frequency / Pitch / Note
    buzzer.freq(1000)
    time.sleep(.5)
    buzzer.duty_u16(0)

def honk_stop():
    buzzer.duty_u16(0)
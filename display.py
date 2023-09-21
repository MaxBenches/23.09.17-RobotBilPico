import machine

# Assign display pins

seg_A = machine.Pin(18, machine.Pin.OUT)
seg_B = machine.Pin(17, machine.Pin.OUT)
seg_C = machine.Pin(16, machine.Pin.OUT)
seg_D = machine.Pin(15, machine.Pin.OUT)
seg_E = machine.Pin(14, machine.Pin.OUT)
seg_F = machine.Pin(13, machine.Pin.OUT)
seg_G = machine.Pin(12, machine.Pin.OUT)

pins = [seg_A, seg_B, seg_C, seg_D, seg_E, seg_F, seg_G]

# This list of 10 numbers shows the states of the pins for the segments
# to display the appropriate number.
# Index the list to display the correct number.

# numbers = [zero, one, two, three, four, five, six, seven, eight, nine, clear display]
numbers = [[1, 0, 1, 1, 0, 1, 1],
           [0, 1, 1, 0, 1, 1, 1]]

def display_number(number_to_display):
    pin = 0
    for segment in range(7):
        pins[pin].value(numbers[number_to_display][segment])
        pin += 1
    return number_to_display
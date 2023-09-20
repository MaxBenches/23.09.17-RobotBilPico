import time
# This function changes 'gears' by changing the variable we use to control the dutycycle (speed of the  car)

# Initialise speeds list, index and
speeds = [0.3, 0.9]
index = 1
speed_factor = speeds[index]

def change_gear(button_x, button_y):
    global speeds
    global index
    global speed_factor
    if button_y == 1:
        if index == 1:
            pass
        else:
            index += 1
            speed_factor = speeds[index]
    if button_x == 1:
        if index == 0:
            pass
        else:
            index -= 1
            speed_factor = speeds[index]
    return speed_factor

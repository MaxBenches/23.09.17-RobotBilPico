import display
# This function changes 'gears' by changing the variable
# we use to control the dutycycle (speed of the  car)

# Initialise speeds list, index and speed_factor
# 0.9 - Highest value, 0.4 - Next discernible difference,
# 0.25 - Lowest value while still being able to drive
speeds = [0.4, 0.9]
index = 1
speed_factor = speeds[index]

def change_gear(button_x, button_y):
    global speeds
    global index
    global speed_factor
    if button_y == 1:
        display.display_number(1)
        if index == 1:
            pass
        else:
            index += 1
            speed_factor = speeds[index]
    if button_x == 1:
        display.display_number(0)
        if index == 0:
            pass
        else:
            index -= 1
            speed_factor = speeds[index]
    return speed_factor

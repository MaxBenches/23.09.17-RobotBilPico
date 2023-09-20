import time
# This function changes 'gears' by changing the variable we use to control the dutycycle (speed of the  car)

# Initialise speed
speed = 0.5

def change_gear(y_axis_right):
    global speed
    if y_axis_right == 1:
        if speed >= 0.9:
            pass
        else:
            speed += 0.1
    elif y_axis_right == -0.9999:
        if speed <= 0.1:
            pass
        else:
            speed -= 0.1
    return speed

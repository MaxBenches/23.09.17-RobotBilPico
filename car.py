import motor

def drive(x, y):
    motor.M_left((x-y) * -1)
    motor.M_right(x-y)
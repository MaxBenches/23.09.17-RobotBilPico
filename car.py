import motor

def drive(x, y):
    motor.M_left((x, y))
    motor.M_right((x, y))
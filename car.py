import motor

def drive(left_trig, right_trig):

    motor.turn_left(, right_trig)
    motor.M_right(left_trig, right_trig)

def stop():
    motor.Mstop()
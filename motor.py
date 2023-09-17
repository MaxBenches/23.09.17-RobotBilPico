import machine


""" PIN ASSIGNMENTS """
# H-Bro Pins
IN1 = machine.Pin(0, machine.Pin.OUT)   # IN1 on = FORWARD
IN2 = machine.Pin(1, machine.Pin.OUT)   # IN2 on = BACKWARD
IN3 = machine.Pin(2, machine.Pin.OUT)   # IN3 on = FORWARD
IN4 = machine.Pin(3, machine.Pin.OUT)   # IN4 on = BACKWARD

# PWM Pin
pwmM1 = machine.PWM(machine.Pin(4))  #EN-A
pwmM2 = machine.PWM(machine.Pin(5))  #EN-B

""" FUNCTIONS """
def M_left(speed):
    # Fremad
    if speed >= 0:
        IN1.on()
        IN2.off()
        pwmM1.duty_u16(int(65536 * speed))
        print("M1 is moving forward")

    # # Bagud
    elif speed <= 0:
        IN1.off()
        IN2.on()
        pwmM1.duty_u16(int(65536 * speed))
        print("M2 is moving backwards")

def M_right(speed):
    # Fremad
    if speed >= 0:
        IN3.on()
        IN4.off()
        pwmM2.duty_u16(int(65536 * speed))
        print("M1 is moving forward")

    # Bagud
    elif speed <= 0:
        IN3.off()
        IN4.on()
        pwmM2.duty_u16(int(65536 * speed))
        print("M2 is moving backwards")

def Mstop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

"""
# Test
def M1(direction):
    # Forwards
    if direction >= 0:
        direc = "Forward"
        print(f"Motor 1 is moving {direc}.")

    # Backwards
    elif direction <= 0:
        direc = "Backward"
        print(f"Motor 1 is moving {direc}.")

def M2(direction):
    # Forwards
    if direction >= 0:
        direc = "Forward"
        print(f"Motor 2 is moving {direc}.")

    # Backwards
    elif direction <= 0:
        direc = "Backward"
        print(f"Motor 2 is moving {direc}.")

def Mstop():
    print("Car is stopped.")
"""
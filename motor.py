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
        speed2 = speed * 0.9
        IN1.on()
        IN2.off()
        pwmM1.duty_u16(int(65536 * speed2))

    # # Bagud
    elif speed <= 0:
        speed2 = speed * 0.9
        IN1.off()
        IN2.on()
        pwmM1.duty_u16(int(65536 * (speed2 * -1)))

def M_right(speed):
    # Fremad
    if speed >= 0:
        speed2 = speed * 0.9
        IN3.on()
        IN4.off()
        pwmM2.duty_u16(int(65536 * speed2))

    # Bagud
    elif speed <= 0:
        speed2 = speed * 0.9
        IN3.off()
        IN4.on()
        pwmM2.duty_u16(int(65536 * (speed2 * -1)))

def Mstop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
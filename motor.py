import machine


""" PIN ASSIGNMENTS """
# H-Bridge Pins
IN1 = machine.Pin(0, machine.Pin.OUT)   # IN1 on = FORWARD
IN2 = machine.Pin(1, machine.Pin.OUT)   # IN2 on = BACKWARD
IN3 = machine.Pin(2, machine.Pin.OUT)   # IN3 on = FORWARD
IN4 = machine.Pin(3, machine.Pin.OUT)   # IN4 on = BACKWARD

# PWM Pin
pwmM1 = machine.PWM(machine.Pin(4))  #EN-A
pwmM2 = machine.PWM(machine.Pin(5))  #EN-B

# PWM Frequency
pwmM1.freq(2000)
pwmM2.freq(2000)

""" FUNCTIONS """
# Stops both motors
def stop_motors():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

def forward(speed):
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()
    pwmM1.duty_u16(int(65536 * speed))     # Left Speed
    pwmM2.duty_u16(int(65536 * speed))     # Right Speed

def backward(speed):
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()
    pwmM1.duty_u16(int(65536 * speed))     # Left Speed
    pwmM2.duty_u16(int(65536 * speed))     # Right Speed

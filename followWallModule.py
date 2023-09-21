import motor
import GY53
import machine

def follow_wall():
    """H-Bridge and PWM definitions"""
    IN1 = machine.Pin(0, machine.Pin.OUT)  # IN1 on = FORWARD
    IN2 = machine.Pin(1, machine.Pin.OUT)  # IN2 on = BACKWARD
    IN3 = machine.Pin(2, machine.Pin.OUT)  # IN3 on = FORWARD
    IN4 = machine.Pin(3, machine.Pin.OUT)  # IN4 on = BACKWARD
    pwmM1 = machine.PWM(machine.Pin(4))  # EN-A
    pwmM2 = machine.PWM(machine.Pin(5))  # EN-B

    """ Standard speed definitions """
    speed = 0.5  # for motor module
    speedL = 0.5  # left motor
    speedR = 0.5  # right motor

    """ Standard Dutycycle """


    """PWM frequency and motor duty cycles"""
    motor.pwm_freq(1000, 1000)  # standard pwm freq
    def dutycycleLEFT(speedL):
        pwmM1.duty_u16(int(65536 * speedL))  # Left Speed

    def dutycycleRIGHT(speedR):
        pwmM2.duty_u16(int(65536 * speedR))  # Right Speed

    while True:
        motor.forward(speed)
        distance = GY53.getdistancegy53()
        if distance in range(15, 29): # drej til mod væg
            #Up PWM på motor mod væg
            """ SÆT PWM OP PÅ VENSTRE HJUL HER """
            speedL = 0.9
            dutycycleLEFT(speedL)
            IN1.on()
            IN3.on()
        elif distance in range(1, 9): # drej væk fra væg
            # Up PWM på motor mod væg
            """ SÆT PWM OP PÅ VENSTRE HJUL HER """
            speedR = 0.9
            dutycycleRIGHT(speedR)
            IN1.on()
            IN3.on()
        elif distance in range(10, 15):
            # PWM standard fremad
            speedL = 0.5
            speedR = 0.5
            dutycycleLEFT(speedL)
            dutycycleRIGHT(speedR)
            IN1.on()
            IN3.on()
        elif distance in range(30, 200): # drej højre på egen akse når væg er langt væk
            IN1.on()
            IN4.on()
import UDP
import motor
import gear
import blink

def main():
    # UDP setup has been tested and works
    sock, UDP_IP, UDP_PORT = UDP.UDP_setup("0.0.0.0", 5005, "BenchNet", "happyjungle592")
    sock.bind((UDP_IP, UDP_PORT))
    blink.blink_pico(3)

    motor.pwm_freq(1000, 1000)

    while True:
        message = UDP.msg_receive(sock, 1024, "utf-8")
        message_new = message.split(":")

        left_trig = float(message_new[0])           # Controls backward movement
        right_trig = float(message_new[1])          # Controls forward movement
        x_axis_right = float(message_new[2])        # This becomes the turning factor
        button_x = int(message_new[3])              # Used for changing gear down
        button_y = int(message_new[4])              # Used for changing gear up

        # Initialize motor speeds
        left_speed = 0
        right_speed = 0

        # Speed factor - To scale the dutycycle
        speed_scale = gear.change_gear(button_x, button_y)
        print(f"Speed scale: {speed_scale}")

        # Check if either trigger is pressed to set motor speed
        if right_trig > 0:
            # Right trigger pressed, go forward
            left_speed = right_trig * speed_scale
            right_speed = right_trig * speed_scale
        elif left_trig > 0:
            # Left trigger pressed, go backward
            left_speed = -left_trig * speed_scale
            right_speed = -left_trig * speed_scale

        # Adjust left and right motor speeds based on turning factor (x_axis_right)
        if right_trig > 0 or left_trig > 0:
            left_speed -= x_axis_right * 1.5      # Times 1.5 to adjust speed of turn
            right_speed += x_axis_right * 1.5     # Times 1.5 to adjust speed of turn

        # Clip motor speeds to the range [-1, 1]
        # This is done to ensure that the values
        # provided to the variables and therefore
        # the speed of the motors, are within
        # an appropriately valid range - If missing
        # the values of the variables goes over 1
        # and fucks up the steering of the car
        left_speed = max(-1, min(1, left_speed))
        right_speed = max(-1, min(1, right_speed))

        # Set motor speeds and directions
        if right_trig > 0:
            motor.forward(right_trig)
        elif left_trig > 0:
            motor.backward(left_trig)
        else:
            motor.stop_motors()

        # Set PWM duty cycle based on scaled speed
        # This is done to control the dutycycle
        # (speed) of the wheels, when turning
        pwm_duty_left = int(65536 * abs(left_speed))
        pwm_duty_right = int(65536 * abs(right_speed))
        motor.pwmM1.duty_u16(pwm_duty_left)
        motor.pwmM2.duty_u16(pwm_duty_right)

main()
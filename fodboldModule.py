import UDP
import motor
import gear
import blink
import horn

def main():
    # Set up UDP connection
    sock, UDP_IP, UDP_PORT = UDP.UDP_setup("0.0.0.0", 5005, "ITEK 2nd", "2nd_Semester_F23v")
    sock.bind((UDP_IP, UDP_PORT))
    # Blink to indicate the Pico has been connected to the network
    blink.blink_pico(3)
    # Set PWM frequency
    motor.pwm_freq(1000, 1000)

    while True:
        # Receive controller input and assign to variables
        trig_left, trig_right, x_axis_right, \
            button_x, button_y, button_b = UDP.recv_input(sock, 1024, "utf-8")

        # Speed factor - To scale the dutycycle (speed)
        speed_scale = gear.change_gear(button_x, button_y)

        if button_b == 1:
            horn.honk()


        # Initialise left and right speed variables - If not done, the car moves slow
        left_speed = 0
        right_speed = 0

        # Check if either trigger is pressed to set motor speed
        if trig_right > 0:
            # Right trigger pressed, go forward
            left_speed = trig_right * speed_scale
            right_speed = trig_right * speed_scale
        elif trig_left > 0:
            # Left trigger pressed, go backward
            left_speed = trig_left * speed_scale
            right_speed = trig_left * speed_scale

        # Adjust left and right motor speeds based on turning factor (x_axis_right)
        if trig_right > 0 or trig_left > 0:
            # Modify the turning factor based on speed_scale,
            # so that turning speed scales properly
            turning_factor = x_axis_right * speed_scale
            left_speed -= turning_factor
            right_speed += turning_factor


        # Set motor speeds and directions
        if trig_right > 0:
            motor.forward(trig_right)
        elif trig_left > 0:
            motor.backward(trig_left)
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

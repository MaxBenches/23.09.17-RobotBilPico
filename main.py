import blink
import motor
import UDP

blink.blink_pico(3)

def main():

    motor.M_left(1)
    motor.M_right(1)
    motor.M_left(-1)
    motor.M_right(-1)

    # UDP setup has been tested and works
    """
    sock, UDP_IP, UDP_PORT = UDP.UDP_setup("0.0.0.0", 5005, "BenchNet", "happyjungle592")
    sock.bind((UDP_IP, UDP_PORT))
    blink.blink_pico(3)

    while True:
        message = UDP.msg_receive(sock, 1024, ("utf-8"))
        print(message)
    """


main()
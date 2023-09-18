import blink
import car
import UDP


def main():

    # UDP setup has been tested and works

    sock, UDP_IP, UDP_PORT = UDP.UDP_setup("0.0.0.0", 5005, "ITEK 2nd", "2nd_Semester_F23v")
    sock.bind((UDP_IP, UDP_PORT))
    blink.blink_pico(3)

    while True:
        message_axes = UDP.msg_receive(sock, 1024, ("utf-8"))
        message_new = message_axes.split(":")
        x = float(message_new[0])
        y = float(message_new[1])
        print(x, y)

        car.drive(x, y)


main()
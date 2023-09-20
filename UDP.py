import network
import socket


# This function sets up a UDP connection to a specified network
def UDP_setup(listen_ip, listen_port, network_name, network_password):
    UDP_IP = listen_ip
    UDP_PORT = listen_port
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    ssid = network_name
    password = network_password
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print(station.ifconfig())
    return sock, UDP_IP, UDP_PORT


# This function receives a UDP message, decodes it,
# splits it at the ":", assigns the index values to variables
# and returns those
# Buffersize and which decoding format
# needs to be specified as arguments
def recv_input(sock, buffer_size, utf_x):
    message = sock.recv(buffer_size)
    message_decoded = message.decode(utf_x)
    message_split = message_decoded.split(":")
    trig_left = float(message_split[0])     # Controls backward movement
    trig_right = float(message_split[1])    # Controls forward movement
    x_axis_right = float(message_split[2])  # This becomes the turning factor
    button_x = int(message_split[3])        # Used for changing gear down
    button_y = int(message_split[4])        # Used for changing gear up
    button_b = int(message_split[5])        # Used for honking
    return trig_left, trig_right, x_axis_right, button_x, button_y, button_b

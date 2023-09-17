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


# This function receives a UDP message, decodes it
# and then prints it to the console
# Buffersize and which decoding format
# needs to be specified as arguments
def msg_receive(sock, buffer_size, utf_x):
    message = sock.recv(buffer_size)
    message_decoded = message.decode(utf_x)
    return message_decoded
    #print(message_decoded) # Used for test

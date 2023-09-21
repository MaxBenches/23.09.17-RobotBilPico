from machine import Pin
import blink
import time
import QRE1113
import push_box
import followWallModule

blink.blink_pico(3)

def main():
    followWallModule.follow_wall()

main()
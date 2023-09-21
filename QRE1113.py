from machine import Pin
import time

ir = Pin(6, Pin.IN)

def getQRE1113val():
    getsensor = ir.value()
    print(ir.value())
    if getsensor:
        #print("sort")
        return True, "Sort"
    else:
        #print("hvid")
        return False, "Hvid"
from machine import Pin
import time

buzzer = Pin(18, Pin.OUT)
#led
#buzzer = Pin(23, Pin.OUT)
pir = Pin(19, Pin.IN, Pin.PULL_DOWN)
while True:
    if pir.value() ==1: 
        print("Movimiento detectado") 
        buzzer.value(1)
        time.sleep(3)
    else:
        print("Sin movimiento")
        buzzer.value(0)
        time.sleep(1)
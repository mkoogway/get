import RPi.GPIO as GPIO
import time

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]

for i in dac:
    GPIO.setup(i,GPIO.OUT)

T = float(input("Input period: "))

try:
    while(True):
        inp = 0
        for j in range(256):
            inp = dec2bin(j)
            i = 0
            for led in dac:
                GPIO.output(led, inp[i])
                i += 1
            time.sleep(T/2/256)
        for j in range(256,0,-1):
            inp = dec2bin(j)
            i = 0
            for led in dac:
                GPIO.output(led, inp[i])
                i += 1
            time.sleep(T/2/256)
finally:
    print("ok")
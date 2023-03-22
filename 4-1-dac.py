import RPi.GPIO as GPIO

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]

for i in dac:
    GPIO.setup(i,GPIO.OUT)

try:
    while(True):
        inp = input('Input a number from 0 to 255: ')
        if inp == 'q':
            break
        inp = int(inp)
        if inp >= 2**8 or inp < 0:
            print("err")
            continue
        inp = dec2bin(inp)
        out = 0
        for i in range(8):
            out += inp[i]*3.3/(2**(i+1))
        print(f'Expected output: {out}\n')
        i = 0
        for led in dac:
            GPIO.output(led, inp[i])
            i += 1
finally:
    print("ok")
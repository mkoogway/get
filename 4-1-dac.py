import RPi.GPIO as GPIO

def dec2bin(val):                                           #   Converts a decimal to binary number, returns list of ints
    return [int(bit) for bit in bin(val)[2:].zfill(8)]      #


GPIO.setmode(GPIO.BCM)          #   Setting the pin numeration mode
dac = [26,19,13,6,5,11,9,10]    #   A list of DAC leds (inputs)

for i in dac:
    GPIO.setup(i,GPIO.OUT)      #   Setting DAC inputs as output pins

try:
    while(True):
        inp = input('Input a number from 0 to 255: ')   #   inp - level of power from 0 to 255
        if inp == 'q':                                  #   press 'q' to exit
            break
        inp = int(inp)
        if inp >= 2**8 or inp < 0:                      #   max input is 255, min is 0
            print("Enter a number from 0 to 255!")
            continue
        inp = dec2bin(inp)                              #   convert input to list if 0 and 1
        out = 0
        for i in range(8):                              #   
            out += inp[i]*3.3/(2**(i+1))                #   calculate the expected output
        print(f'Expected output: {out}\n')              #   print it

        for i in range(len(dac)):
            GPIO.output(dac[i], inp[i])

finally:
    print("Exception found or programm finished.")
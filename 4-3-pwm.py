import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)

p = GPIO.PWM(22, 1000)

p.start(0)

try:
    while(True):
        k = int(input('Коэффициент заполнения: '))
        p.ChangeDutyCycle(k)
        exp = 3.3*k/100
        print(f"Expected: {exp}")
finally:
    GPIO.cleanup()
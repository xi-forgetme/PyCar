import RPi.GPIO as GPIO
import time
import sys

class Car():
    def __init__(self):
        self.enab_pin = [5,6,13,19]
        self.inx_pin = [21,22,23,24]
        self.RightAhead_pin = self.inx_pin[0]
        self.RightBack_pin = self.inx_pin[1]
        self.LeftAhead_pin = self.inx_pin[2]
        self.LeftBack_pin = self.inx_pin[3]
        self.setup()
    def setup(self):
        print("Hey! Init...")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in self.enab_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        pin = None
        for pin in self.inx_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        print("--End Setup--")

    def front(self):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)

    def back(self):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)

    def leftFront(self):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)
    
    def rightFront(self):
        self.setup()
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)

    def leftBack(self):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)

    def rightBack(self):
        self.setup()
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)

def main(status):
        car = Car()
        if status == 'front':
            car.front()
        elif status == 'back':
            car.back()
        elif statis == 'leftFront':
            car.leftFront()
        elif status == 'rightFront':
            car.rightFront()
        elif status == 'leftBack':
            car.leftBack()
        elif status == 'rightBack':
            car.rightBack()
        elif status == 'stop':
            car.setup()
if __name__ == '__main__':
    main(sys.argv[1])
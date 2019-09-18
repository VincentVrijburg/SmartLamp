# Import necessary modules.
import RPi.GPIO as GPIO

# Define the Relay class in order to use the Relay in other scripts.
class Relay:
    def __init__(self, pin):
        self.pin = pin
        self.lastTimeTurnedOn = None
        self.setup()
    
    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def dispose(self):
        GPIO.cleanup()

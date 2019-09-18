# Import necessary modules.
import RPi.GPIO as GPIO

# Define the Relay class in order to use the Relay in other scripts.
class LightSensor:
    def __init__(self, pin):
        self.pin = pin
        self.setup()
    
    def setup(self):
        GPIO.setwarnings(True)
        GPIO.setup(self.pin, GPIO.IN)

    def is_dark_environment(self):
        return GPIO.input(self.pin)

    def dispose(self):
        GPIO.cleanup()

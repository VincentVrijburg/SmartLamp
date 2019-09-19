# Import necessary modules.
import RPi.GPIO as GPIO

# Define the Relay class in order to use the Relay in other scripts.
class MotionSensor:
    def __init__(self, pin):
        self.pin = pin
        self.motionDetected = False
        self.setup()
    
    def setup(self):
        GPIO.setwarnings(True)
        GPIO.setup(self.pin, GPIO.IN)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.motion_detected)

    def motion_detected(self, pin):
        if GPIO.input(pin):
            self.motionDetected = True
        else:
            self.motionDetected = False

    def dispose(self):
        GPIO.cleanup()

# Import necessary modules.
import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import modules.relay as r
import modules.motion_sensor as ms
import modules.light_sensor as ls

# Set the different inputs/outputs for the Raspberry Pi modules and sensors.
pin_motion_sensor_in = 11
pin_light_sensor_in = 12
pin_relay_out = 7

# Set the correct RPi.GPIO mode.
GPIO.setmode(GPIO.BOARD)

# Initialize the different classes.
motionSensor = ms.MotionSensor(pin_motion_sensor_in)
lightSensor = ls.LightSensor(pin_light_sensor_in)
relay = r.Relay(pin_relay_out)

while 1:
    if ((relay.lastTimeTurnedOn is not None) and ((relay.lastTimeTurnedOn + timedelta(seconds=5) > datetime.now()))):
        if (motionSensor.motionDetected):
            print("Het licht blijft aan, en er is beweging gedetecteerd")
            relay.lastTimeTurnedOn = datetime.now()
            relay.turn_on()
        else:
            print("Het licht blijft aan")
            relay.turn_on()
    else:
        if (motionSensor.motionDetected):
            needsLight = lightSensor.is_dark_environment()
            if (needsLight == True):
                print("Beweging gedetecteerd, het licht zal aangezet worden indien nodig")
                relay.lastTimeTurnedOn = datetime.now()
                relay.turn_on()
            else:
                print("Beweging gedetecteerd, maar het licht is niet nodig")
                relay.turn_off()
        else:
            relay.turn_off()

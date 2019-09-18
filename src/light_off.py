import RPi.GPIO as GPIO
import modules.relay as r

# Set the output for the relay module.
pin_relay_out = 7

# Set the correct RPi.GPIO mode.
GPIO.setmode(GPIO.BOARD)

# Initialize the relay class.
relay = r.Relay(pin_relay_out)

# Turn the relay on in order to turn the light on.
relay.turn_off()
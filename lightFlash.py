import RPi.GPIO as GPIO
import time

# Pin Constants
LED = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)

#GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
on = True
try:
	while True:
		if on:
			GPIO.output(led, 0)
			on = False
		else:
			GPIO.output(led, 1)
			on = True

		time.sleep(1)

except KeyboardInterrupt:
	print('Program terminated.')

finally:
	GPIO.cleanup()
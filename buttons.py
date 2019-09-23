

#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP) //pin n   

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x = 0


GPIO.add_event_detect(21, GPIO.RISING)  # add rising edge detection on a channel
GPIO.add_event_detect(20, GPIO.RISING)

while x < 5:
	if GPIO.event_detected(21):
	    print('Button pressed')
	    x+=1
	    print(x)
	if GPIO.event_detected(20):
		print('switched')
		print(x)
		break

print GPIO.input(21)
print GPIO.input(20)








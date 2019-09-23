

#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP) //pin n   


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x = 0


GPIO.add_event_detect(21, GPIO.RISING)  # add rising edge detection on a channel

while x < 5:
	if GPIO.event_detected(21):
	    print('Button pressed')
	    x+=1
	    print(x)


print GPIO.input(21)







#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP) //pin n   


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
x = 0
y = 0


GPIO.add_event_detect(21, GPIO.RISING)  # add rising edge detection on a channel
GPIO.add_event_detect(20, GPIO.RISING) # switc
GPIO.add_event_detect(23, GPIO.RISING) # stick X
# GPIO.add_event_detect(18, GPIO.RISING) 

while x < 5:
	if GPIO.event_detected(21):
	    print('Button pressed')
	    x+=1
	    print(x)
	if GPIO.event_detected(20):
		print('switched')
		print(x)
		break
	if GPIO.event_detected(23):
		print('Stick Down')
		y+=1
		print(y)
	# if GPIO.event_detected(18):
	# 	print('OTHER Stick')
	# 	y-=1
	# 	print(y)


print GPIO.input(21)
print GPIO.input(20)
print GPIO.input(23)






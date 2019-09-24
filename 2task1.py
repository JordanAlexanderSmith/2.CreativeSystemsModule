import RPi.GPIO as GPIO
import sys
import time
from colorama import Fore, Back, Style

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #Switch
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Stick

x = 1 #Button Clicks
BG = 0 #Background flipper
RGB = 0 # Red, Green, Blue flipper

GPIO.add_event_detect(21, GPIO.RISING)  
GPIO.add_event_detect(23, GPIO.RISING)

print("Hello World!")

while x <= 32:

	if GPIO.input(20) == 1:     #when switch is turned from off to on it flips the background color of the terminal, MUST be turned off after one flip
		if BG == 0:
			print(Back.WHITE)
			BG=1
			time.sleep(3)
		else:
			print(Back.BLACK)
			BG=0
			time.sleep(3)


	if GPIO.event_detected(21): #prints my name and the number of presses upon a button press
	    print('Jordan Alexander Smith', x)
	    x+=1
	    time.sleep(0.5)

	if GPIO.event_detected(23): #Changes the color of the text upon a stick toggle
		if RGB == 0:
			print(Fore.RED)
			print('Stick Down')
			RGB = 1
			time.sleep(2)
			continue
		if RGB == 1:
			print(Fore.BLUE)
			print('Stick Down')
			RGB = 2
			time.sleep(2)
			continue
		if RGB == 2:
			print(Fore.GREEN)
			print('Stick Down')
			RGB = 0
			time.sleep(2)
			continue

print('Goodbye World?')

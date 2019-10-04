# 2.CreativeSystemsModule

For task 1 of module 2 we were asked to create a system that had 3 different states of digital output using the GPIO pins attached to the raspberry pi in combination with a switch, a button, and an analog stick.

I figured that printing my name to the terminal was a form of digital output, so I worked to apply different states to my logic. The simplest function is printing my name at the click of the button. I found a way to create 6 different states of printing my name by manipulating the color of the background of the terminal using the switch and the color of the words using the analog stick.

The 2 colors black and white, multipied by the 3 colors red, green, and blue, come to 6 different combinations of colors for printing to the terminal.

To recreate my work one would need a Raspberry Pi, a board, a switch, a button, an analog stick, and the necessary colorama package installed to their device. By wiring the device in the fashion of my code one should recieve the desired output. Once the button is pressed 32 times, the program terminates and says goodbye.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For task 2 of module 2 we were asked to use the knowledge we gained from task one and create a playable device.

I chose to create a box that manipulates a sin wave depending on the orientation of the joystick. It changes frequency on the X axis, and amplitude on the Y axis. The tone is turned on and off by a switch on the side. Additionally, a button controls the sound of a snare drum.

In order to recreate my work one would need an ESP32, a board, a switch, a button, and an analog stick. The schematics of the wire and pinning is shown in the pictures attached to this repository. I used a simple cardboard box for the enclosure and by cutting a few holes, was able to connect all of my components accordingly.

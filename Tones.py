import pyaudio
import numpy as np
import time

import keyboard  # using module keyboard
from playsound import playsound



p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)


stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)


#stream.write(volume*samples)
x = 0
y = 0
while x < 10:
	#f+=20
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*(f+y)/fs)).astype(np.float32)
	stream.write(volume*samples)
	x+=1
	y+=32
	volume-=0.02
	playsound('/Users/will/Documents/snare.wav')

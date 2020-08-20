from synthesizer import Player, Synthesizer, Waveform, Writer
from os import system
from sys import argv 
#import synthesizer
#from synthesizer import Writer
import math
import random

def playNicely(length):
    player = Player()
    player.open_stream()
    pitch = 440
    velocity = 1
    maxE = 10
    ratio = 2 ** (2/12)
    for i in range(length):
        if(True):
            if(random.randint(0,9) <3):
                offset = random.randint(-2,2)/2
            else:
                offset = 0
            pitch = pitch * (ratio) ** (velocity + offset)
            if(pitch < 250):
                velocity += 0.5
                pitch = pitch * (ratio) ** 1
                if(random.randint(0,99) < 5):
                    velocity = -0.5
                    pitch = pitch * 2 ** (random.randint(7,30)/12)
            if(pitch > 750):
                velocity -= 0.5
                pitch = pitch * (ratio) ** -1
                if(random.randint(0,99) < 5):
                    velocity = 0.5
                    pitch = pitch * 2 ** (-random.randint(7,30)/12)
            if(random.randint(0,20) == 0):
                velocity = random.randint(-1,1) * 2
            if(random.randint(0,9) < 4):
                velocity = velocity + random.randint(-2,2)/2
        synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=True)
        if(random.randint(0,99) < 40 and (velocity == 0 or abs(velocity) >= 2)):
            if(random.randint(0,99) < 70):
                lenExp = 0
            elif(random.randint(0,99) < 80):
                lenExp = 1
            else:
                lenExp = 2
            length = (1/10) * (2 ** (lenExp))
            player.play_wave(synthesizer.generate_chord([float(0)], length))
        else:
            print("Bass pitch: " + str(pitch) + " Hz, You are now listening to interval ratio: " + str(pitch))
            if(random.randint(0,99) < 85):
                lenExp = 0
            elif(random.randint(0,99) < 80):
                lenExp = 1
            else:
                lenExp = 2
            length = (1/10) * (2 ** (lenExp))
            player.play_wave(synthesizer.generate_chord([float(pitch)], length) )

def main(argv):
    #maxInt = int(argv[1])
    length = int(argv[1])
    playNicely(length)

main(argv)



















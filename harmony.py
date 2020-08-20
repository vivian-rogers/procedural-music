from synthesizer import Player, Synthesizer, Waveform, Writer
from os import system
from sys import argv 
#import synthesizer
#from synthesizer import Writer
import math
import random

def GCD(chord):
	b = chord[0]
	for i in range(1,len(chord)):
		s=math.gcd(b,chord[i])
		b=s
	return b

#def createPrimes(primes,maxprime):
#	for num in range(3,maxprime,2):
#		if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#			primes.append(num)
#			print (num)

def entropy(chord):
#	product = 1
#	for i in chord:
#		product = product * i
#    return product
    sum = 0
    for i in chord:
        sum += i*i
    return sum 


def binaryInsert(chords,chord, lowerBound, upperBound):
    chordEntropy = 0
    chordEntropy = entropy(chord)
    avg = int((upperBound + lowerBound) / 2)
    if(upperBound == lowerBound):
	#chords.insert(upperBound,[chord,returnPitches(chord)])
        chords.insert(upperBound,chord)
    else:
        if(chordEntropy > entropy(chords[avg])):
	    #if(True):
            if(GCD(chord) == 1):
                binaryInsert(chords,chord,avg+1,upperBound)	
            else:
                binaryInsert(chords,chord,lowerBound,avg)	
                upperBound = avg
			#print(str(lowerBound) + " " + str(upperBound) + " " + str(avg))
	#	chords.insert(avg,chord)
	
def returnPitches(interval,refpitch,bass):
    temp = []
    avg = 0
    #for i in interval:
    #    avg += i / len(interval)
    if(bass == True):
        for i in interval:
            #temp.append(refpitch* (2**(i/12)) / (2**(interval[0]/12)))
            #temp.append((2 ** (interval[0] / 12))*refpitch)
            temp.append(refpitch*i / interval[0])
    else:
        for i in interval:
            temp.append(refpitch*i / interval[-1])
    return temp
	


def chordGen(chords,numNotes, maxRes):
	temp = []
	for i in range(numNotes):
		temp.append(1)
	chords.append(temp)
	temp = []
	for i in range(1,maxRes):
		#temp.append(i)
		for j in range(i+1,maxRes):
			#temp = [i]
			temp = [i,j]
			#temp = [2**(i/12),2**(j/12)]
			#temp.append(j)
			if( temp[-1] / temp[0] < 2.5):
				binaryInsert(chords,temp,0,len(chords))
			temp = []

#def chordGenHelper(chords, layer, maxRes):
#	if(layer != 0):
#	else:
#		temp = [i,j]
#		#temp.append(j)
#		if( temp[-1] / temp[0] < 2.5):
#			binaryInsert(chords,temp,0,len(chords))
#			temp = []
		

def intervalsToPitches(chords,frequencies):
	for i in chords:
		frequencies.append(returnPitches(i,440,True))
		
		
	
def printChords(chords):
	for i in chords:
		print(str(i))
def writeChords(freqs,chords):
    player = Player()
    player.open_stream()
    #for i in freqs:
    for i in range(len(freqs)):
        print("You are now listening to interval ratio: " + str(chords[i]))
        synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=False)
        player.play_wave(synthesizer.generate_chord(freqs[i], 0.35))
        #player.play_wave(synthesizer.generate_chord([float(1)], 0.5))
	#wave = Synthesizer.generate_chord(2, i, 3.0)
	#writer.write.wave("./test.wav",wave)
def playNicely(freqs,chords,length):
    player = Player()
    player.open_stream()
    pitch = 440
    velocity = 1
    maxE = 10
    ratio = 2 ** (2/12)
    #ratio = 20/19
    for i in range(length):
        if(True):
#            if(random.randint(0,1) == 0):
#               pitch = 440 * chords[random.randint(2,18)][0]/chords[random.randint(2,16)][-1]
#            else:
#                pitch = 440 * chords[random.randint(2,18)][-1]/chords[random.randint(2,16)][0]
#            if(pitch > 750):
#                pitch = pitch/2
#            if(pitch < 250):
#                pitch = pitch*2
            #if(velocity < 0):
            if(random.randint(0,9) <2):
                offset = random.randint(-1,1)
            else:
                offset = 0
            pitch = pitch * (ratio) ** (velocity + offset)
                #pitch = pitch * chords[random.randint(2,maxE)][0]/chords[random.randint(2,maxE)][-1]
            #else:
            #   pitch = pitch * 15/14
                #pitch = pitch * chords[random.randint(2,maxE)][-1]/chords[random.randint(2,maxE)][0]
            if(pitch < 300):
                #velocity += 1
                velocity += 0.5
                pitch = pitch * (ratio) ** 1
                if(random.randint(0,9) < 3):
                    velocity = -0.5
                    pitch = pitch * 2 ** (18/12)
            if(pitch > 750):
                velocity -= 0.5
                #velocity -= 1
                pitch = pitch * (ratio) ** -1
                if(random.randint(0,9) < 3):
                    velocity = 0.5
                    pitch = pitch * 2 ** (-18/12)
            if(random.randint(0,20) == 0):
                velocity = random.randint(-1,1) * 2
            if(random.randint(0,9) < 4):
                velocity = velocity + random.randint(-2,2)/2
        chosenChord = chords[random.randint(2,18)]
        #chosenChord = [2,3]
        synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=True)
        if(random.randint(0,99) < 25 and abs(velocity) < 0.6):
            #length = (1) / 6
            length = (1/10) * (2 ** (random.randint(0,1)))
            #length = (random.randint(0,1) + 1) / 6
            player.play_wave(synthesizer.generate_chord([float(0)], length))
        else:
            #system("clear")
            print("Bass pitch: " + str(pitch) + " Hz, You are now listening to interval ratio: " + str(chosenChord))
            #length = (2) / 12
            length = (1/10) * (2 ** (random.randint(0,1)))
            player.play_wave(synthesizer.generate_chord(returnPitches(chosenChord,pitch,True), length) )
       # player.play_wave(synthesizer.generate_chord(freqs[i], random.randint(1,4)/8))


def main(argv):
    maxInt = int(argv[1])
    length = int(argv[2])
    chords = []
    freqs = []
    chordGen(chords,2,maxInt)
    printChords(chords)
    intervalsToPitches(chords,freqs)
    #printChords(freqs)
    playNicely(freqs,chords, length)
    #writeChords(freqs,chords)

#def main():
#    writer = Writer()
#    chord = ["C4", "E4", "G4"]
#    wave = Synthesizer.generate_chord(len(chord),chord, 3)
#    writer.write_wave("path/to/your.wav", wave)


main(argv)



















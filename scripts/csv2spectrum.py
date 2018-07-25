import sys
import csv
import math

import numpy as np
import matplotlib.pyplot as plt

from operator import itemgetter
from bisect import bisect_left
from random import randint

spectral_file_out = "./spectrum_document_csv.dat"

if (len(sys.argv) != 4 and len(sys.argv) != 5):
	print("e.g. python csv2spectrum.py ./Schilke_OrionSurvey.csv 2 ./llda_train_input/hot_cores_tr_features.dat 1,100")
	sys.exit(1)

fileName = sys.argv[1]
channeling = int(sys.argv[2])
featuresFile = sys.argv[3]
spectrum_chunk = int(sys.argv[4].split(',')[0]) if len(sys.argv) == 5 else None
spectrum_chunks_size = int(sys.argv[4].split(',')[1]) if len(sys.argv) == 5 else None

def takeClosest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    after_delta = after - myNumber
    before_delta = myNumber - before
    if after_delta < before_delta:
        return after
    elif before_delta < after_delta:
        return before
    else:
        return before

def takeClosest_v2(myList, myNumber, thresshold = 200000):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    after_delta = after - myNumber
    before_delta = myNumber - before
    if after_delta < before_delta and after_delta <= thresshold:
        return after
    elif before_delta < after_delta and before_delta <= thresshold:
        return before
    elif after_delta == before_delta and after_delta <= thresshold:
        return before
    else:
        return myNumber

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open(featuresFile) as f:
    tokens = f.readline().split()
    vocabulary = [int(token) for token in tokens]

spectrum = list()
with open(fileName) as csvfile:
    #FORMAT: freq[GHz]:energy[K],
	spamreader = csv.reader(csvfile, delimiter=',')
	for i, row in enumerate(spamreader):
		if i == 0:
			continue
	        
		energy = float(row[4].replace(',','.'))
		frequency = float(row[3].replace(',','.'))

		# if not (frequency > 625 and frequency < 626):
		# 	continue

		#frequency_ch = int(math.floor(frequency*10**channeling)) #Frequency in GHz
		frequency_ch = int(round(frequency*10**channeling)) #Frequency in GHz
		spectrum.append((frequency, takeClosest(vocabulary,frequency_ch),energy))
		#spectrum.append((frequency, takeClosest_v2(vocabulary,frequency_ch,20000000),energy))
		#spectrum.append((frequency, frequency_ch, energy))

spectrum.sort(key=itemgetter(0))
corpus = list(chunks(spectrum,spectrum_chunks_size))
spectrum = corpus[spectrum_chunk-1]
print("From: "+str(spectrum[0])+" To: "+str(spectrum[-1]))

spectrum_document = list()
for freq, freq_ch, energy in spectrum:
	tf = int(math.ceil(np.log2(energy+1))) #TF v2.2
	spectrum_document.extend([str(freq_ch) for i in range(tf)])

#Saving file
mFile_out = open(spectral_file_out,'w')
print("Generated File:")
print(" ".join(spectrum_document)+"\n")
mFile_out.write(" ".join(spectrum_document)+"\n")
mFile_out.close()


#plt.plot([freq for freq, energy in spectrum],[energy for freq, energy in spectrum])
#plt.show()

#Calculating Mean & Standard Deviation
#ALL TRANSITIONS TODO: INCLUDE NOISE / SIMULTED SIGNAL
#energy_array = np.array(energy_list)
#energy_mean = np.mean(energy_list)
#print("\nMean: "+str(energy_mean))
#energy_std = np.std(energy_array)
#print("\nSigma: "+str(sigma_thresshold)+"x"+str(energy_std))

#print(spectrum[:10])

import astropy.units as u
import numpy as np
from astropy.io import fits

import math
import os
import operator
import sys

from sklearn.cluster import DBSCAN

from bisect import bisect_left

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
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

channeling = int(sys.argv[1])
corpus = sys.argv[2]

spectral_file_out = "./spectrum_document.dat"
c = 299792458
sigma_thresshold = 0

#ROI1
#freq_list = [624498400000,	624498400000,	624498400000,	624551600000,	624551900000,	624552100000,	624552300000,	624582700000,	624583000000,	624583100000,	624583300000,	624626000000,	624629100000,	624629100000,	624629100000,	624670300000,	624680300000,	624680300000,	624736100000,	624736100000,	624736100000,	624744300000,	624778000000,	624819300000,	624819300000,	624819300000,	624838000000,	624878800000,	624878800000,	624878800000,	624887400000,	624901300000,	624905400000,	624905600000,	624907800000,	624908800000,	624909000000,	624914500000,	624914500000,	624914500000,	624914500000,	624914500000,	624920100000,	624924600000,	624926400000,	624926500000,	624926400000,	624932000000,	624932300000,	624935500000,	624935700000,	624935800000,	624936400000,	624964300000,	624977800000,	624988300000,	625024600000,	625063300000,	625072700000,	625155700000,	625207600000,	625294000000,	625335000000,	625352500000,	625383100000,	625434000000,	625510200000,	625668100000,	625749500000,	625781300000,	625901600000,	625918700000,	625932000000,	625971500000,	626007700000,	626041100000,	626041200000,	626043500000,	626073600000,	626073600000,	626075400000,	626087300000]
#energy_list = [9.7,	9.7,	9.7,	4.5,	4.5,	4.5,	4.5,	6.5,	6.5,	6.5,	6.5,	16.7,	16.7,	16.7,	16.7,	4.1,	3.1,	3.1,	9.7,	9.7,	9.7,	9.7,	5.9,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	6.7,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	16.9,	9.6,	9.6,	9.6,	1.7,	4.8,	6,	8.1,	5.7,	7.3,	4.6,	4.6,	4.6,	2.2,	5.7,	4.9,	18.1,	6.1,	15.2,	15.2,	15.2,	5.5,	5,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1]

#ROI2
#freq_list = [625901600000,	625918700000,	625932000000,	625971500000,	626007700000,	626041100000,	626041200000,	626043500000,	626073600000,	626073600000,	626075400000,	626087300000,	626103100000,	626111200000,	626112200000,	626137500000,	626156800000,	626185800000,	626191900000,	626196500000,	626306200000,	626306200000,	626306200000,	626349200000,	626374800000,	626376400000,	626397800000,	626451900000,	626474600000,	626476700000,	626476700000,	626482600000,	626489900000,	626511900000,	626511900000,	626555000000,	626555900000,	626608700000,	626609000000,	626626300000,	626640000000,	626654100000,	626673800000,	626724700000,	626803800000,	626809500000,	626864900000,	626865800000,	626880700000,	626930500000,	626945200000,	626989000000,	626989000000,	626989000000,	626989000000,	627004600000,	627013000000,	627015600000,	627018100000,	627019400000,	627019500000,	627020600000,	627020600000,	627022000000,	627023300000,	627057400000,	627057800000,	627057800000,	627057800000,	627058100000,	627058400000,	627058600000]
#energy_list = [15.2,	15.2,	15.2,	5.5,	5,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	21.1,	5.4,	5.4,	3.1,	3.9,	3.9,	3.9,	8.8,	2.5,	2.5,	4.2,	6.8,	13.1,	13.1,	13.1,	13.1,	8.5,	9.4,	9.4,	13.8,	13.8,	14.2,	14.2,	26.2,	26.2,	18.2,	15.3,	3.7,	5.9,	5.9,	8.6,	8.6,	9,	9.8,	12,	4.3,	4.3,	4.3,	4.3,	8.8,	14.6,	14.6,	14.6,	14.6,	14.6,	14.6,	14.6,	14.6,	14.6,	0,	5.7,	5.7,	5.7,	0,	0,	0]

#Ejemplo controlado
#channeled_freq_list = [70, 167, 973264, 76]
channeled_freq_list = [70, 167, 973264]
energy_list = [80, 500, 1200]

#Channeling
#channeled_freq_list = [int(math.floor(freq/10**(9-channeling))) for freq in freq_list]

#Frequency Casting
words = set()
with open(corpus) as f:
	for line in f:
		tokens = line.split()[1:]
		words.update(tokens)

vocabulary = sorted(list(words), key=int)
vocabulary = [int(word) for word in vocabulary]

casted_freq_list = [takeClosest(vocabulary,freq) for freq in channeled_freq_list]  

data_list = zip(casted_freq_list, energy_list)
#data_list = zip(channeled_freq_list, energy_list)

#Calculating Mean & Standard Deviation
energy_array = np.array(energy_list)
energy_mean = np.mean(energy_list)
energy_std = np.std(energy_array)

print("Sigma: "+str(sigma_thresshold)+"x"+str(energy_std))

#TF Representation
words = []
for freq, energy in data_list:
        #tf = int(np.log2(math.ceil(energy))) if energy >= energy_std*sigma_thresshold else 0
        #tf = int(np.log2(math.ceil(energy))) if energy >= 1 else 0
        tf = int(np.log2(math.ceil(energy+1)))
        words.extend([str(freq) for i in range(tf)])

mFile_out = open(spectral_file_out,'w')
print("Generated File:")
print(" ".join(words)+"\n")
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()

import numpy as np
from scipy import stats
from math import floor, ceil
import sys

if (len(sys.argv) != 4):
	#python frequency_expander.py file expansion resolution")
	print("e.g. python frequency_expander.py hot_cores_tr.dat 3 0.001")
	sys.exit() 

#CASA SPECTRUMS RESOLUTION: DELTA FREQ 0,001 [GHz]
if (sys.argv[1].split('.')[0].split('_')[-1] == 'tr' or sys.argv[1].split('.')[0].split('_')[-1] == '1' or sys.argv[1].split('.')[0].split('_')[-1] == '2'):
	print("Cannot expand this data file")
	sys.exit()

dataFile = sys.argv[1]
expansion = int(sys.argv[2])


if (sys.argv[1].split('.')[0].split('_')[-1] == '3'):
	resolution = int(float(sys.argv[3])*1e3)
elif (sys.argv[1].split('.')[0].split('_')[-1] == '4'):
	resolution = int(float(sys.argv[3])*1e4)
elif (sys.argv[1].split('.')[0].split('_')[-1] == 'full'):
	resolution = int(float(sys.argv[3])*1e5)

counter = 0
with open(dataFile) as f:
	mFile = open(dataFile.split('.')[0]+'_expanded.'+dataFile.split('.')[1], 'w')
	for line in f:
		counter += 1

		freqs = [int(freq) for freq in line.split()[1:]]
		#freq_unique = sorted(set(freqs))
		freqs_aux = freqs[:]

		freqs_count = [freqs.count(freq) for freq in freqs]
		freqs_dict = dict(zip(freqs, freqs_count))
		
		for freq, count in freqs_dict.iteritems():
			normal = stats.norm(freq,float(resolution*expansion/2))
			
			for i in range(expansion):
				new_freq = freq+(i+1)*resolution
				new_count = int(count/normal.pdf(freq)*normal.pdf(new_freq))
				freqs.extend([new_freq for i in range(new_count)])

				#print("Freq: "+str(freq)+" Count: "+str(count))
				#print("New Freq: "+str(new_freq)+" New Count: "+str(new_count))				
		freqs.sort(key=int)
		mFile.write(line.split()[0]+" "+" ".join(str(freq) for freq in freqs)+"\n")
	mFile.close()

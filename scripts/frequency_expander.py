import numpy as np
from scipy import stats
from math import floor, ceil
import sys

#CASA SPECTRUMS FREQUENCY RESOLUTION: DELTA FREQ 0,001 [GHz]

if (len(sys.argv) != 4):
	"""Parameters 
	llda_input_data: train data file to expand
	neighborhood_expansion: number of neighbor channels to add
	spectrum_resolution: emission lenght
	"""
	print("e.g. python frequency_expander.py hot_cores_tr.dat 3 0.00001")
	sys.exit() 

if (sys.argv[1].split('.')[0].split('_')[-1] == 'tr' or sys.argv[1].split('.')[0].split('_')[-1] == '1' or sys.argv[1].split('.')[0].split('_')[-1] == '2'):
	print("Cannot expand this data file")
	sys.exit()

dataFile = sys.argv[1]
expansion = int(sys.argv[2])
resolution = sys.argv[3]

outputFile = dataFile.split('.')[0]+'_expanded'+'.'+dataFile.split('.')[1]

if (sys.argv[1].split('.')[0].split('_')[-1] == '3'):
	resolution = int(float(resolution)*1e3)
elif (sys.argv[1].split('.')[0].split('_')[-1] == '4'):
	resolution = int(float(resolution)*1e4)
elif (sys.argv[1].split('.')[0].split('_')[-1] == 'full'):
	resolution = int(float(resolution)*1e5)

counter = 0
with open(dataFile) as f:
	mFile = open(outputFile, 'w')
	for line in f:
		freqs = [int(freq) for freq in line.split()[1:]]
		#freqs_aux = freqs[:]

		freqs_count = [freqs.count(freq) for freq in freqs]
		freqs_dict = dict(zip(freqs, freqs_count))
		
		for freq, count in freqs_dict.items():
			normal = stats.norm(freq,(resolution*expansion)/2)
			
			for i in range(expansion):
				new_freq_plus = freq+(i+1)*resolution 
				new_freq_minus = freq-(i+1)*resolution 
				new_count_plus = int(count/normal.pdf(freq)*normal.pdf(new_freq_plus))
				new_count_minus = int(count/normal.pdf(freq)*normal.pdf(new_freq_minus))
				freqs.extend([new_freq_plus for i in range(new_count_plus)])
				freqs.extend([new_freq_minus for i in range(new_count_minus)])
		freqs.sort()
		mFile.write(line.split()[0]+" "+" ".join(map(str,freqs))+"\n")
	mFile.close()

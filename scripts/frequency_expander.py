import numpy as np
from scipy import stats
from math import floor, ceil
import sys


"""
Parameters 
llda_input_data: train data file to expand
neighborhood_expansion: number of neighbor channels to add to each side of the spectral line transition
spectrum_resolution: spectral emission lenght, base


*EMPIRICAL FREQUENCY BASE (SUPPORT)(SPECTRAL LINE BROADENING LENGTH): 0,002 [GHz]
"""

if (len(sys.argv) != 4):
	print("e.g. python frequency_expander.py hot_cores_full.dat 3 0.002")
	sys.exit() 

if (sys.argv[1].split('.')[0].split('_')[-1] == 'tr' or sys.argv[1].split('.')[0].split('_')[-1] == '1' or sys.argv[1].split('.')[0].split('_')[-1] == '2'):
	print("Cannot expand this data file")
	sys.exit()

llda_input_data = sys.argv[1]
neighboors = int(sys.argv[2])
support = sys.argv[3]

outputFile = llda_input_data.split('.')[0]+'_expanded'+'.'+llda_input_data.split('.')[1]

#Checking minimun spectral resolution (channeling > 2)
if (sys.argv[1].split('.')[0].split('_')[-1] == '3'):
	support = int(float(support)*1e3)
elif (sys.argv[1].split('.')[0].split('_')[-1] == '4'):
	support = int(float(support)*1e4)
elif (sys.argv[1].split('.')[0].split('_')[-1] == 'full'):
	support = int(float(support)*1e5)

counter = 0
with open(llda_input_data) as f:
	mFile = open(outputFile, 'w')
	for line in f:
		freqs = [int(freq) for freq in line.split()[1:]]

		freqs_count = [freqs.count(freq) for freq in freqs]
		freqs_dict = zip(freqs, freqs_count)
		
		#Aplying Gaussian Expansion
		for central_freq, central_freq_count in freqs_dict:
			normal = stats.norm(central_freq,support/6)
			
			for i in range(neighboors):
				#Getting new frequency neighboors
				new_freq_right = central_freq+(i+1)*(support/2)/neighboors 
				new_freq_left = central_freq-(i+1)*(support/2)/neighboors 
				
				#Getting Tf-idf of new frequency neighboors 
				new_count_right = int(central_freq_count/normal.pdf(central_freq)*normal.pdf(new_freq_right))
				new_count_left = int(central_freq_count/normal.pdf(central_freq)*normal.pdf(new_freq_left))
				
				freqs.extend([new_freq_right for i in range(new_count_right)])
				freqs.extend([new_freq_left for i in range(new_count_left)])
		freqs.sort()
		mFile.write(line.split()[0]+" "+" ".join(map(str,freqs))+"\n")
	mFile.close()

#Execution:
import numpy as np
import sys
import math
import os
import operator

if len(sys.argv) != 4:
	print("e.g. python llda_input_parser_CASA.no_shift.py casa_spectrum/spectrum.dat 2 244.93555")

spectral_file = os.path.basename(os.path.normpath(sys.argv[1]))
channeling = int(sys.argv[2])
rest_freq = float(sys.argv[3])

#spectral_file_out = filename+'_llda_input_CH-'+sys.argv[2]+'.dat'
spectral_file_out = "./spectrum_document.dat"

freq_list = []
energy_list = []
with open(spectral_file) as f:
	words = []
	for line in f:
		if not line[0].isdigit():
			continue

		lineSplit = line.split()
		freq = lineSplit[0].split('e')
		freq = float(freq[0])*10**int(freq[1])
		energy = lineSplit[1].split('e')
		energy = float(energy[0])*10**int(energy[1])
		freq_list.append(freq)
		energy_list.append(energy)
		#freq_list.append(int(math.ceil(float(freq[0])*(10**(float(freq[1])+int(sys.argv[2]))))))
		#energy_list.append(int(float(energy[0])*(10**float(energy[1]))))

data_list = zip(freq_list, energy_list)

#Frequency Red-Shiftting
freq_max, energy_max = max(data_list,key=operator.itemgetter(1))
#freq_delta = rest_freq-freq_max
#shifted_freq_list = [freq+freq_delta for freq in freq_list]

#Channeling
channeled_freq_list = [int(math.floor(freq*10**channeling)) for freq in freq_list]
#channeled_freq_list = [int(round(freq*10**channeling)) for freq in freq_list]

#Amplify intensity for spectrums with low intensity
if (energy_max < 1):
	print("Datacube with low intensity")
	energy_list = [energy*10 for energy in energy_list]

data_list = zip(channeled_freq_list, energy_list)

#Calculating Mean & Standard Deviation
energy_array = np.array(energy_list)
energy_mean = np.mean(energy_list)
energy_std = np.std(energy_array)

#TF Representation
words = []
for freq, energy in data_list:
	#tf = int(math.ceil(np.log2(energy))) if energy >= energy_std*3 else 0
	tf = int(math.ceil(np.log2(energy))) if energy >= 1 else 0	
	words.extend([str(freq) for i in range(tf)])
		
mFile_out = open(spectral_file_out,'w')
print("Generated File:")
print(" ".join(words)+"\n")
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()


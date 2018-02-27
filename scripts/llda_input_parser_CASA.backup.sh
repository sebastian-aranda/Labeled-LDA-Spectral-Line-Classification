#Execution:
#python llda_input_parser_CASA.py channeling[numeric]
import numpy as np
import sys
import math
import os
import operator

spectral_file = os.path.basename(os.path.normpath(sys.argv[1]))
filename = spectral_file[:-4]
#print("Parsing "+filename)
#spectral_file_out = filename+'_llda_input_CH-'+sys.argv[2]+'.dat'
spectral_file_out = "./spectrum_document.dat"

channeling = int(sys.argv[2])

freq_list = []
energy_list = []
with open(spectral_file) as f:
	words = []
	for line in f:
		if not line[0].isdigit():
			continue
		lineSplit = line.split(" ")
		freq = lineSplit[0].split('e')
		energy = lineSplit[1].split('e')
		freq_list.append(int(math.ceil(float(freq[0])*(10**(float(freq[1])+channeling)))))
		energy_list.append(int(float(energy[0])*(10**float(energy[1]))))

#print("Energy list...")
#print(energy_list)
data_list = zip(freq_list, energy_list)

freq_max, energy_max = max(data_list,key=operator.itemgetter(1))
if energy_max < 1:
	energy_list = [energy*10 for energy in energy_list]

#Calculating Standard Deviation
energy_array = np.array(energy_list)
energy_std = np.std(energy_array)

#print("Energy std: "+str(energy_std))

#TF Representation
words = []
for freq, energy in data_list:
	tf = 0
	#if energy > 3*energy_std:
	#	tf = int(np.floor(np.log2(energy)) + 1)
	tf = int(math.ceil(np.log2(energy) if energy >= 1 else 0))
	words.extend([str(freq) for i in range(tf)])
		

print("Generated File")
print(" ".join(words)+"\n")
mFile_out = open(spectral_file_out,'w')
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()

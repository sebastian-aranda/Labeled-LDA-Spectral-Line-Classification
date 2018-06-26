import sys
import math

fileName = sys.argv[1]
channeling = int(sys.argv[2])
with open(fileName) as f:
	for i,line in enumerate(f):
		if i < 1:
			continue
		tokens = line.split(':')
		chemical = tokens[1]
		
		freq = float(tokens[2].split(',')[0].strip())
		#freq = int(math.floor(freq*10**channeling))
		#freq = int(math.ceil(freq*10**channeling))
		freq = int(round(freq*10**channeling))
		energy_lower_kelvin = int(float(tokens[-2]))
		print(chemical+"\t"+str(freq)+"\t"+str(energy_lower_kelvin))
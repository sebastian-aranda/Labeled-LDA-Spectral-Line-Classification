#Execution:
#python llda_input_parser_CASA.py channeling[numeric]
import numpy as np
import sys
import tarfile
from subprocess import call

#Arguments
#sys.argv[1]: file_name.theta
#sys.argv[2]: model_labelmap.sub

#print("Extracting (gunzip) "+sys.argv[1])
call("gunzip "+sys.argv[1], shell=True)

#PARA UN SOLO DOCUMENTO -> 1 sola linea
#print("Reading "+sys.argv[1][:-3])
probabilities = []
with open(sys.argv[1][:-3]) as f:
	data = f.readline()
	data = data.split()
	probabilities = [float(prob.split(':')[1]) for prob in data]

#Obteniendo Labels
chemicals = []
with open(sys.argv[2], 'r') as f:
	for line in f:
		chemicals.append(line.strip())

result = zip(chemicals, probabilities)
result_sorted = sorted(result, key=lambda x: -float(x[1]))
#result_sorted = sorted(result, key=lambda x: x[1], reverse=True)

for i,result in enumerate(result_sorted):
	chem, prob = result
	print(str(i+1)+';'+chem+';'+str(prob))

#print("Ziping (gzip) "+sys.argv[1][:-3])
call('gzip '+sys.argv[1][:-3],shell=True)

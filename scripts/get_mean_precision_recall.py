import sys
import os

from collections import defaultdict

if (len(sys.argv) < 2):
	print("e.g. python get_mean_precision_recall.py results.csv")
	sys.exit(1)

results_file = sys.argv[1]

precision_array = [] 
recall_array = []
with open(results_file) as f:
	for line in f:
		#spectral_window = ".".join(line.split(',')[0].split('.')[:2])
		#model = line.split(',')[0].split('.')[2]
		spec_window_model = line.split(',')[0]
		precision = float(line.split(',')[1].strip())
		recall = float(line.split(',')[2].strip())
		
		precision_array.append(precision)
		recall_array.append(recall)

print(spec_window_model+","+str(sum(precision_array)/len(precision_array))+","+str(sum(recall_array)/len(recall_array)))


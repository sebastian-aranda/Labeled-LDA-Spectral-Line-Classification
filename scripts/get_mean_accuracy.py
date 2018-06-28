import sys
import os

from collections import defaultdict

if (len(sys.argv) < 3):
	print("e.g. python get_mean_accuracy.py results.csv 10")
	sys.exit(1)

results_file = sys.argv[1]
iterations = int(sys.argv[2])

matches_dict = defaultdict(float) 
with open(results_file) as f:
	for line in f:
		model = line.split(',')[0]
		accuracy = float(line.split(',')[1].strip())
		matches_dict[model] += accuracy

for model, accuracy_sum in matches_dict.iteritems():
	print(model+","+str(accuracy_sum/iterations))

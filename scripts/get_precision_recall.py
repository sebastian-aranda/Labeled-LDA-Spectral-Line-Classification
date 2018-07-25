import sys
import os
from collections import Counter

if (len(sys.argv) < 4):
	print("e.g. python get_precision_recall.py spectrum.model.output topN relevant_species_ids")
	sys.exit(1)

prediction_file = sys.argv[1]
fileName = os.path.basename(os.path.normpath(prediction_file))
# results_path = sys.argv[1]
topN = int(sys.argv[2])
relevant_species = sys.argv[3]

# results = [os.path.join(dp, f) for dp, dn, filenames in os.walk(results_path) for f in filenames]
# results_models = [".".join(result.split('/')[-1].split('.')[:-1]) for result in results if "model" in result]

TP = 0
FP = 0
FN_plus_TP = len(relevant_species.split(','))
with open(prediction_file) as f:
	last_pos = f.tell()
	last_line = f.readlines()[-1]
	f.seek(last_pos)
	for i,line in enumerate(f):
		if i >= topN:
			break;

		no = line.split()[0].split(';')[1]
		transition_name = " ".join(line.split(';')[1].split()[1:])
		prob = line.split()[-1].split(';')[1]
		last_prob = last_line.split()[-1].split(';')[1]

		if no in relevant_species and prob != last_prob:
			TP += 1
		elif no not in relevant_species and prob != last_prob:
			FP += 1

print("TP: "+str(TP)+" FP: "+str(FP)+" Relevant: "+str(FN_plus_TP))

#Calculating Precision & Recall
precision = TP/float(TP+FP)
recall = TP/float(FN_plus_TP)

print(fileName+","+str(precision)+","+str(recall))
import sys
import os
from collections import Counter

if (len(sys.argv) < 2):
	print("e.g. python get_accuracy.py path/to/results [model_name]")
	sys.exit(1)

# def get_immediate_subdirectories(a_dir):
#     return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

#Retrieve trained models
# models = get_immediate_subdirectories('./llda_models/')
results = [os.path.join(dp, f) for dp, dn, filenames in os.walk(sys.argv[1]) for f in filenames]
results_models = [result.split('.')[-2] for result in results if "model" in result]
results_count = Counter(results_models)

#Create dict
match_count = dict()
for model in results_models:
	match_count[model] = 0

total_matches = 0

os.chdir(sys.argv[1])
if not os.path.isfile('matches.out'):
	print('[Error] Matches not found')

with open('matches.out') as f:
	for line in f:
		total_matches += 1 if "MATCH" in line else 0
		for model, total in results_count.most_common():
			if model in line:
				match_count[model] += 1

if (len(sys.argv) == 2):
	for result_model, total in results_count.most_common():
		mAccuracy = float(match_count[result_model])/total
		#print("Accuracy["+result_model+"]: "+str(match_count[result_model])+"/"+str(results_count[result_model])+" = "+str(mAccuracy))
		print("_".join(result_model.split('_')[1:-1])+","+str(mAccuracy))
		#print("Total Matches for "+sys.argv[1]+": "+str(total_matches)+"\n")
else:
	for result_model, total in results_count.most_common():
		if sys.argv[2] not in result_model:
			continue
		try:
			mAccuracy = float(match_count[result_model])/results_count[result_model]
			print("Accuracy["+result_model+"]: "+str(match_count[result_model])+"/"+str(results_count[result_model])+" = "+str(mAccuracy))
		except:
			print("[Error]:"+str(sys.exc_info()[0]))
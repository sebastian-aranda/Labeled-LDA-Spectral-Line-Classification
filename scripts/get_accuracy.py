import sys
import os
from collections import Counter

if (len(sys.argv) != 2):
	print("e.g. get_accuracy path/to/results")
	sys.exit(1)

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

models = get_immediate_subdirectories('./llda_models/')

results = [os.path.join(dp, f) for dp, dn, filenames in os.walk(sys.argv[1]) for f in filenames]
results_models = [result.split('.')[-2] for result in results if "model" in result]
results_count = Counter(results_models)

match_count = dict()
for model in models:
	match_count[model] = 0
total_matches = 0

os.chdir(sys.argv[1])
with open('matches.out') as f:
	for line in f:
		total_matches += 1
		for model in models:
			if model in line:
				match_count[model] += 1


for result_model, total in results_count.most_common():
	print("Accuracy["+result_model+"]: "+str(match_count[result_model])+"/"+str(results_count[result_model])+" = "+str(float(match_count[result_model])/results_count[result_model]))

print(total_matches)
import sys
import os
import itertools

if (len(sys.argv) != 2):
	exit(0)

input_model = sys.argv[1]

files = [file for file in os.listdir('.') if file[0] != '.' and file.split('.')[-1] == 'output']
files.sort()
objects = list(set(['.'.join(file.split('.')[:-2]) for file in files]))

if input_model != 'test':
	models = ['model_'+input_model+'_tr_500it','model_'+input_model+'_2_500it','model_'+input_model+'_full_500it','model_'+input_model+'_full_expanded_00002_500it','model_'+input_model+'_full_expanded_00010_500it','model_'+input_model+'_full_expanded_00200_500it']
else:
	models = ['model_test_2_500it']

targets = list(itertools.product(objects,models))
for obj,model in targets:
        file = obj+'.'+model+'.output'
        with open(file) as f:
                for i,line in enumerate(f):
                        if i >= 5:
                                break
                        print(obj+";"+model+";"+line.rstrip('\n'))

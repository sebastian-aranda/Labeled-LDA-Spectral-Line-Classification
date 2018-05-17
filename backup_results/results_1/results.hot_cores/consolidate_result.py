import sys
import os
import itertools

input_model = sys.argv[1]

files = [file for file in os.listdir('.') if file.split('.')[-1] == 'output']
files.sort()
objects = list(set(['.'.join(file.split('.')[:-2]) for file in files]))
#objects = ['DMTAU','DMTAU2','HD163296','IRC2', 'IRS43']
models = ['model_'+input_model+'_tr_500it','model_'+input_model+'_2_500it','model_'+input_model+'_full_500it','model_'+input_model+'_full_expanded_500it']

targets = list(itertools.product(objects,models))
for obj,model in targets:
        file = obj+'.'+model+'.output'
        print(file)
        with open(file) as f:
                for i,line in enumerate(f):
                        if i >= 5:
                                break
                        print(line.rstrip('\n'))

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys

import pickle

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)

#Results Beta
#file = "./results_casted_beta/results.accuracy.results_tfv1.1.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv1.1.2_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv1.2.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv1.2.2_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.1.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.1.2_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.2.1_C_1.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.2.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.2.1_C_3.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.2.1_C_3.5.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv2.2.2_C_3.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv3.1.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv3.1.2_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv3.2.1_C_2.0.csv"
#file = "./results_casted_beta/results.accuracy.results_tfv3.2.2_C_2.0.csv"

#Final results
#file = "./results_shifted_all_10it/results.accuracy.mean.csv"
#file = "./results_shifted_expanded_10it/results.accuracy.mean.csv"
file = "./results_casted_all_10it/results.accuracy.mean.csv"
#file = "./results_casted_expanded_10it/results.accuracy.mean.csv"

#Obtain models info
model_names = list()
model_accuracys = list()
with open(file) as f:
    for line in f:
        tokens = line.split(',')
        model_names.append(tokens[0])
        model_accuracys.append(float(tokens[1].rstrip()))

#Obtain models metadata
models_metadata = dict()
for model in model_names:
	models_metadata[model] = dict()

pickle_models_filename = 'models_metadata.dmp'

if not os.path.isfile(pickle_models_filename):
	print("Reading models metadata...")
	#Obtain number of features (vocabulary) per model
	for i,model in enumerate(model_names):
	    with open('./llda_train_input/'+model+'_features.dat') as f:
	        line = f.readline()
	        models_metadata[model]['vocabulary_len'] = len(line.split())
	#Obtain number of tokens per model
	for model in model_names:
	    #model_data = "_".join(model.split('_')[:-1]) if "expanded" not in model else "_".join(model.split('_')[:-3]) 
	    with open('./llda_train_input/'+model+'.dat') as f:
	        tokens_count = 0
	        for line in f:
	                tokens_count += len(line.split())
	        models_metadata[model]['tokens_len'] = tokens_count

	#Obtain number of topics per model
	for model in model_names:
	    if 'expanded' in model:
	        tokens = model.split('_expanded')
	        labelmap_path = './llda_train_input/'+tokens[0]+'_labelmap.sub'
	    else:
	        labelmap_path = './llda_train_input/'+model+'_labelmap.sub'
	    
	    with open(labelmap_path) as f:
	        topics_count = 0
	        for line in f:
	        	topics_count += 1
	        models_metadata[model]['topics_count'] = topics_count

	pickleout = open(pickle_models_filename,'wb')
	pickle.dump(models_metadata,pickleout)
	pickleout.close()
else:
	print("Recovering models metadata from pickle dump...")
	picklein = open(pickle_models_filename,'rb')
	models_metadata = pickle.load(picklein)
	picklein.close()
    
model_vocabulary_len = []
model_tokens_len = []
model_topics_len = []
for model in model_names:
    model_vocabulary_len.append(models_metadata[model]['vocabulary_len'])
    model_tokens_len.append(models_metadata[model]['tokens_len'])
    model_topics_len.append(models_metadata[model]['topics_count'])
    

results = zip(model_names, model_accuracys, model_vocabulary_len, model_tokens_len, model_topics_len)

results_tr = list()
results_2 = list()
results_full = list()

results_full_ex3_00050 = list()
results_full_ex3_00100 = list()
results_full_ex3_01000 = list()

for model, accuracy, vlen, tlen, topics in results:
    if model.endswith('tr'):
        results_tr.append((model,accuracy,vlen,tlen, topics))
    elif model.endswith('2'):
        results_2.append((model,accuracy,vlen,tlen, topics))
    elif model.endswith('full'):
        results_full.append((model,accuracy,vlen,tlen, topics))
    elif model.endswith('full_expanded_00050_x3'):
        results_full_ex3_00050.append((model,accuracy,vlen,tlen, topics))
    elif model.endswith('full_expanded_00100_x3'):
        results_full_ex3_00100.append((model,accuracy,vlen,tlen, topics))
    elif model.endswith('full_expanded_01000_x3'):
        results_full_ex3_01000.append((model,accuracy,vlen,tlen, topics))

axes_list = []
def plotScoreBars(results,rows,cols,subplot, title=""):
    axes = plt.gca()
    
    res_sortedby_vocabulary_len = sorted(results,key=lambda x: x[2])
    res_sortedby_tokens_len = sorted(results,key=lambda x: x[3])
    res_sortedby_topics_len = sorted(results,key=lambda x: x[4])
    
    x = range(len(results))
    
    mPlot = plt.subplot(rows,cols,subplot,sharex=axes_list[0]) if len(axes_list) > 0 else plt.subplot(rows,cols,subplot)
    axes_list.append(mPlot)

    if subplot < 5:
    	plt.setp(mPlot.get_xticklabels(), visible=False)
    	
    # if subplot == 4:
    # 	plt.text(-0.5, .9, r'$\tau = 0.00050 [GHz]$')
    # elif subplot == 5:
    # 	plt.text(-0.5, .9, r'$\tau = 0.00100 [GHz]$')
    # elif subplot == 6:
    # 	plt.text(-0.5, .9, r'$\tau = 0.01000 [GHz]$')

    plt.bar(x, [i[1] for i in res_sortedby_tokens_len], align='center')
    if subplot%2 == 1:
    	plt.ylabel('Accuracy Score')
    #plt.title(title+'(sorted by n° of tokens)')
    plt.title(title)
    plt.xticks(x, ['_'.join(i[0].split('_')[:-1]) if "expanded" not in i[0] else '_'.join(i[0].split('_')[:-4]) for i in res_sortedby_tokens_len],rotation='vertical')
    plt.ylim(0, 1)
    mPlot.tick_params(axis='both', which='major', labelsize=10)

    return axes 
    
    #plt.subplot(rows,cols,subplot+3)
    #plt.bar(x, [i[1] for i in res_sortedby_topics_len], align='center')
    #plt.ylabel('Accuracy Score')
    #plt.title(title+'(sorted by n° of topics)')
    #plt.xticks(x, ['_'.join(i[0].split('_')[:-1]) if "expanded" not in i[0] else '_'.join(i[0].split('_')[:-4]) for i in res_sortedby_topics_len],rotation='vertical')
    #plt.ylim(0, 1)

plt.close('all')
plt.figure(figsize=(6,2))
# plt.figure()

plotScoreBars(results_tr,1,3,1,"Truncated models")
plotScoreBars(results_2,1,3,2,"Medium models")
plotScoreBars(results_full,1,3,3,"Full models")

#plotScoreBars(results_full_ex3_00050,3,2,4,r"Expanded $\tau$"+" = 0.0005 [GHz]")
#plotScoreBars(results_full_ex3_00100,3,2,5,r"Expanded $\tau$"+" = 0.001 [GHz]")
#plotScoreBars(results_full_ex3_01000,3,2,6,r"Expanded $\tau$"+" = 0.01 [GHz]")

#left_plots = [x for i,x in enumerate(axes_list) if i%2 == 0]
#right_plots = [x for i,x in enumerate(axes_list) if not i%2 == 0]

plt.tight_layout()
plt.show()
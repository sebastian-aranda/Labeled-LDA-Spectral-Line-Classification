import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys

import pickle

font = {'family' : 'sans-serif',
        #'weight' : 'bold',
        'size'   : 14}

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

#file = "./results_casted_all_10it/results.accuracy.all.top1.mean.csv"
file = "./results_casted_alma_10it/results.accuracy.all.top1.mean.csv"

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


def plotScoreBars(results,title=""):
    axe = plt.gca()

    bars_list = []
    bar_width = 0.2
    for i,r in enumerate(results):
        res_sortedby_vocabulary_len = sorted(r,key=lambda x: x[2])
        res_sortedby_tokens_len = sorted(r,key=lambda x: x[3])
        res_sortedby_topics_len = sorted(r,key=lambda x: x[4])

        print(res_sortedby_vocabulary_len)

        x = np.asarray(range(len(r)))
        mPlot = plt.bar(x+i*bar_width, [i[1] for i in res_sortedby_tokens_len], width = bar_width, align='center')[0]
        bars_list.append(mPlot)
    
    plt.title('Accuracy@1')
    plt.ylabel('Score')
    plt.xticks(x+bar_width, ['_'.join(i[0].split('_')[:-1]) if "expanded" not in i[0] else '_'.join(i[0].split('_')[:-4]) for i in res_sortedby_tokens_len],rotation='vertical')
    plt.ylim(0, 1)
    plt.yticks(np.arange(0, 1.1, 0.2))
    plt.legend(tuple(bars_list),title, loc=4)

plt.figure(figsize=(7,5))
#plotScoreBars([results_tr,results_2,results_full],("truncated","medium","full"))
plotScoreBars([results_full_ex3_00050,results_full_ex3_00100,results_full_ex3_01000],(r"Exp $\tau = 0.0005 [GHz]$, $\chi = 3$",r"Exp $\tau = 0.0010 [GHz]$, $\chi = 3$",r"Exp $\tau = 0.0100 [GHz]$, $\chi = 3$"))

plt.tight_layout()
plt.show()
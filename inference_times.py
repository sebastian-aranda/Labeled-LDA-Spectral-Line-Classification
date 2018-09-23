import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import sys
import os
from collections import defaultdict

import pickle

font = {'family' : 'sans-serif',
        #'weight' : 'bold',
        'size'   : 14}

matplotlib.rc('font', **font)

time_results = []

#Obtain times from inference output
filename = './results_casted_all_10it/nohup.out'
fitsname = ''
modelname = ''
with open(filename) as f:
    for line in f:
        fitsname = line.split(":")[1].strip()[11:] if "Parsing Fits:" in line else fitsname
        modelname = line.split(":")[1].strip()[6:-6] if "Used model:" in line else modelname 
        
        if "Parsing time" in line:
            exectime = dict()
            exectime['parser'] = float(line.split(":")[1].split()[0])
        elif "L-LDA inference time" in line:
            exectime['llda'] = float(line.split(":")[1].split()[0])
        elif "Total execution time" in line:
            exectime['total'] = float(line.split(":")[1].split()[0])
            time_results.append((fitsname, modelname,exectime))
        
#Obtain models metadata
model_names = list(set([model for fits,model,exectime in time_results if model != '']))
#models_metadata = defaultdict(lambda: defaultdict(int))
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

#Obtain FITS metadata
fits_names = list(set([fits for fits,model,exectime in time_results]))
fits_metadata = defaultdict(int)

fits_metadata['HD163296_CO_2_1.image.fits'] = 432*432*250
fits_metadata['uid___A002_Xa916fc_X668__IRS43_HCO32.final.image.pbcor.fits'] = 512*512*400
fits_metadata['uid___A002_Xa916fc_X668__IRS43_HCO32.final.image.pbcor.v2.fits'] = 512*512*400
fits_metadata['Orion.HNC.cbc.contsub.image.fits'] = 450*450*121
fits_metadata['Orion.HNC.cbc.contsub.image.v2.fits'] = 450*450*121
fits_metadata['DMTau.CS_5-4.image.fits'] = 420*420*330
fits_metadata['Orion.methanol.cbc.contsub.image.fits'] = 100*100*41
fits_metadata['Orion.methanol.cbc.contsub.image.v2.fits'] = 100*100*41
fits_metadata['TWHydra_CO3_2line.image.fits'] = 100*100*118
fits_metadata['TWHydra_HCOplusline.image.fits'] = 100*100*118
fits_metadata['TWHydra_HCOplusline.image.v2.fits'] = 100*100*118

#Getting Times
llda_times_dict = defaultdict(lambda: defaultdict(lambda: list()))
parser_times_dict = defaultdict(lambda: defaultdict(lambda: list()))
total_time_dict = defaultdict(lambda: defaultdict(lambda: list()))

for fitsname, modelname, exectime in time_results:
    llda_times_dict[modelname][fitsname].append(exectime['llda'])
    parser_times_dict[modelname][fitsname].append(exectime['parser'])
    total_time_dict[modelname][fitsname].append(exectime['total'])

llda_average_times_fits = [(model,fits,sum(times)/float(len(times))) for model, fits_dict in llda_times_dict.items() for fits, times in fits_dict.items()]

llda_average_times_models = dict()
for model in model_names:
	llda_average_times_models[model] = sum([x[2] for x in llda_average_times_fits if model == x[0]])
llda_average_times_models = [(model,time) for model, time in llda_average_times_models.items()]
llda_average_times_models.sort(key = lambda x: x[1])

fig = plt.figure(figsize=(10,4))
filters = list(set(['_'.join(model.split('_')[:-1]) if "expanded" not in model else '_'.join(model.split('_')[:-4]) for model in model_names]))

def plotModelsTimes(data,subplot_params):
	plt.subplot(subplot_params[0],subplot_params[1],subplot_params[2])
	mPlot, = plt.plot([models_metadata[model]['tokens_len'] for model, time in data],[time for model, time in data], label=mFilter)
	#mPlot = plt.scatter([models_metadata[model]['tokens_len'] for model, time in data],[time for model, time in data])
	plt.title(plotTitle)
	plt.ylabel("Elapsed time [s]")
	#plt.ylabel("Tiempo transcurrido (elapsed time) [s]")
	#plt.xticks(range(len(llda_average_times_models)),[model.split("_")[-1] if "expanded" not in model else "e"+model.split("_")[-2]  for model,time in llda_average_times_models], rotation = 'vertical')
	plt.xlabel("Number of training words")
	#plt.xlabel("Cantidad de palabras de entrenamiento")
	#plt.xscale('log')

	return mPlot

# for i, mFilter in enumerate(filters):
# 	dataPlot = [(x[0],x[2]) for x in llda_average_times_fits if mFilter in x[0]]
# 	plotModelsTimes(dataPlot,(7,2,i+1))

print(model_names)

plotTitle = "Inference Time for Standard Models"
standard_plots = []
mFilter = 'tr'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
standard_plots.append(plotModelsTimes(dataPlot,(1,2,1)))

mFilter = '2'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
standard_plots.append(plotModelsTimes(dataPlot,(1,2,1)))

mFilter = 'full'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
standard_plots.append(plotModelsTimes(dataPlot,(1,2,1)))

ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
ax.get_xaxis().get_major_formatter().set_powerlimits((-3,3))
ax.get_xaxis().get_major_formatter().set_scientific(True)
plt.legend(handles=standard_plots)

plotTitle = "Inference Time for Expanded Models"
expanded_plots = []
mFilter = '00050_x3'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
expanded_plots.append(plotModelsTimes(dataPlot,(1,2,2)))

mFilter = '00100_x3'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
expanded_plots.append(plotModelsTimes(dataPlot,(1,2,2)))

mFilter = '01000_x3'
dataPlot = [(x[0],x[1]) for x in llda_average_times_models if x[0].endswith(mFilter)]
expanded_plots.append(plotModelsTimes(dataPlot,(1,2,2)))

ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
ax.get_xaxis().get_major_formatter().set_powerlimits((-3,3))
ax.get_xaxis().get_major_formatter().set_scientific(True)
plt.legend(handles=expanded_plots)

plt.tight_layout()
plt.show()

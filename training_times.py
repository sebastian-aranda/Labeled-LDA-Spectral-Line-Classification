import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import sys
import os
from collections import defaultdict

import matplotlib.ticker as ticker

font = {'family' : 'sans-serif',
        #'weight' : 'bold',
        'size'   : 14}

matplotlib.rc('font', **font)

training_times = []
file = 'training_times.dat'
with open(file) as f:
    for line in f:
        tokens = line.split()
        training_times.append((tokens[0], int(tokens[1][3:]),int(tokens[2][2:]),int(tokens[3][2:-1]),float(tokens[5].replace(",","."))))
# print(training_times)

models = ['tr','2','full','expanded_00050','expanded_00100','expanded_01000']
training_times.sort(key = lambda x: x[2])
#training_times.sort(key = lambda x: (x[2],x[1]))
fig = plt.figure(figsize=(10,4))
for i,model in enumerate(models):
    if i == 0:
        fits_plots = []
        plt.subplot(1,2,1)
    elif i == 3:
        fits_plots = []
        plt.subplot(1,2,2)
    
    training_times_plot = [x for x in training_times if x[0].endswith(model)]
    mPlot, = plt.plot([x[2] for x in training_times_plot],[x[4] for x in training_times_plot], label = model)
    fits_plots.append(mPlot)
    
    if i == 2:
        #plt.title("Standard models")
        plt.title("Modelos Clásicos")
        #plt.xlabel("Number of training words")
        plt.xlabel("Cantidad de palabras de entrenamiento")
        #plt.ylabel("Elapsed time [s]")
        plt.ylabel("Tiempo transcurrido (elapsed time) [s]")
        plt.axis([0, training_times_plot[-1][2], 0, training_times_plot[-1][4]])
        #plt.xscale("log")
        plt.legend(handles=fits_plots)
        ax = plt.gca()
        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        ax.get_xaxis().get_major_formatter().set_powerlimits((-3,3))
        ax.get_xaxis().get_major_formatter().set_scientific(True)
    elif i == 5:
        #plt.title("Expanded models")
        plt.title("Modelos expandidos")
        #plt.xlabel("Number of training words")
        plt.xlabel("Cantidad de palabras de entrenamiento")
        #plt.ylabel("Elapsed time [s]")
        plt.ylabel("Tiempo transcurrido (elapsed time) [s]")
        plt.axis([0, training_times_plot[-1][2], 0, training_times_plot[-1][4]])
        #plt.xscale("log")
        plt.legend(handles=fits_plots)
        ax = plt.gca()
        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        ax.get_xaxis().get_major_formatter().set_powerlimits((-3,3))
        ax.get_xaxis().get_major_formatter().set_scientific(True)

##################################################################
# fits_plots = []
# for i,model in enumerate(models):
#     training_times_plot = [x for x in training_times if x[0].endswith(model)]
#     mPlot, = plt.plot([x[2] for x in training_times_plot],[x[4] for x in training_times_plot], label = model)
#     fits_plots.append(mPlot)

#plt.title("Expanded models")
#plt.title("Modelos expandidos")
#plt.xlabel("Number of training words")
# plt.xlabel("Cantidad de palabras de entrenamiento")
#plt.ylabel("Elapsed time [s]")
# plt.ylabel("Tiempo transcurrido (elapsed time) [s]")
#plt.axis([0, training_times_plot[-1][2], 0, training_times_plot[-1][4]])
# plt.xscale("log")
# plt.legend(handles=fits_plots)

plt.tight_layout()
plt.show()

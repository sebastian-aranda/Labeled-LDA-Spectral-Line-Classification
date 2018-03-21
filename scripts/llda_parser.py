import astropy.units as u
import numpy as np
from astropy.io import fits

import math
import os
import operator
import sys

from sklearn.cluster import DBSCAN

if len(sys.argv) != 3:
        print("e.g. python llda_parser.py fits_file.fits 2")
        sys.exit(0)

fileName = sys.argv[1]
#fileName = os.path.basename(os.path.normpath(sys.argv[1]))
channeling = int(sys.argv[2])

spectral_file_out = "./spectrum_document.dat"
c = 299792458

print("Parsing Fits: "+fileName)
hdulist = fits.open(fileName)
hdu_primary = hdulist[0]
hdu_header = hdu_primary.header
hdu_data = hdu_primary.data

data_array = hdu_data[0,:,:,:] if hdu_header['NAXIS'] == 4 else hdu_data 

naxis1 = hdu_header['NAXIS1'] #Ra
naxis2 = hdu_header['NAXIS2'] #Dec
naxis3 = hdu_header['NAXIS3'] #Frequency
rest_freq = hdu_header['RESTFRQ'] #Rest freq

#Determining regions of interest

def collapseImage(args):
       lenX = args[0]
       lenY = args[1]
       nchan = args[2]
       dataa = args[3]
       #print("Collapsing Image, parameters  lenX:" +str(lenX) + " lenY: "+str(lenY)+" nchan: "+str(nchan)+" dataa: "+str(dataa.shape))
       collapsedImage = np.zeros((lenX,lenY), dtype=np.float)
       for slice in dataa:
           collapsedImage = np.add(collapsedImage,slice)
       return collapsedImage

list_of_args = [(naxis1,naxis2,naxis3,data_array)]
collapsedImages = [collapseImage(args) for args in list_of_args]
rms = np.sqrt(np.mean(np.square(collapsedImages[0])))

negValues = []
regionPoints = []
for i in range(naxis1):
    for j in range(naxis2):
        value = collapsedImages[0][i][j]
        if value < 3*rms:
            negValues.append(value)
        else:
            regionPoints.append([i,j])

db = DBSCAN(eps=int(0.1*naxis1), min_samples=4).fit(regionPoints)
result_labels = db.labels_
n_clusters_ = len(set(result_labels)) - (1 if -1 in result_labels else 0)
unique_labels = set(result_labels)
#print('Estimated number of clusters: %d' % n_clusters_)

clusteredPoints = []
for i,point in enumerate(regionPoints):
    currentCluster = result_labels[i]
    if currentCluster == -1:
        continue
    else:
        clusteredPoints.append([point,currentCluster])

clusters_intensity = []
for cluster in range(n_clusters_):
    points = [t[0] for t in clusteredPoints if t[1] == cluster]
    intensity_array = []

    for chan in range(naxis3):
        sumValues = 0.0
        for point in points:
            sumValues = sumValues + data_array[chan,point[0],point[1]]
        intensity_array.append(sumValues)
    
    intensitiy_values = np.array(intensity_array)
    clusters_intensity.append(intensitiy_values)
    
    #sumValues = np.sum(intensitiy_values)
    #avgJ = np.mean(intensitiy_values)
    #sigma = np.std(intensitiy_values)
    #threeSigma= 2.5*sigma

#print("SumValues\n"+str(list(map(np.sum,clusters_intensity))))
#print("Avg\n"+str(list(map(np.mean,clusters_intensity))))
#print("Sigma\n"+str(list(map(np.std,clusters_intensity))))

clusters_intensity_sum = list(map(np.sum,clusters_intensity))
cluster_index_selected = clusters_intensity_sum.index(max(clusters_intensity_sum))
intensitiy_values = clusters_intensity[cluster_index_selected]
intensitiy_values = [intensitiy_value/sum(intensitiy_values) for intensitiy_value in intensitiy_values]
#intensitiy_values = [intensitiy_value/(intensitiy_values) for intensitiy_value in intensitiy_values]

freq_list = []
energy_list = []

for n_chan in range(len(data_array)):
    freq = float(hdu_header['CRVAL3']+hdu_header['CDELT3']*n_chan)
    
    mLambda = c/freq
    theta_square = hdu_header['BMAJ']*hdu_header['BMIN']
    intensity = intensitiy_values[n_chan]
    #intensity = int(np.sum(data_array[n_chan])) if np.sum(data_array[n_chan]) > 0 else 0 #Revisar
    energy_kelvin = 1.36*((mLambda*100)**2)/(theta_square*3600**2)*(intensity*1000)
    
    #print("F:"+str(freq)+" - I:"+str(intensity)+" - K:"+str(energy_kelvin))
    freq_list.append(freq)
    energy_list.append(energy_kelvin)

data_list = zip(freq_list, energy_list)

#Frequency Red-Shiftting
freq_max, energy_max = max(data_list,key=operator.itemgetter(1))
redshift = (rest_freq-freq_max)/freq_max
#print("Redshift: "+str(redshift)+" Restfreq of spectral line: "+str(rest_freq))
shifted_freq_list = [freq*(1+redshift) for freq in freq_list]

#print("Freq/Energy Max: "+str(freq_max)+"/"+str(energy_max))

#Channeling
channeled_freq_list = [int(math.floor(freq/10**(9-channeling))) for freq in shifted_freq_list]

#Amplify intensity for spectrums with low intensity
if (energy_max < 1):
        print("Low energy cube. Amplifying Energy List x4")
        energy_list = [energy*5 for energy in energy_list]

data_list = zip(channeled_freq_list, energy_list)

#Calculating Mean & Standard Deviation
energy_array = np.array(energy_list)
energy_mean = np.mean(energy_list)
energy_std = np.std(energy_array)

#TF Representation
words = []
for freq, energy in data_list:
        tf = int(math.ceil(np.log2(energy))) if energy >= 1 else 0
        #tf = int(math.ceil(np.log2(energy))) if energy >= energy_std*3 else 0
        words.extend([str(freq) for i in range(tf)])

mFile_out = open(spectral_file_out,'w')
print("Generated File:")
print(" ".join(words)+"\n")
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()
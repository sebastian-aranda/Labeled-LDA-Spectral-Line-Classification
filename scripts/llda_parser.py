import astropy.units as u
import numpy as np
from astropy.io import fits

import math
import os
import operator
import sys

if len(sys.argv) != 3:
        print("e.g. python llda_parser.py fits_file.fits 2")
        sys.exit(0)

fileName = sys.argv[1]
#fileName = os.path.basename(os.path.normpath(sys.argv[1]))
channeling = int(sys.argv[2])

spectral_file_out = "./spectrum_document.dat"
c = 299792458

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
"""
def collapseImage(args):
       lenX = args[0]
       lenY = args[1]
       nchan = args[2]
       dataa = args[3]
       print "Collapsing Image, parameters  lenX:" +str(lenX) + " lenY: "+str(lenY)+" nchan: "+str(nchan)+" dataa: "+str(dataa.shape)
       collapsedImage = np.zeros((lenX,lenY), dtype=np.float)
       for slice in dataa:
           collapsedImage = np.add(collapsedImage,slice)
       return collapsedImage

list_of_args = [(naxis1,naxis2,naxis3,data_array)]
collapsedImages = [collapseImage(args) for args in list_of_args]
rms = np.sqrt(np.mean(np.square(collapsedImages[0])))

plotValues=np.ndarray((naxis1,naxis2),float)
negValues = []
regionPoints = []
for i in range(naxis1):
    for j in range(naxis2):
        value = collapsedImages[0][i][j]
        if value < 3*rms:
            negValues.append(value)
            plotValues[i][j] = 0
        else:
            plotValues[i][j] = value
            regionPoints.append([i,j])
        j = j+1
    i = i+1

db = DBSCAN(eps=int(0.1*head['NAXIS1']), min_samples=4).fit(regionPoints)
result_labels = db.labels_
n_clusters_ = len(set(result_labels)) - (1 if -1 in result_labels else 0)
unique_labels = set(result_labels)
print('Estimated number of clusters: %d' % n_clusters_)
#cmap = get_cmap(n_clusters_+1)

for point in regionPoints:
    currentCluster = result_labels[i]
    if currentCluster == -1:
        #col = 'k'
        col = 'white'
    else:
        #col = cmap(currentCluster)
        clusteredPoints.append([point,currentCluster])
    #print "Point: "+str(point)+" Cluster: "+str(result_labels[i])
    #plt.plot(int(point[1]),int(point[0]),marker='o', markerfacecolor=col)
    #if currentCluster <> previousCluster:
    #    if currentCluster <> -1:    
    #        lbls.append(mpatches.Patch(color=col, label=currentCluster))
    #        previousCluster = currentCluster
    #i = i+1

for cluster in range(n_clusters_):
    points = [t[0] for t in clusteredPoints if t[1] == cluster]
    intensity_array = []

    for chan in range(naxis3):
        sumValues = 0.0
        for point in points:
            sumValues = sumValues + dataa[chan,point[0],point[1]]
        intensity_array.append(sumValues)
    
    intensitiy_values = array(spectra)
    
    sumValues = np.sum(intensitiy_values)
    avgJ = np.ndarray.mean(spectralValues)
    sigma = np.ndarray.std(spectralValues)
    threeSigma= 2.5*sigma
    
    channels=[]
    topValues=[]
    for chan in range(naxis3):
        if intensity_values[chan] > threeSigma:
            if (chan == 0) and (spectra[chan] > spectra[chan+1]):
                topValues.append([chan,spectra[chan]])
            if (chan > 0) and (chan < nchan-2) and (spectra[chan] > spectra[chan+1]) and (spectra[chan] > spectra[chan-1]):
                topValues.append([chan,spectra[chan]])
            if (chan == nchan-1) and (spectra[chan] > spectra[chan-1]):
                topValues.append([chan,spectra[chan]])
"""

freq_list = []
energy_list = []

for n_chan in range(len(data_array)):
    freq = float(hdu_header['CRVAL3']+hdu_header['CDELT3']*n_chan)
    
    mLambda = c/freq
    theta_square = hdu_header['BMAJ']*hdu_header['BMIN']
    intensity = int(np.sum(data_array[n_chan])) if np.sum(data_array[n_chan]) > 0 else 0 #Revisar
    energy_kelvin = 1.36*((mLambda*100)**2)/(theta_square*3600**2)*intensity
    
    #print("F:"+str(freq)+" - I:"+str(intensity)+" - K:"+str(energy_kelvin))
    freq_list.append(freq)
    energy_list.append(energy_kelvin)

data_list = zip(freq_list, energy_list)

#Frequency Red-Shiftting
freq_max, energy_max = max(data_list,key=operator.itemgetter(1))
redshift = (rest_freq-freq_max)/freq_max
#print("Redshift: "+str(redshift)+" Restfreq of spectral line: "+str(rest_freq))
shifted_freq_list = [freq*(1+redshift) for freq in freq_list]

#print("Original Frequency List")
#print(freq_list)
#print("\n")
#print("Doppler correction")
#print(shifted_freq_list)
#print("\n")
#sys.exit(1)

#Channeling
channeled_freq_list = [int(math.floor(freq/10**(9-channeling))) for freq in shifted_freq_list]

#Amplify intensity for spectrums with low intensity
if (energy_max < 1):
        energy_list = [energy*3 for energy in energy_list]

data_list = zip(channeled_freq_list, energy_list)

#Calculating Mean & Standard Deviation
energy_array = np.array(energy_list)
energy_mean = np.mean(energy_list)
energy_std = np.std(energy_array)

#TF Representation
words = []
for freq, energy in data_list:
        #tf = 0
        #tf = int(math.ceil(np.log2(energy))) if energy >= 1 else 0
        tf = int(math.ceil(np.log2(energy))) if energy >= energy_std*3 else 0
        words.extend([str(freq) for i in range(tf)])

mFile_out = open(spectral_file_out,'w')
print("Generated File:")
print(" ".join(words)+"\n")
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()











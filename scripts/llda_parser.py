import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FormatStrFormatter

import astropy.units as u
from astropy.io import fits

from sklearn.cluster import DBSCAN

import math
import os
import operator
import sys
import time

from bisect import bisect_left
from random import randint

font = {'family' : 'sans-serif',
        #'weight' : 'bold',
        'size'   : 16}

matplotlib.rc('font', **font)

############ FUNCTION DEFINITIONS ################
def takeClosest(myList, myNumber, thresshold = 100000):
    """
    Assumes myList is sorted. Returns closest value to myNumber.
    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    after_delta = after - myNumber
    before_delta = myNumber - before
    if after_delta < before_delta and after_delta <= thresshold:
        return after
    elif before_delta < after_delta and before_delta <= thresshold:
        return before
    elif after_delta == before_delta and after_delta <= thresshold:
        return before
    else:
        return myNumber

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

##################################################

if len(sys.argv) < 4:
        print("e.g. python llda_parser.py fits_file.fits 2 features.dat")
        sys.exit(0)

fileName = sys.argv[1]
fitsName = os.path.basename(os.path.normpath(sys.argv[1]))
channeling = int(sys.argv[2])
features = sys.argv[3]
plot = True if len(sys.argv) > 4 and sys.argv[4] == '-p' else False

start_time = time.time()

spectral_file_out = "./spectrum_document.dat"
c = 299792458

print("Parsing Fits: "+fileName)

hdulist = fits.open(fileName)
hdu_primary = hdulist[0]
hdu_header = hdu_primary.header
hdu_data = hdu_primary.data

data_array = hdu_data[0,:,:,:] if hdu_header['NAXIS'] == 4 else hdu_data 

naxis1 = hdu_header['NAXIS1'] #RA
naxis2 = hdu_header['NAXIS2'] #DEC
naxis3 = hdu_header['NAXIS3'] #Frequency
rest_freq = hdu_header['RESTFRQ'] #Rest freq

crval1 = hdu_header['CRVAL1'] #RA[0]
crval2 = hdu_header['CRVAL2'] #DEC[0]
cdelt1 = hdu_header['CDELT1'] #RA delta
cdelt2 = hdu_header['CDELT2'] #DEC delta

# ra_pos = [crval1*cdelt1*i for i in range(naxis1)]
# dec_pos = [crval2*cdelt2*i for i in range(naxis2)]

#Umbral adaptivo
sigma_thresshold = 4.0 if naxis3 >= 1000 else 3.5 if naxis3 >= 500 else 2.5 if naxis3 >= 100 else 1.5
#sigma_thresshold2 = 2.0 #For water fits
print("sigma_thresshold: " + str(sigma_thresshold))

#Determining regions of interest
list_of_args = (naxis1,naxis2,naxis3,data_array)
collapsedImage = collapseImage(list_of_args)
rms = np.sqrt(np.mean(np.square(collapsedImage)))
# print("RMS of Collapsed Cube "+str(rms))

# if (plot):
#     plt.figure(figsize=(2,10))
#     plt.subplot(121)
#     plt.imshow(collapsedImage, cmap="magma")
#     plt.colorbar()
#     plt.gca().invert_yaxis()
#     plt.xlabel("RA")
#     plt.ylabel("DEC")
#     plt.title(hdu_header['OBJECT'])

negValues = []
regionPoints = []
values = np.ndarray((naxis1,naxis2),float)
for i in range(naxis1):
    for j in range(naxis2):
        value = collapsedImage[i][j]
        if value < sigma_thresshold*rms:
            negValues.append(value)
            values[i][j] = 0
        else:
            regionPoints.append([i,j])
            values[i][j] = value

if (plot):
    plt.figure(figsize=(10,6))
    plt.subplot(121)
    plt.imshow(values, cmap="magma")
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.xlabel("RA")
    plt.ylabel("DEC")
    plt.title(hdu_header['OBJECT'])
    

db = DBSCAN(eps=int(0.1*naxis1), min_samples=4).fit(regionPoints)
result_labels = db.labels_
n_clusters_ = len(set(result_labels)) - (1 if -1 in result_labels else 0)
unique_labels = set(result_labels)
print('Estimated number of clusters: %d' % n_clusters_)

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
        values_array = []
        for point in points:
            sumValues = sumValues + data_array[chan,point[0],point[1]]
            values_array.append(data_array[chan,point[0],point[1]])
        meanValues = np.mean(values_array)
        intensity_array.append(meanValues)
        #intensity_array.append(sumValues)
    
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
#intensitiy_values = [intensitiy_value/sum(intensitiy_values) for intensitiy_value in intensitiy_values]

freq_list = []
energy_list = []

#for n_chan in range(len(data_array)):
for n_chan in range(0,len(data_array),int(len(data_array)/30)):
    freq = float(hdu_header['CRVAL3']+hdu_header['CDELT3']*n_chan)
    
    mLambda = c/freq
    theta_square = hdu_header['BMAJ']*hdu_header['BMIN']
    intensity = intensitiy_values[n_chan]
    #intensity = int(np.sum(data_array[n_chan])) if np.sum(data_array[n_chan]) > 0 else 0 #Revisar
    energy_kelvin = 1.36*((mLambda*100)**2)/(theta_square*3600**2)*(intensity*1000)

    #print("F:"+str(freq)+" - I:"+str(intensity)+" - K:"+str(energy_kelvin))
    freq_list.append(freq)
    energy_list.append(energy_kelvin)

hdulist.close()

data_list = zip(freq_list, energy_list)
data_list_aux = zip(freq_list, energy_list)

#Frequency Red-Shiftting
freq_max, energy_max = max(data_list_aux,key=operator.itemgetter(1))
#freq_max, energy_max = data_list[int(len(data_list)/2)]
redshift = (rest_freq-freq_max)/freq_max
shifted_freq_list = [freq*(1+redshift) for freq in freq_list]

#print("\nFreq/Energy Max: "+str(freq_max)+"/"+str(energy_max))
print("\nRedshift: "+str(redshift)+" Restfreq of spectral line: "+str(rest_freq))

#Channeling
#channeled_freq_list = [int(math.floor(freq/10**(9-channeling))) for freq in shifted_freq_list]
#channeled_freq_list = [int(math.ceil(freq/10**(9-channeling))) for freq in shifted_freq_list]
channeled_freq_list = [int(round(freq/10**(9-channeling))) for freq in shifted_freq_list]

#Frequency Casting
with open(features) as f:
    tokens = f.readline().split()
    vocabulary = [int(token) for token in tokens]

#Not compatible with TF vX.X.2
casted_freq_list = [takeClosest(vocabulary,freq) for freq in channeled_freq_list]


#Calculating Mean & Standard Deviation
energy_array = np.array(energy_list)
energy_mean = np.mean(energy_array)
energy_std = np.std(energy_array)
energy_thresshold = sigma_thresshold*energy_std
# print("\nMean: "+str(energy_mean))
# print("\nSigma: "+str(energy_thresshold))

#Plotting Spectrum
if plot:
    plt.subplot(122)
    plt.plot(energy_array)
    xarray = [x for x in range(0,len(energy_array))]
    k = int(len(energy_list)/4)
    plt.xticks(xarray[::k],[int(ch/100) for ch in channeled_freq_list[::k]])

    #Plotting Thresshold
    plt.plot([xarray[0],xarray[-1]], [energy_thresshold,energy_thresshold])

    #ax = plt.gca()
    #plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Intensity [T]")
    plt.tight_layout()
    plt.title(hdu_header['OBJECT'])
    plt.show()

#TF Representation
words = []
data_list = zip(casted_freq_list, channeled_freq_list, energy_list)
for freq_casted, freq_chan, energy in data_list:
        #tf = int(np.log2(math.ceil(energy))) if energy > 0 else 0 #TF v1.1.1 OK: 2.0
        #tf = int(np.log2(math.ceil(energy))) if energy > 0 else 1 #TF v1.1.2 OK: 2.0
        #tf = int(np.log2(math.ceil(energy))) if energy > energy_std*sigma_thresshold else 0 #TF v1.2.1 OK: 2.0 
        #tf = int(np.log2(math.ceil(energy))) if energy > energy_std*sigma_thresshold else 1 #TF v1.2.2 OK: 2.0

        #tf = int(np.log2(math.ceil(energy+1))) if energy > 0 else 0  #TF v2.1.1 OK: 2.0
        #tf = int(np.log2(math.ceil(energy+1))) if energy > 0 else 1  #TF v2.1.2 OK: 2.0
        
        tf = int(math.ceil(np.log2(energy+1))) if energy > energy_std*sigma_thresshold else 0  #TF v2.2.1 OK: 1.0,2.0,3.0

        #tf = int(np.log2(math.ceil(energy+1))) if energy > energy_std*sigma_thresshold else 1  #TF v2.2.2 OK: 2.0
        
        #tf = int(np.log2(math.ceil(energy))+1) if energy > 0 else 0 #TF v3.1.1 OK: 2.0
        #tf = int(np.log2(math.ceil(energy))+1) if energy > 0 else 1 #TF v3.1.2 OK: 2.0
        #tf = int(np.log2(math.ceil(energy))+1) if energy > energy_std*sigma_thresshold else 0 #TF v3.2.1 OK: 2.0
        #tf = int(np.log2(math.ceil(energy))+1) if energy > energy_std*sigma_thresshold else 1 #TF v3.2.2 OK: 2.0
            
        words.extend([str(freq_casted) for i in range(tf)]) #Channeled + Casted Version
        #words.extend([str(freq_chan) for i in range(tf)]) #Only Channeled Version
words.sort()

#words.extend([str('24493') for i in range(30)]) #CarbonMonosulfide:HotCores_2(12):20/3008 | AlmaBand6_2(68): 5/90
#words.extend([str('18180') for i in range(300)]) #Protonate2-proynenitrile:HotCores2(57):35/808
#words.extend([str('22975876') for i in range(1)]) #Methanol:HotCoresFull(34):7/17636
#words.extend([str('32122568') for i in range(1)]) #Water:HotCoresFull(20):x/x

#print("Generated File:")
#print(" ".join(words)+"\n")

mFile_out = open(spectral_file_out,'w')
mFile_out.write(" ".join(words)+"\n")
mFile_out.close()

end_time = time.time()
print("Parsing time: "+str(end_time-start_time)+" seconds")
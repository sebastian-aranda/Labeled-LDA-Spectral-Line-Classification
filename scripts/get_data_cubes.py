import sys
import os

import astropy.units as u
import numpy as np
from astropy.io import fits

test_data = sys.argv[1]
fits_folder = 'fits_delivery_20180309/'

with open(test_data) as f:
	mFile = open('tmp.csv','w')
	for line in f:
		tokens = line.split(';')
		fits_name = tokens[0].split('/')[-1]
		fits_path = fits_folder+fits_name
		print("Open fits: "+fits_path)
		hdulist = fits.open(fits_path)
		hdu_primary = hdulist[0]
		hdu_header = hdu_primary.header
		hdu_data = hdu_primary.data

		if hdu_header['NAXIS'] > 2:
			new_line = '../../'+fits_path+';'+tokens[1]
			mFile.write(new_line)
		else:
			print(fits_name+' is not a datacube')

os.remove(test_data)
os.rename('tmp.csv',test_data)

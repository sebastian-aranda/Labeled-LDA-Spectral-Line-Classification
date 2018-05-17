#from __future__ import print_function
import sys
import os

species_no = sys.argv[1]
object = sys.argv[2]

files = [file for file in os.listdir('.') if file.split('.')[-1] == 'output']
files.sort()
#print(len(files))
#print(files)
for file in files:
	if file.split('.')[0] != object:
		continue
	print(file)
	with open(file) as f:
		for i,line in enumerate(f):
			tokens = line.split(';')
			species_no_result = tokens[1].split()[0]
			if species_no_result == species_no:
				print(line.rstrip('\n'))	

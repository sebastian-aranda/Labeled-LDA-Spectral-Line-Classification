#from __future__ import print_function
import sys
import os

files = [file for file in os.listdir('.') if file.split('.')[-1] == 'output']
files.sort()
#print(len(files))
#print(files)
for file in files:
	print(file)
	with open(file) as f:
		for i,line in enumerate(f):			
			if i >= 3:
				break
			print(line.rstrip('\n'))	

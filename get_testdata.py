import sys
import os

if (len(sys.argv) != 2):
	print("e.g. python get_testdata.py ./path/to/folder/ ./llda_train_input/model_labelmap.sub")
	sys.exit(0)


species = dict()
with open(sys.argv[2]) as f:
	for line in f:
		tokens = line.split()
		species[tokens[0]] = " ".join(tokens[1:])

files = [file for file in os.listdir(sys.argv[1]) if file[0] != '.' and file.split('.')[-1] == 'fits']
print(files)
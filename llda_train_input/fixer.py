import sys
import os

if (len(sys.argv) != 4):
	print("e.g. python fixer.py hot_cores_tr.dat hot_cores_tr_labelmap.sub 21")
	sys.exit(1)

fileName = sys.argv[1]
labelmap_fileName = sys.argv[2]
speciesNo = int(sys.argv[3])

mFile = open("temp.dat", "w")
print("Opening: "+fileName)
with open(fileName) as f:
	counter = 0
	for line in f:
		tokens = line.split()
		if speciesNo == int(tokens[0][1:-1]):
			continue
		mFile.write("["+str(counter)+"] ")
		mFile.write(" ".join(tokens[1:]))
		mFile.write("\n")
		counter += 1
mFile.close()
os.remove(fileName)
os.rename("temp.dat", "./llda_train_input/"+os.path.basename(os.path.normpath(fileName+"x")))

mFile = open("temp.sub", "w")
with open(labelmap_fileName) as f:
	counter = 0
	for line in f:
		tokens = line.split()
		if speciesNo == int(tokens[0]):
			continue
		mFile.write(str(counter))
		mFile.write(" ")
		mFile.write(" ".join(tokens[1:]))
		mFile.write("\n")
		counter += 1
mFile.close()
os.remove(labelmap_fileName)
os.rename("temp.sub", "./llda_train_input/"+os.path.basename(os.path.normpath(labelmap_fileName)))

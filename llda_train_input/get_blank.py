import sys

fileName = sys.argv[1]

with open(fileName) as f:
	for line in f:
		if len(line.split()) < 2:
			print(line)

import sys

with open(sys.argv[1]) as f:
	for i,line in enumerate(f):
		if i == int(sys.argv[2]):
			print(line)
		

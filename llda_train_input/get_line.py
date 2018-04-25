import sys

if (len(sys.argv) != 3):
	print("e.g. python get_line.py hot_cores_full.dat 10")
	sys.exit(1)

with open(sys.argv[1]) as f:
	for i,line in enumerate(f):
		if i == int(sys.argv[2]):
			print(line)
		

import sys

if (len(sys.argv) != 3):
	print("e.g. python get_freq_line.py hot_cores_full.dat 24493555")
	sys.exit(1)

with open(sys.argv[1]) as f:
	for i,line in enumerate(f):
		if any(sys.argv[2] in s for s in line.split()[1:]):
			print(line.split()[0])
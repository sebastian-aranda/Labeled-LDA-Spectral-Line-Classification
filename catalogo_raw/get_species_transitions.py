import sys

if (len(sys.argv) != 3):
	print("e.g. python get_species_transitions.py hot_cores_full.raw \"carbon monosulfide\"")
	sys.exit(1)

with open(sys.argv[1]) as f:
	for i,line in enumerate(f):
		if sys.argv[2] in " ".join(line.split()[:-2]).lower():
			print(line.replace('\n',''))
		

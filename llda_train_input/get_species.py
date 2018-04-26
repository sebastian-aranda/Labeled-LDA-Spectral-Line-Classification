import sys

species = []
with open(sys.argv[2]) as f:
	for line in f:
		tokens = line.split()
		species.append((tokens[0]," ".join(tokens[1:])))

with open(sys.argv[1]) as f:
	for i,line in enumerate(f):
		tokens = line.split()
		
		species_no = tokens[0][1:-1] 
		species_name = ''
		for x, y in species:
			if x == species_no:
				species_name = y
		
		if sys.argv[3] in tokens:
			print(tokens[0]+" "+species_name)
		

import sys

if (len(sys.argv) != 2):
	print("e.g. python get_vocabulary.py hot_cores_full.dat")
	sys.exit(0)

words = set()
with open(sys.argv[1]) as f:
	for line in f:
		tokens = line.split()[1:]
		words.update(tokens)

words = sorted(list(words), key=int)
print(" ".join(words))

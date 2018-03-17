import sys

count = 0

filename = sys.argv[1]
word_list = list()
with open(filename) as f:
	for line in f:
		word_list.extend(line.split()[1:])

print(len(word_list))
print(len(set(word_list)))	

import sys
import operator

if len(sys.argv) != 2:
        print("e.g. python spectral_line.py casa_spectrums/casa_spectrum.dat")


aux_list = []

filename = sys.argv[1]
with open(filename) as f:
        for line in f:
                if not line[0].isdigit():
                	continue

                tokens = line.split()
                freq = tokens[0].split('e')
                freq = float(freq[0])*10**int(freq[1])
                energy = tokens[1].split('e')
                energy = float(energy[0])*10**int(energy[1])

                aux_list.append((freq,energy))

freq_max, energy_max = max(aux_list,key=operator.itemgetter(1))
print("Energy Peak: {} Kelvin".format(energy_max))
print("Frequency: {} ".format(freq_max))

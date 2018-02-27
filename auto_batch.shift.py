import sys
import shutil
import os
import subprocess

if (len(sys.argv) != 2):
	print("e.g. python auto_batch.shift.py test_data/data.csv")
	sys.exit(1)

#mData = os.path.basename(os.path.normpath(sys.argv[1]))
mData = sys.argv[1]

models_array = [(0,'llda_models/model_hot_cores_tr_500it/','llda_train_input/hot_cores_tr_labelmap.sub'),(2,'llda_models/model_hot_cores_2_500it/','llda_train_input/hot_cores_2_labelmap.sub'),(5,'llda_models/model_hot_cores_full_500it/','llda_train_input/hot_cores_full_labelmap.sub'),(5,'llda_models/model_hot_cores_full_expanded_500it/','llda_train_input/hot_cores_full_labelmap.sub')]
for channeling, model, labelmap in models_array:
	with open(mData) as f:
		for line in f:
			tokens = line.strip().split(';')
			if (len(tokens) < 3):
				continue
			#print(tokens)
			os.system("python auto.shift.py "+model+" "+str(channeling)+" "+tokens[2]+" casa_spectrums/"+tokens[1]+" "+labelmap)
			
			data_name = tokens[1].split('.')[0]
			model_name = model.split('/')[1]
			os.system("mv output.dat "+data_name+"."+model_name+".output")

models_array = [(0,'llda_models/model_alma_band_6_tr_500it/','llda_train_input/alma_band_6_tr_labelmap.sub'),(2,'llda_models/model_alma_band_6_2_500it/','llda_train_input/alma_band_6_2_labelmap.sub'),(5,'llda_models/model_alma_band_6_full_500it/','llda_train_input/alma_band_6_full_labelmap.sub'),(5,'llda_models/model_alma_band_6_full_expanded_500it/','llda_train_input/alma_band_6_full_labelmap.sub')]
for channeling, model, labelmap in models_array:
        with open(mData) as f:
                for line in f:
                        tokens = line.strip().split(';')
                        if (len(tokens) < 3):
                                continue
                        #print(tokens)
                        os.system("python auto.shift.fix1.py "+model+" "+str(channeling)+" "+tokens[2]+" casa_spectrums/"+tokens[1]+" "+labelmap)

                        data_name = tokens[1].split('.')[0]
                        model_name = model.split('/')[1]
                        os.system("mv output.dat "+data_name+"."+model_name+".output")

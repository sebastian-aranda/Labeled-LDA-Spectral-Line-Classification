import sys
import gzip
import shutil
import os

if (len(sys.argv) != 7):
	print("You must give 6 parameters: model_path, features_path, labels_path, channeling, fits_path, species_no")
	print("e.g. python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../FITS/DMTau.CS_5-4.image.fits 12")
	sys.exit(1)

model = os.path.basename(os.path.normpath(sys.argv[1]))
features = os.path.basename(os.path.normpath(sys.argv[2]))
labels = os.path.basename(os.path.normpath(sys.argv[3]))
channeling = sys.argv[4]
fits_path = sys.argv[5]
species_no = sys.argv[6]

filename = fits_path
temp_filename = "spectrum_document.dat"

os.chdir("./scripts/")

os.system("python llda_parser_v2.py "+filename+" "+channeling+" "+"../llda_train_input/"+features)

print("Used model")
print(model)
with open(temp_filename, 'rb') as f_in, gzip.open(temp_filename+".gz", 'wb') as f_out: 
    shutil.copyfileobj(f_in, f_out)
os.rename(temp_filename+".gz","../llda_models/"+model+"/"+temp_filename+".gz") #Must copy to "./llda_models/models/" beacause of some rules that read files in JGibbLabeledLDA<

#Model Inference
#Labeled LDA in Java Copyright (C) 2008-2013 Myle Ott (Labeled LDA), Xuan-Hieu Phan and Cam-Tu Nguyen (JGibbLDA)
os.chdir("../JGibbLabeledLDA-master/")
os.system("java -mx8192M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -inf -dir ../llda_models/"+model+"/ -model "+model+" -niters 30 -twords 10 -dfile "+temp_filename+".gz")

os.chdir("../llda_models/"+model+"/")
os.remove(temp_filename+".gz")
os.rename(temp_filename+"."+model+".theta.gz", "../../scripts/"+temp_filename+"."+model+".theta.gz")
os.system("rm "+temp_filename+"."+model+".*")

#Parsing llda output
os.chdir("../../scripts/")
shutil.copyfile("../llda_train_input/"+labels,labels)
os.system("python llda_output_theta_parser.py "+temp_filename+"."+model+".theta.gz "+labels+" > ../output.dat")
os.remove(labels)
os.remove(temp_filename+"."+model+".theta.gz")

os.chdir("../")
#Evaluate Prediction
match = False
with open('output.dat') as f:
	last_pos = f.tell()
	last_line = f.readlines()[-1]
	f.seek(last_pos)
	for i,line in enumerate(f):
		if i>=5:
			break
		no = line.split()[0].split(';')[1]
		prob = line.split()[-1].split(';')[1]
		last_prob = last_line.split()[-1].split(';')[1]
		
		if no == species_no and prob != last_prob:
			print("Prob: "+str(prob)+" Last Prob: "+str(last_prob))
			response = "¡MATCH! Model["+model+"] FITS["+filename+"]: "+prob+"\n"
			with open("matches.out","a") as fileMatch:
				fileMatch.write(response)
			print(response)
			match = True
if (not match):
	print("Transition not found")


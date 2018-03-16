import sys
import gzip
import shutil
import os
#import subprocess
if (len(sys.argv) != 6):
	print("You must give 5 parameters: model_path, labels_path, channeling, fits_path")
	print("e.g. python auto-full.py llda_models/hot_cores_2_1000/ llda_train_input/hot_cores_2_labelmap.sub 2 mFits.fits")
	sys.exit(1)

model = os.path.basename(os.path.normpath(sys.argv[1]))
labels = os.path.basename(os.path.normpath(sys.argv[2]))
channeling = sys.argv[3]
fits_path = sys.argv[4]
filename = os.path.basename(os.path.normpath(sys.argv[4]))

#Parsing output from Spectral Profile Tool of CASA Viewer
temp_filename = "spectrum_document" #Same as spectral_file_out variable in llda_input_parser_CASA
#shutil.copyfile("./casa_spectrums/"+filename,"./scripts/"+filename)
shutil.copyfile(fits_path, ./scripts/"+filename)
os.chdir("./scripts/")
os.system("python llda_parser.py "+filename+" "+channeling+" "+rest_freq)
print("Used model")
print(model)
with open(temp_filename+".dat", 'rb') as f_in, gzip.open(temp_filename+".dat.gz", 'wb') as f_out: #Must copy to "./llda_models/models/" beacause of some rules that read files in JGibbLabeledLDA
    shutil.copyfileobj(f_in, f_out)
os.remove(temp_filename+".dat")
os.remove(filename)
os.rename(temp_filename+".dat.gz","../llda_models/"+model+"/"+temp_filename+".dat.gz")

#Model Inference
#Labeled LDA in Java Copyright (C) 2008-2013 Myle Ott (Labeled LDA), Xuan-Hieu Phan and Cam-Tu Nguyen (JGibbLDA)
os.chdir("../JGibbLabeledLDA-master/")
os.system("java -mx4096M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -inf -dir ../llda_models/"+model+"/ -model "+model+" -niters 500 -twords 10 -dfile "+temp_filename+".dat.gz")

os.chdir("../llda_models/"+model+"/")
os.remove(temp_filename+".dat.gz")
os.rename(temp_filename+".dat."+model+".theta.gz", "../../scripts/"+temp_filename+".dat."+model+".theta.gz")
os.system("rm "+temp_filename+".dat."+model+".*")

#Parsing llda output
os.chdir("../../scripts/")
shutil.copyfile("../llda_train_input/"+labels,labels)
os.system("python llda_output_theta_parser.py "+temp_filename+".dat."+model+".theta.gz "+labels+" > ../output.dat")
os.remove(labels)
os.remove(temp_filename+".dat."+model+".theta.gz")

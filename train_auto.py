import sys
import gzip
import shutil
import os
#import subprocess

if (len(sys.argv) != 7):
	print("You must give 6 parameters: train_data(gziped), alpha, beta, number_of_topics, number_of_iterations, model_name")
	print("e.g. python train_auto.py llda_train_input/hot_cores_tr.dat.gz 0.7 0.008 85 500 model_hot_cores_tr_500it")
	sys.exit(0)

data_train = os.path.basename(os.path.normpath(sys.argv[1]))
alpha = sys.argv[2]
beta = sys.argv[3]
number_of_topics = sys.argv[4]
number_of_iterations = sys.argv[5]
model_name = sys.argv[6]

os.chdir("./JGibbLabeledLDA-master/")
shutil.copyfile("../llda_train_input/"+data_train,data_train)
os.system("java -mx8192M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha "+alpha+" -beta "+beta+" -ntopics "+number_of_topics+" -niters "+number_of_iterations+" -twords 10 -model "+model_name+" -dir . -dfile "+data_train)
os.mkdir("../llda_models/"+model_name)
os.system("mv "+model_name+".* ../llda_models/"+model_name+"/")
os.remove(data_train)

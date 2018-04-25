import sys
import shutil
import os
import subprocess

if (len(sys.argv) != 1):
        print("e.g. python inference_batch.test.py")
        sys.exit(0)

models_array = [(2,'llda_models/model_test_2_500it/','llda_train_input/test_2.dat','llda_train_input/test_2_labelmap.sub')]

os.system("mkdir results."+model_name)
for channeling, model_path, corpus_path, labelmap_path in models_array:
        os.system("python inference.test.py "+model_path+" "+corpus_path+" "+labelmap_path+" "+str(channeling))
        fits_name = "ejemplo_controlado"

        model = model_path.split('/')[1]
        out_name = fits_name+"."+model+".output"
        os.system("mv output.dat results."+model_name+"/"+out_name)
        os.chdir("results."+model_name+"/")
        os.system("python ../scripts/consolidate_result.py "+model_name+" > res."+model_name+".out")



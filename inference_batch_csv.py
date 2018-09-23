import sys
import shutil
import os
import subprocess

INFERENCE_TRIES = 10
if (len(sys.argv) != 3):
        print("e.g. python inference_batch_csv.py hot_cores test_data/data_test_schilke.hot_cores.csv")
        sys.exit(0)

#mData = os.path.basename(os.path.normpath(sys.argv[1]))
model_name = sys.argv[1]
mData = sys.argv[2]

if model_name == 'hot_cores':
        models_array = [
        #(0,'llda_models/model_hot_cores_tr_500it/','llda_train_input/hot_cores_tr_features.dat','llda_train_input/hot_cores_tr_labelmap.sub')
        #,(2,'llda_models/model_hot_cores_2_500it/','llda_train_input/hot_cores_2_features.dat','llda_train_input/hot_cores_2_labelmap.sub')
        (5,'llda_models/model_hot_cores_full_500it/','llda_train_input/hot_cores_full_features.dat','llda_train_input/hot_cores_full_labelmap.sub')
        
        #,(5,'llda_models/model_hot_cores_full_expanded_00050_x3_500it','llda_train_input/hot_cores_full_expanded_00050_x3_features.dat','llda_train_input/hot_cores_full_labelmap.sub')
        #,(5,'llda_models/model_hot_cores_full_expanded_00100_x3_500it','llda_train_input/hot_cores_full_expanded_00100_x3_features.dat','llda_train_input/hot_cores_full_labelmap.sub')
        #,(5,'llda_models/model_hot_cores_full_expanded_01000_x3_500it','llda_train_input/hot_cores_full_expanded_01000_x3_features.dat','llda_train_input/hot_cores_full_labelmap.sub')
        ]
else:
        print("Model not found")
        sys.exit(0)



for run in range(1,INFERENCE_TRIES+1):
        print("#################INFERENCE TRY: "+str(run)+"/"+str(INFERENCE_TRIES))
        run = str(run) if run > 9 else '0'+str(run) 
        os.system("mkdir results_csv."+model_name+".t"+run)
        for channeling, model_path, features_path, labelmap_path in models_array:
                with open(mData) as f:
                        for test_example in f:
                                if test_example[0] == "#" or test_example[0] == "\n":
                                        continue
                                fits_path = test_example.split(';')[0]
                                spw = test_example.split(';')[1]
                                species_no = test_example.split(';')[2]
                                #print(fits_path)
                                os.system("python inference_csv.py "+model_path+" "+features_path+" "+labelmap_path+" "+str(channeling)+" "+fits_path+" "+spw+" "+species_no)
                                fits_name = fits_path.split('/')[-1]
                                fits_name = ".".join(fits_name.split('.')[:-1])

                                model = model_path.split('/')[1]
                                out_name = fits_name+"."+spw.replace(",","-")+"."+model+".output"
                                os.system("mv output_csv.dat results_csv."+model_name+".t"+run+"/"+out_name)
        os.system("mv matches_csv.out results_csv."+model_name+".t"+run+"/")
#os.chdir("results."+model_name+"/")
#os.system("python ../scripts/consolidate_result.py "+model_name+" > res."+model_name+".out")

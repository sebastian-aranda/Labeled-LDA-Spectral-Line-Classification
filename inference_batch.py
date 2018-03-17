import sys
import shutil
import os
import subprocess

if (len(sys.argv) != 3):
        print("e.g. python inference_batch.py hot_cores test_data/data.csv")
        sys.exit(0)

#mData = os.path.basename(os.path.normpath(sys.argv[1]))
model_name = sys.argv[1]
mData = sys.argv[2]

if model_name == 'hot_cores':
        models_array = [(0,'llda_models/model_hot_cores_tr_500it/','llda_train_input/hot_cores_tr_labelmap.sub'),(2,'llda_models/model_hot_cores_2_500it/','llda_train_input/hot_cores_2_labelmap.sub'),(5,'llda_models/model_hot_cores_full_500it/','llda_train_input/hot_cores_full_labelmap.sub'), (5,'llda_models/model_hot_cores_full_expanded_500it','llda_train_input/hot_cores_full_labelmap.sub')]
elif model_name == 'alma_band_6':
        models_array = [(0,'llda_models/model_alma_band_6_tr_500it/','llda_train_input/alma_band_6_tr_labelmap.sub'),(2,'llda_models/model_alma_band_6_2_500it/','llda_train_input/alma_band_6_2_labelmap.sub'),(5,'llda_models/model_alma_band_6_full_500it/','llda_train_input/alma_band_6_full_labelmap.sub'), (5,'llda_models/model_alma_band_6_full_expanded_500it','llda_train_input/alma_band_6_full_labelmap.sub')]
elif model_name == 'agb_ppn_pn':
        models_array = [(0,'llda_models/model_agb_ppn_pn_tr_500it/','llda_train_input/agb_ppn_pn_tr_labelmap.sub'),(2,'llda_models/model_agb_ppn_pn_2_500it/','llda_train_input/agb_ppn_pn_2_labelmap.sub'),(5,'llda_models/model_agb_ppn_pn_full_500it/','llda_train_input/agb_ppn_pn_full_labelmap.sub'), (5,'llda_models/model_agb_ppn_pn_full_expanded_500it','llda_train_input/agb_ppn_pn_full_labelmap.sub')]        
elif model_name == 'planetary':
        models_array = [(0,'llda_models/model_planetary_tr_500it/','llda_train_input/planetary_tr_labelmap.sub'),(2,'llda_models/model_planetary_2_500it/','llda_train_input/planetary_2_labelmap.sub'),(5,'llda_models/model_planetary_full_500it/','llda_train_input/planetary_full_labelmap.sub'), (5,'llda_models/model_planetary_full_expanded_3-0.001_500it','llda_train_input/planetary_full_labelmap.sub')]
elif model_name == 'dark_clouds':
        models_array = [(0,'llda_models/model_dark_clouds_tr_500it/','llda_train_input/dark_clouds_tr_labelmap.sub'),(2,'llda_models/model_dark_clouds_2_500it/','llda_train_input/dark_clouds_2_labelmap.sub'),(5,'llda_models/model_dark_clouds_full_500it/','llda_train_input/dark_clouds_full_labelmap.sub'),(5,'llda_models/model_dark_clouds_full_expanded_3-0.001_500it','llda_train_input/dark_clouds_full_labelmap.sub')]
elif model_name == 'diffuse_clouds':
        models_array = [(0,'llda_models/model_diffuse_clouds_tr_500it/','llda_train_input/diffuse_clouds_tr_labelmap.sub'),(2,'llda_models/model_diffuse_clouds_2_500it/','llda_train_input/diffuse_clouds_2_labelmap.sub'),(5,'llda_models/model_diffuse_clouds_full_500it/','llda_train_input/diffuse_clouds_full_labelmap.sub')]
elif model_name == 'comets':
        models_array = [(0,'llda_models/model_comets_tr_500it/','llda_train_input/comets_tr_labelmap.sub'),(2,'llda_models/model_comets_2_500it/','llda_train_input/comets_2_labelmap.sub'),(5,'llda_models/model_comets_full_500it/','llda_train_input/comets_full_labelmap.sub')]
elif model_name == 'extragalactic':
        models_array = [(0,'llda_models/model_extragalactic_tr_500it/','llda_train_input/extragalactic_tr_labelmap.sub'),(2,'llda_models/model_extragalactic_2_500it/','llda_train_input/extragalactic_2_labelmap.sub'),(5,'llda_models/model_extragalactic_full_500it/','llda_train_input/extragalactic_full_labelmap.sub')]
elif model_name == 'dark_clouds':
        models_array = [(5,'llda_models/model_dark_clouds_full_expanded_3-0.001_500it/','llda_train_input/dark_clouds_full_labelmap.sub'),(5,'llda_models/model_diffuse_clouds_full_expanded_3-0.001_500it/','llda_train_input/diffuse_clouds_full_labelmap.sub'),(5,'llda_models/model_comets_full_expanded_3-0.001_500it/','llda_train_input/comets_full_labelmap.sub'),(5,'llda_models/model_extragalactic_full_expanded_3-0.001_500it/','llda_train_input/extragalactic_full_labelmap.sub'),]
else:
        print("Model not found")
        sys.exit(0)


os.system("mkdir results."+model_name)
for channeling, model_path, labelmap_path in models_array:
        with open(mData) as f:
                for fits_path in f:
                        os.system("python inference.py "+model_path+" "+labelmap_path+" "+str(channeling)+" "+fits_path)
                        fits_name = fits_path.split('/')[-1]
                        fits_name = ".".join(fits_name.split('.')[:-1])

                        model = model_path.split('/')[1]
                        out_name = fits_name+"."+model+".output"
                        os.system("mv output.dat results."+model_name+"/"+out_name)



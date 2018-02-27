#Inference on HD163296: CO_2_1 [230,512-230,573GHz]
python auto.py llda_models/model_hot_cores_tr_1000it/ 0 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat HD163296_hot_cores_tr.output

python auto.py llda_models/hot_cores_2_1000/ 2 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/hot_cores_2_labelmap.sub
mv output.dat HD163296_hot_cores_2.output

python auto.py llda_models/hot_cores_full_model/ 5 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/hot_cores_full_labelmap.sub
mv output.dat HD163296_hot_cores_full.output

python auto.py llda_models/model_alma_band_6_tr_1000it/ 0 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat HD163296_alma_band_6_tr.output

python auto.py llda_models/model_alma_band_6_2_1000it/ 2 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat HD163296_alma_band_6_2.output

python auto.py llda_models/model_alma_band_6_full_1000it/ 5 casa_spectrums/CO_2_1_HD163296.dat llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat HD163296_alma_band_6_full.output

#Inference on Orion: HNC [271,945-272,003GHz]
python auto.py llda_models/model_hot_cores_tr_1000it/ 0 casa_spectrums/HNC.dat llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat ORION_hot_cores_tr.output

python auto.py llda_models/hot_cores_2_1000/ 2 casa_spectrums/HNC.dat llda_train_input/hot_cores_2_labelmap.sub
mv output.dat ORION_hot_cores_2.output

python auto.py llda_models/hot_cores_full_model/ 5 casa_spectrums/HNC.dat llda_train_input/hot_cores_full_labelmap.sub
mv output.dat ORION_hot_cores_full.output

python auto.py llda_models/model_alma_band_6_tr_1000it/ 0 casa_spectrums/HNC.dat llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat ORION_alma_band_6_tr.output

python auto.py llda_models/model_alma_band_6_2_1000it/ 2 casa_spectrums/HNC.dat llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat ORION_alma_band_6_2.output

python auto.py llda_models/model_alma_band_6_full_1000it/ 5 casa_spectrums/HNC.dat llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat ORION_alma_band_6_full.output

#Inference on DMTAU: CS [244,936-244,926GHz]
python auto.py llda_models/model_hot_cores_tr_1000it/ 0 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat DMTAU_hot_cores_tr.output

python auto.py llda_models/hot_cores_2_1000/ 2 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/hot_cores_2_labelmap.sub
mv output.dat DMTAU_hot_cores_2.output

python auto.py llda_models/hot_cores_full_model/ 5 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/hot_cores_full_labelmap.sub
mv output.dat DMTAU_hot_cores_full.output

python auto.py llda_models/model_alma_band_6_tr_1000it/ 0 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat DMTAU_alma_band_6_tr.output

python auto.py llda_models/model_alma_band_6_2_1000it/ 2 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat DMTAU_alma_band_6_2.output

python auto.py llda_models/model_alma_band_6_full_1000it/ 5 casa_spectrums/DMTAU.CS.5-4.dat llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat DMTAU_alma_band_6_full.output

#Inference on IRS43: HCO_3_2 [267,571-267,535GHz]
python auto.py llda_models/model_hot_cores_tr_1000it/ 0 casa_spectrums/HCO32.dat llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat IRS43_hot_cores_tr.output

python auto.py llda_models/hot_cores_2_1000/ 2 casa_spectrums/HCO32.dat llda_train_input/hot_cores_2_labelmap.sub
mv output.dat IRS43_hot_cores_2.output

python auto.py llda_models/hot_cores_full_model/ 5 casa_spectrums/HCO32.dat llda_train_input/hot_cores_full_labelmap.sub
mv output.dat IRS43_hot_cores_full.output

python auto.py llda_models/model_alma_band_6_tr_1000it/ 0 casa_spectrums/HCO32.dat llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat IRS43_alma_band_6_tr.output

python auto.py llda_models/model_alma_band_6_2_1000it/ 2 casa_spectrums/HCO32.dat llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat IRS43_alma_band_6_2.output

python auto.py llda_models/model_alma_band_6_full_1000it/ 5 casa_spectrums/HCO32.dat llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat IRS43_alma_band_6_full.output


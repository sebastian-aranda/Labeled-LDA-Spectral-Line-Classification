##################### WATER #####################
#gzip -k llda_train_input/water_tr.dat
#python train_auto.py llda_train_input/water_tr.dat.gz 50 0.1 1 500 model_water_tr_500it
#rm llda_train_input/water_tr.dat.gz

#gzip -k llda_train_input/water_2.dat
#python train_auto.py llda_train_input/water_2.dat.gz 50 0.1 1 500 model_water_2_500it
#rm llda_train_input/water_2.dat.gz

#gzip -k llda_train_input/water_full.dat
#python train_auto.py llda_train_input/water_full.dat.gz 50 0.1 1 500 model_water_full_500it
#rm llda_train_input/water_full.dat.gz

gzip -k llda_train_input/water_full_expanded_00200.dat
python train_auto.py llda_train_input/water_full_expanded_00200.dat.gz 50 0.1 1 500 model_water_full_expanded_00200_500it
rm llda_train_input/water_full_expanded_00200.dat.gz
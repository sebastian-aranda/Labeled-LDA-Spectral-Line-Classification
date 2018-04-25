##################### ALMA BAND 6 #####################
:'
gzip -k llda_train_input/alma_band_6_tr.dat
python train_auto.py llda_train_input/alma_band_6_tr.dat.gz 0.4 1.8 117 500 model_alma_band_6_tr_500it
rm llda_train_input/alma_band_6_tr.dat.gz

gzip -k llda_train_input/alma_band_6_2.dat
python train_auto.py llda_train_input/alma_band_6_2.dat.gz 0.4 0.02 117 500 model_alma_band_6_2_500it
rm llda_train_input/alma_band_6_2.dat.gz

gzip -k llda_train_input/alma_band_6_full.dat
python train_auto.py llda_train_input/alma_band_6_full.dat.gz 0.4 0.002 117 500 model_alma_band_6_full_500it
rm llda_train_input/alma_band_6_full.dat.gz

gzip -k llda_train_input/alma_band_6_full_expanded_00002.dat
python train_auto.py llda_train_input/alma_band_6_full_expanded_00002.dat.gz 0.4 0.1 117 500 model_alma_band_6_full_expanded_00002_500it
rm llda_train_input/alma_band_6_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/alma_band_6_full_expanded_00010.dat
python train_auto.py llda_train_input/alma_band_6_full_expanded_00010.dat.gz 0.4 0.1 117 500 model_alma_band_6_full_expanded_00010_500it
rm llda_train_input/alma_band_6_full_expanded_00010.dat.gz
##################### HOT CORES #####################
:'
gzip -k llda_train_input/hot_cores_tr.dat
python train_auto.py llda_train_input/hot_cores_tr.dat.gz 0.6 0.009 85 500 model_hot_cores_tr_500it
rm llda_train_input/hot_cores_tr.dat.gz

gzip -k llda_train_input/hot_cores_2.dat
python train_auto.py llda_train_input/hot_cores_2.dat.gz 0.6 0.0005 85 500 model_hot_cores_2_500it
rm llda_train_input/hot_cores_2.dat.gz

gzip -k llda_train_input/hot_cores_full.dat
python train_auto.py llda_train_input/hot_cores_full.dat.gz 0.6 0.0001 85 500 model_hot_cores_full_500it
rm llda_train_input/hot_cores_full.dat.gz

gzip -k llda_train_input/hot_cores_full_expanded_00002.dat
python train_auto.py llda_train_input/hot_cores_full_expanded_00002.dat.gz 0.6 0.1 85 500 model_hot_cores_full_expanded_00002_500it
rm llda_train_input/hot_cores_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/hot_cores_full_expanded_00010.dat
python train_auto.py llda_train_input/hot_cores_full_expanded_00010.dat.gz 0.6 0.1 85 500 model_hot_cores_full_expanded_00010_500it
rm llda_train_input/hot_cores_full_expanded_00010.dat.gz
##################### AGB_PPN_PN #####################
:'
gzip -k llda_train_input/agb_ppn_pn_tr.dat
python train_auto.py llda_train_input/agb_ppn_pn_tr.dat.gz 0.7 0.007 71 500 model_agb_ppn_pn_tr_500it
rm llda_train_input/agb_ppn_pn_tr.dat.gz

gzip -k llda_train_input/agb_ppn_pn_2.dat
python train_auto.py llda_train_input/agb_ppn_pn_2.dat.gz 0.7 0.0008 71 500 model_agb_ppn_pn_2_500it
rm llda_train_input/agb_ppn_pn_2.dat.gz

gzip -k llda_train_input/agb_ppn_pn_full.dat
python train_auto.py llda_train_input/agb_ppn_pn_full.dat.gz 0.7 0.0004 71 500 model_agb_ppn_pn_full_500it
rm llda_train_input/agb_ppn_pn_full.dat.gz

gzip -k llda_train_input/agb_ppn_pn_full_expanded_00002.dat
python train_auto.py llda_train_input/agb_ppn_pn_full_expanded_00002.dat.gz 0.7 0.1 71 500 model_agb_ppn_pn_full_expanded_00002_500it
rm llda_train_input/agb_ppn_pn_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/agb_ppn_pn_full_expanded_00010.dat
python train_auto.py llda_train_input/agb_ppn_pn_full_expanded_00010.dat.gz 0.7 0.1 71 500 model_agb_ppn_pn_full_expanded_00010_500it
rm llda_train_input/agb_ppn_pn_full_expanded_00010.dat.gz
##################### PLANETARY #####################
:'
gzip -k llda_train_input/planetary_tr.dat
python train_auto.py llda_train_input/planetary_tr.dat.gz 2.5 0.003 20 500 model_planetary_tr_500it
rm llda_train_input/planetary_tr.dat.gz

gzip -k llda_train_input/planetary_2.dat
python train_auto.py llda_train_input/planetary_2.dat.gz 2.5 0.0009 20 500 model_planetary_2_500it
rm llda_train_input/planetary_2.dat.gz

gzip -k llda_train_input/planetary_full.dat
python train_auto.py llda_train_input/planetary_full.dat.gz 2.5 0.0008 20 500 model_planetary_full_500it
rm llda_train_input/planetary_full.dat.gz

gzip -k llda_train_input/planetary_full_expanded_00002.dat
python train_auto.py llda_train_input/planetary_full_expanded_00002.dat.gz 2.5 0.1 20 500 model_planetary_full_expanded_00002_500it
rm llda_train_input/planetary_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/planetary_full_expanded_00010.dat
python train_auto.py llda_train_input/planetary_full_expanded_00010.dat.gz 2.5 0.1 20 500 model_planetary_full_expanded_00010_500it
rm llda_train_input/planetary_full_expanded_00010.dat.gz
##################### DARK CLOUDS #####################
:'
gzip -k llda_train_input/dark_clouds_tr.dat
python train_auto.py llda_train_input/dark_clouds_tr.dat.gz 0.9 0.007 58 500 model_dark_clouds_tr_500it
rm llda_train_input/dark_clouds_tr.dat.gz

gzip -k llda_train_input/dark_clouds_2.dat
python train_auto.py llda_train_input/dark_clouds_2.dat.gz 0.9 0.0005 58 500 model_dark_clouds_2_500it
rm llda_train_input/dark_clouds_2.dat.gz

gzip -k llda_train_input/dark_clouds_full.dat
python train_auto.py llda_train_input/dark_clouds_full.dat.gz 0.9 0.0003 58 500 model_dark_clouds_full_500it
rm llda_train_input/dark_clouds_full.dat.gz

gzip -k llda_train_input/dark_clouds_full_expanded_00002.dat
python train_auto.py llda_train_input/dark_clouds_full_expanded_00002.dat.gz 0.9 0.1 58 500 model_dark_clouds_full_expanded_00002_500it
rm llda_train_input/dark_clouds_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/dark_clouds_full_expanded_00010.dat
python train_auto.py llda_train_input/dark_clouds_full_expanded_00010.dat.gz 0.9 0.1 58 500 model_dark_clouds_full_expanded_00010_500it
rm llda_train_input/dark_clouds_full_expanded_00010.dat.gz
##################### DIFFUSE CLOUDS #####################
:'
gzip -k llda_train_input/diffuse_clouds_tr.dat
python train_auto.py llda_train_input/diffuse_clouds_tr.dat.gz 2.1 0.003 24 500 model_diffuse_clouds_tr_500it
rm llda_train_input/diffuse_clouds_tr.dat.gz

gzip -k llda_train_input/diffuse_clouds_2.dat
python train_auto.py llda_train_input/diffuse_clouds_2.dat.gz 2.1 0.0003 24 500 model_diffuse_clouds_2_500it
rm llda_train_input/diffuse_clouds_2.dat.gz

gzip -k llda_train_input/diffuse_clouds_full.dat
python train_auto.py llda_train_input/diffuse_clouds_full.dat.gz 2.1 0.0002 24 500 model_diffuse_clouds_full_500it
rm llda_train_input/diffuse_clouds_full.dat.gz

gzip -k llda_train_input/diffuse_clouds_full_expanded_00002.dat
python train_auto.py llda_train_input/diffuse_clouds_full_expanded_00002.dat.gz 2.1 0.1 24 500 model_diffuse_clouds_full_expanded_00002_500it
rm llda_train_input/diffuse_clouds_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/diffuse_clouds_full_expanded_00010.dat
python train_auto.py llda_train_input/diffuse_clouds_full_expanded_00010.dat.gz 2.1 0.1 24 500 model_diffuse_clouds_full_expanded_00010_500it
rm llda_train_input/diffuse_clouds_full_expanded_00010.dat.gz
##################### COMETS #####################
:'
gzip -k llda_train_input/comets_tr.dat
python train_auto.py llda_train_input/comets_tr.dat.gz 1.7 0.003 30 500 model_comets_tr_500it
rm llda_train_input/comets_tr.dat.gz

gzip -k llda_train_input/comets_2.dat
python train_auto.py llda_train_input/comets_2.dat.gz 1.7 0.0004 30 500 model_comets_2_500it
rm llda_train_input/comets_2.dat.gz

gzip -k llda_train_input/comets_full.dat
python train_auto.py llda_train_input/comets_full.dat.gz 1.7 0.0003 30 500 model_comets_full_500it
rm llda_train_input/comets_full.dat.gz

gzip -k llda_train_input/comets_full_expanded_00002.dat
python train_auto.py llda_train_input/comets_full_expanded_00002.dat.gz 1.7 0.1 30 500 model_comets_full_expanded_00002_500it
rm llda_train_input/comets_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/comets_full_expanded_00010.dat
python train_auto.py llda_train_input/comets_full_expanded_00010.dat.gz 1.7 0.1 30 500 model_comets_full_expanded_00010_500it
rm llda_train_input/comets_full_expanded_00010.dat.gz
##################### EXTRAGALACTIC #####################
:'
gzip -k llda_train_input/extragalactic_tr.dat
python train_auto.py llda_train_input/extragalactic_tr.dat.gz 1.4 0.004 36 500 model_extragalactic_tr_500it
rm llda_train_input/extragalactic_tr.dat.gz

gzip -k llda_train_input/extragalactic_2.dat
python train_auto.py llda_train_input/extragalactic_2.dat.gz 1.4 0.0007 36 500 model_extragalactic_2_500it
rm llda_train_input/extragalactic_2.dat.gz

gzip -k llda_train_input/extragalactic_full.dat
python train_auto.py llda_train_input/extragalactic_full.dat.gz 1.4 0.0006 36 500 model_extragalactic_full_500it
rm llda_train_input/extragalactic_full.dat.gz

gzip -k llda_train_input/extragalactic_full_expanded_00002.dat
python train_auto.py llda_train_input/extragalactic_full_expanded_00002.dat.gz 1.4 0.1 36 500 model_extragalactic_full_expanded_00002_500it
rm llda_train_input/extragalactic_full_expanded_00002.dat.gz
'

gzip -k llda_train_input/extragalactic_full_expanded_00010.dat
python train_auto.py llda_train_input/extragalactic_full_expanded_00010.dat.gz 1.4 0.1 36 500 model_extragalactic_full_expanded_00010_500it
rm llda_train_input/extragalactic_full_expanded_00010.dat.gz
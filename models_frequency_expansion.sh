#cp ./llda_train_input/hot_cores_full.dat.gz .
#gunzip -d hot_cores_full.dat.gz 
#python ./scripts/frequency_expander.py hot_cores_full.dat 3 0.001
#rm hot_cores_full.dat
#mv hot_cores_full_expanded.dat ./llda_train_input/

cp ./llda_train_input/alma_band_6_full.dat.gz .
gunzip -d alma_band_6_full.dat.gz
python ./scripts/frequency_expander.py alma_band_6_full.dat 3 0.001
rm alma_band_6_full.dat
mv alma_band_6_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/planetary_full.dat.gz .
#gunzip -d planetary_full.dat.gz
#python ./scripts/frequency_expander.py planetary_full.dat 3 0.001
#rm planetary_full.dat
#mv planetary_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/agb_ppn_pn_full.dat.gz .
#gunzip -d agb_ppn_pn_full.dat.gz
#python ./scripts/frequency_expander.py agb_ppn_pn_full.dat 3 0.001
#rm agb_ppn_pn_full.dat
#mv agb_ppn_pn_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/dark_clouds_full.dat.gz .
#gunzip -d dark_clouds_full.dat.gz
#python ./scripts/frequency_expander.py dark_clouds_full.dat 3 0.001
#rm dark_clouds_full.dat
#mv dark_clouds_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/diffuse_clouds_full.dat.gz .
#gunzip -d diffuse_clouds_full.dat.gz
#python ./scripts/frequency_expander.py diffuse_clouds_full.dat 3 0.001
#rm diffuse_clouds_full.dat
#mv diffuse_clouds_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/comets_full.dat.gz .
#gunzip -d comets_full.dat.gz
#python ./scripts/frequency_expander.py comets_full.dat 3 0.001
#rm comets_full.dat
#mv comets_full_expanded.dat ./llda_train_input/

#cp ./llda_train_input/extragalactic_full.dat.gz .
#gunzip -d extragalactic_full.dat.gz
#python ./scripts/frequency_expander.py extragalactic_full.dat 3 0.001
#rm extragalactic_full.dat
#mv extragalactic_full_expanded.dat ./llda_train_input/

cp ./llda_train_input/hot_cores_full.dat.gz .
gunzip -d hot_cores_full.dat.gz 
python ./scripts/frequency_expander.py hot_cores_full.dat 3 0.001
rm hot_cores_full.dat
mv hot_cores_full_expanded.dat ./llda_train_input/

cp ./llda_train_input/alma_band_6_full.dat.gz .
gunzip -d alma_band_6_full.dat.gz
python ./scripts/frequency_expander.py alma_band_6_full.dat 3 0.001
rm alma_band_6_full.dat
mv alma_band_6_full_expanded.dat ./llda_train_input/

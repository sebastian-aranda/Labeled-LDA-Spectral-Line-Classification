cp ./llda_train_input/hot_cores_full.dat .
python ./scripts/frequency_expander.py hot_cores_full.dat 3 0.00002
mv hot_cores_full_expanded.dat ./llda_train_input/hot_cores_full_expanded_00002.dat

cp ./llda_train_input/alma_band_6_full.dat .
python ./scripts/frequency_expander.py alma_band_6_full.dat 3 0.00002
mv alma_band_6_full_expanded_00002.dat ./llda_train_input/

cp ./llda_train_input/planetary_full.dat .
python ./scripts/frequency_expander.py planetary_full.dat 3 0.00002
mv planetary_full_expanded_00002.dat ./llda_train_input/

cp ./llda_train_input/agb_ppn_pn_full.dat .
python ./scripts/frequency_expander.py agb_ppn_pn_full.dat 3 0.00002
mv agb_ppn_pn_full_expanded_00002.dat ./llda_train_input/

cp ./llda_train_input/dark_clouds_full.dat .
python ./scripts/frequency_expander.py dark_clouds_full.dat 3 0.00002
mv dark_clouds_full_expanded.dat ./llda_train_input/dark_clouds_full_expanded_00002.dat

cp ./llda_train_input/diffuse_clouds_full.dat .
python ./scripts/frequency_expander.py diffuse_clouds_full.dat 3 0.00002
mv diffuse_clouds_full_expanded.dat ./llda_train_input/diffuse_clouds_full_expanded_00002.dat

cp ./llda_train_input/comets_full.dat .
python ./scripts/frequency_expander.py comets_full.dat 3 0.00002
mv comets_full_expanded.dat ./llda_train_input/comets_full_expanded_00002.dat

cp ./llda_train_input/extragalactic_full.dat .
python ./scripts/frequency_expander.py extragalactic_full.dat 3 0.00002
mv extragalactic_full_expanded.dat ./llda_train_input/extragalactic_full_expanded_00002.dat

#Inference on 
CASA_SPECTRUM="CO_2_1_HD163296.dat"
REST_FREQ="230.53800"
OUTPUTS_PREFIX="HD163296.CO_2-1"

python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

#python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

#python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

#python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

#python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output


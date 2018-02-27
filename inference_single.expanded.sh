#Inference on 
CASA_SPECTRUM="CO_2_1_HD163296.dat"
REST_FREQ="230.53800"
OUTPUTS_PREFIX="HD163296.CO.2-1"

python auto.py llda_models/model_hot_cores_full_expanded_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_full_expanded.output

python auto.py llda_models/model_alma_band_6_full_expanded_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_full_expanded.output


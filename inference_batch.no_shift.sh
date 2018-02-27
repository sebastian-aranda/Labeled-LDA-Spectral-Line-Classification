#Inference on DMTAU.CS.5-4.dat
CASA_SPECTRUM="DMTAU.CS.5-4.dat"
REST_FREQ="244.93555"
OUTPUTS_PREFIX="DMTAU.CS.4-4"

python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Inference on CO_2_1_HD163296.dat
CASA_SPECTRUM="CO_2_1_HD163296.dat"
REST_FREQ="230.53800"
OUTPUTS_PREFIX="HD163296.CO.2-1"

python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Inference on HNC.dat
CASA_SPECTRUM="HNC.dat"
REST_FREQ="271.98111"
OUTPUTS_PREFIX="orion-IRc2.HNC"

python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Inference on HCO32.dat
CASA_SPECTRUM="HCO32.dat"
REST_FREQ="267.535"
OUTPUTS_PREFIX="IRS43.HCO_3-2"

python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output


#Inference on Orion-methanol.dat
#CASA_SPECTRUM="Orion-methanol.dat"
#REST_FREQ="229.75900"
#OUTPUTS_PREFIX="ORION-KL.CH3OH"

#python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

#python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

#python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

#python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

#python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

#python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Inference on TWHydra_CO3_2line.image.dat
#CASA_SPECTRUM="TWHydra_CO3_2line.image.dat"
#REST_FREQ="345.79599"
#OUTPUTS_PREFIX="TWHydra.C0.3-2"

#python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

#python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

#python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

#python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

#python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

#python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Inference on TWHydra_HCOplusline.image.dat
#CASA_SPECTRUM="TWHydra_HCOplusline.image.dat"
#REST_FREQ="356.73420"
#OUTPUTS_PREFIX="TWHydra.HCO.plus"

#python auto.no_shift.py llda_models/model_hot_cores_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_tr.output

#python auto.no_shift.py llda_models/model_hot_cores_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_2.output

#python auto.no_shift.py llda_models/model_hot_cores_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/hot_cores_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.hot_cores_full.output

#python auto.no_shift.py llda_models/model_alma_band_6_tr_500it/ 0 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_tr_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_tr.output

#python auto.no_shift.py llda_models/model_alma_band_6_2_500it/ 2 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_2_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_2.output

#python auto.no_shift.py llda_models/model_alma_band_6_full_500it/ 5 $REST_FREQ casa_spectrums/$CASA_SPECTRUM llda_train_input/alma_band_6_full_labelmap.sub
#mv output.dat $OUTPUTS_PREFIX.alma_band_6_full.output

#Ejemplos Alma Band 6
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/DMTau.CS_5-4.image.fits 77
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/HD163296_CO_2_1.image.fits 42
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/Orion.HNC.cbc.contsub.image.v2.fits 105
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/uid___A002_Xa916fc_X668__IRS43_HCO32.final.image.pbcor.fits 85
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/Orion.methanol.cbc.contsub.image.fits 90
python inference.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../FITS/Orion.methanol.cbc.contsub.image.v2.fits 90

#Ejemplos Alma Band 7
python inference.py llda_models/model_alma_band_7_full_500it/ llda_train_input/alma_band_7_full_features.dat llda_train_input/alma_band_7_full_labelmap.sub 5 ../../FITS/h2o_fits/Xa3a_ori_spw0.image.v2.fits 51
python inference.py llda_models/model_alma_band_7_full_500it/ llda_train_input/alma_band_7_full_features.dat llda_train_input/alma_band_7_full_labelmap.sub 5 ../../FITS/h2o_fits/Xa91_ori_spw0.image.v2.fits 51

#Ejemplos hot_cores
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/DMTau.CS_5-4.image.fits 12
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/B335_CS67.2freq.fits 12
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/B335_HCN43.2freq.fits 60
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/B335_HCOp43.2freq.fits 24
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/HD163296_CO_2_1.image.fits 68
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/Orion.HNC.cbc.contsub.image.v2.fits 75
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/Orion.methanol.cbc.contsub.image.fits 34
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/Orion.methanol.cbc.contsub.image.v2.fits 34
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/CH3OH_Map_X44c7.fits 34
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/uid___A002_Xa916fc_X668__IRS43_HCO32.final.image.pbcor.fits 24
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/TWHydra_CO3_2line.image.fits 68
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/TWHydra_HCOplusline.image.v2.fits 24
python inference.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../FITS/h2o_fits/Xa91_ori_spw0.image.v2.fits 20

#Ejemplos Diffuse Clouds
python inference.py llda_models/model_diffuse_clouds_full_500it/ llda_train_input/diffuse_clouds_full_features.dat llda_train_input/diffuse_clouds_full_labelmap.sub 5 ../../FITS/Orion.methanol.cbc.contsub.image.v2.fits 90

######## Ejemplos Sinteticos ########
# Carbon_Monoxide__COv\=0__1-0 [115.27120180] Energy [0]
python inference_synthetic.py llda_models/model_alma_band_3_2_500it/ llda_train_input/alma_band_3_2_features.dat llda_train_input/alma_band_3_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__1-0/trainingData.csv 0 38 #NOT FOUND

# Carbon_Monoxide__COv\=0__2-1 Freq [230.53800000] Energy [5.5321]
python inference_synthetic.py llda_models/model_alma_band_6_2_500it/ llda_train_input/alma_band_6_2_features.dat llda_train_input/alma_band_6_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__2-1/trainingData.csv 0 42

python inference_synthetic.py llda_models/model_alma_band_6_full_500it/ llda_train_input/alma_band_6_full_features.dat llda_train_input/alma_band_6_full_labelmap.sub 5 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__2-1/trainingData.csv 0 42

python inference_synthetic.py llda_models/model_alma_band_3_2_500it/ llda_train_input/alma_band_3_2_features.dat llda_train_input/alma_band_3_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__3-2/trainingData.csv 0 38
python inference_synthetic.py llda_models/model_alma_band_3_2_500it/ llda_train_input/alma_band_3_2_features.dat llda_train_input/alma_band_3_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__4-3/trainingData.csv 0 38
python inference_synthetic.py llda_models/model_alma_band_3_2_500it/ llda_train_input/alma_band_3_2_features.dat llda_train_input/alma_band_3_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__5-4/trainingData.csv 0 38
python inference_synthetic.py llda_models/model_alma_band_3_2_500it/ llda_train_input/alma_band_3_2_features.dat llda_train_input/alma_band_3_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Carbon_Monoxide/Carbon_Monoxide__COv\=0__6-5/trainingData.csv 0 38

python inference_synthetic.py llda_models/model_alma_band_7_2_500it/ llda_train_input/alma_band_7_2_features.dat llda_train_input/alma_band_7_2_labelmap.sub 2 ../../Synthetic_Spectrums_125/Formylium/Formylium__HCO+v\=0__4-3/trainingData.csv 0 73

######## Ejemplos survey ########
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 1,200 24,34,65,17,66,37,75,46,56,22,58,21,0,16,6,55,60
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 2,200 66,50,17,34,16,6,46,76,12,21,70,37,55,56,22,0,75,65
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 3,200 17,16,6,34,46,66,76,12,0,55,35,70,37,65,56,22
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 4,200 66,34,46,16,6,70,35,21,17,65,53,56,22,60,55,0,20,68,37
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 5,200 66,46,21,34,16,6,17,68,76,12,55,70,56,22

python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 1,100 0

python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 1,30 24,34,65,17,66,37,75,46,56,22
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 2,30 66,34,58,21,56,22,17,0
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 3,30 66,34,46
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 4,30 66,34,16,6,46
python inference_csv.py llda_models/model_hot_cores_full_500it/ llda_train_input/hot_cores_full_features.dat llda_train_input/hot_cores_full_labelmap.sub 5 ../../Schilke_OrionSurvey.csv 5,30 0,17,16,6,46,34,55,60,66

#Training model with hot_cores_tr
cp ./llda_train_input/hot_cores_tr.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.6 -beta 0.0008 -ntopics 85 -niters 500 -twords 10 -model model_hot_cores_tr_500it -dir . -dfile hot_cores_tr.dat.gz
mkdir ../llda_models/model_hot_cores_tr_500it
mv ./model_hot_cores_tr_500it.* ../llda_models/model_hot_cores_tr_500it/
rm ./hot_cores_tr.dat.gz
cd ..

#Model inference with hot_cores_tr
#java -mx512M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -inf -dir llda_models/ -model model_hot_cores_tr_500it -niters 500 -twords 10 -dfile ../spectrum.dat.gz

#Training model with hot_cores_2
cp ./llda_train_input/hot_cores_2.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.6 -beta 0.00004 -ntopics 85 -niters 500 -twords 10 -model model_hot_cores_2_500it -dir . -dfile hot_cores_2.dat.gz
mkdir ../llda_models/model_hot_cores_2_500it
mv ./model_hot_cores_2_500it.* ../llda_models/model_hot_cores_2_500it/
rm ./hot_cores_2.dat.gz
cd ..
 
#Training model with hot_cores_full
cp ./llda_train_input/hot_cores_full.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.6 -beta 0.00001 -ntopics 85 -niters 500 -twords 10 -model model_hot_cores_full_500it -dir . -dfile hot_cores_full.dat.gz
mkdir ../llda_models/model_hot_cores_full_500it
mv ./model_hot_cores_full_500it.* ../llda_models/model_hot_cores_full_500it/
rm ./hot_cores_full.dat.gz
cd ..

#Training model with alma_band_6_tr
cp ./llda_train_input/alma_band_6_tr.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.4 -beta 0.0008 -ntopics 124 -niters 500 -twords 10 -model model_alma_band_6_tr_500it -dir . -dfile alma_band_6_tr.dat.gz
mkdir ../llda_models/model_alma_band_6_tr_500it
mv ./model_alma_band_6_tr_500it.* ../llda_models/model_alma_band_6_tr_500it/
rm ./alma_band_6_tr.dat.gz
cd ..

#Training model with alma_band_6_2
cp ./llda_train_input/alma_band_6_2.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.4 -beta 0.00004 -ntopics 124 -niters 500 -twords 10 -model model_alma_band_6_2_500it -dir . -dfile alma_band_6_2.dat.gz
mkdir ../llda_models/model_alma_band_6_2_500it
mv ./model_alma_band_6_2_500it.* ../llda_models/model_alma_band_6_2_500it/
rm ./alma_band_6_2.dat.gz
cd ..

#Training model with alma_band_6_full
cp ./llda_train_input/alma_band_6_full.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.4 -beta 0.00001 -ntopics 124 -niters 500 -twords 10 -model model_alma_band_6_full_500it -dir . -dfile alma_band_6_full.dat.gz
mkdir ../llda_models/model_alma_band_6_full_500it
mv ./model_alma_band_6_full_500it.* ../llda_models/model_alma_band_6_full_500it/
rm ./alma_band_6_full.dat.gz
cd ..

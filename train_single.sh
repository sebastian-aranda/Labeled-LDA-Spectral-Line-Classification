#Training model with alma_band_6_tr
cp ./llda_train_input/alma_band_6_tr.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.4 -beta 0.0008 -ntopics 124 -niters 500 -twords 10 -m$
mkdir ../llda_models/model_alma_band_6_tr_500it
mv ./model_alma_band_6_tr_500it.* ../llda_models/model_alma_band_6_tr_500it/
rm ./alma_band_6_tr.dat.gz
cd ..

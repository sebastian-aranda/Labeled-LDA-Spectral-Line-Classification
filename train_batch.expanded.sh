#Training model with hot_cores_full_expanded
#cp ./llda_train_input/hot_cores_full_expanded.dat.gz ./JGibbLabeledLDA-master/
#cd ./JGibbLabeledLDA-master/
#java -mx4096M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.6 -beta 0.0008 -ntopics 85 -niters 500 -twords 10 -model model_hot_cores_full_expanded_500it -dir . -dfile hot_cores_full_expanded.dat.gz
#mkdir ../llda_models/model_hot_cores_full_expanded_500it
#mv ./model_hot_cores_full_expanded_500it.* ../llda_models/model_hot_cores_full_expanded_500it/
#rm ./hot_cores_full_expanded.dat.gz
#cd ..

#Training model with alma_band_6_full_expanded
cp ./llda_train_input/alma_band_6_full_expanded.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx4096M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 0.4 -beta 0.00001 -ntopics 124 -niters 500 -twords 10 -model model_alma_band_6_full_expanded_500it -dir . -dfile alma_band_6_full_expanded.dat.gz
mkdir ../llda_models/model_alma_band_6_full_expanded_500it
mv ./model_alma_band_6_full_expanded_500it.* ../llda_models/model_alma_band_6_full_expanded_500it/
rm ./alma_band_6_full_expanded.dat.gz
cd ..

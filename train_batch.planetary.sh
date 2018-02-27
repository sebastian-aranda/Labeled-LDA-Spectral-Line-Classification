#Training model with planetary_tr
cp ./llda_train_input/planetary_tr.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 2.4 -beta 0.0003 -ntopics 21 -niters 500 -twords 10 -model model_planetary_tr_500it -dir . -dfile planetary_tr.dat.gz
mkdir ../llda_models/model_planetary_tr_500it
mv ./model_planetary_tr_500it.* ../llda_models/model_planetary_tr_500it/
rm ./planetary_tr.dat.gz
cd ..

#Training model with planetary_2
cp ./llda_train_input/planetary_2.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 2.4 -beta 0.00009 -ntopics 21 -niters 500 -twords 10 -model model_planetary_2_500it -dir . -dfile planetary_2.dat.gz
mkdir ../llda_models/model_planetary_2_500it
mv ./model_planetary_2_500it.* ../llda_models/model_planetary_2_500it/
rm ./planetary_2.dat.gz
cd ..
 
#Training model with planetary_full
cp ./llda_train_input/planetary_full.dat.gz ./JGibbLabeledLDA-master/
cd ./JGibbLabeledLDA-master/
java -mx2048M -cp bin:lib/args4j-2.0.6.jar:lib/trove-3.0.3.jar jgibblda.LDA -est -alpha 2.4 -beta 0.00008 -ntopics 21 -niters 500 -twords 10 -model model_planetary_full_500it -dir . -dfile planetary_full.dat.gz
mkdir ../llda_models/model_planetary_full_500it
mv ./model_planetary_full_500it.* ../llda_models/model_planetary_full_500it/
rm ./planetary_full.dat.gz
cd ..

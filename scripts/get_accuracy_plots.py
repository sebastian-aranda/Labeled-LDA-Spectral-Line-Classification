# import matplotlib.pyplot as plt
# import matplotlib
# import numpy as np
# import sys
# import os

# if (len(sys.argv) != 2):
# 	print("e.g. python get_accuracy_plots.py results/results.accuracy.mean.csv")
# 	sys.exit(0)

# filename = sys.argv[1]

# font = {'family' : 'normal',
#         #'weight' : 'bold',
#         'size'   : 12}

# matplotlib.rc('font', **font)

# #Obtain models info
# model_names = list()
# model_accuracys = list()
# print("Reading Accuracy from "+filename)
# with open(filename) as f:
#     for line in f:
#         tokens = line.split(',')
#         model_names.append(tokens[0])
#         model_accuracys.append(float(tokens[1].rstrip()))

# #Obtain models vocabulary length
# model_vocabulary_len = list()
# for model in model_names:
#     if os.path.isfile('./llda_train_input/'+model+'_features.dat'):
#         with open('./llda_train_input/'+model+'_features.dat') as f:
#             line = f.readline()
#             model_vocabulary_len.append(len(line.split()))

# #Obtain models topics length
# model_topics_len = list()
# for model in model_names:
#     topics_count = 0
    
#     if 'expanded' in model:
#         tokens = model.split('_expanded')
#         labelmap_path = './llda_train_input/'+tokens[0]+'_labelmap.sub'
#     else:
#         labelmap_path = './llda_train_input/'+model+'_labelmap.sub'
    
#     if os.path.isfile(labelmap_path):
#         with open(labelmap_path) as f:
#             for line in f:
#                 topics_count += 1
    
#     model_topics_len.append(topics_count)

# results = zip(model_names, model_accuracys, model_vocabulary_len, model_topics_len)

# results_tr = list()
# results_2 = list()
# results_full = list()

# results_full_ex3_00050 = list()
# results_full_ex3_00100 = list()
# results_full_ex3_01000 = list()

# for model, accuracy, vlen, topics in results:
#     if model.endswith('tr'):
#         results_tr.append((model,accuracy,vlen,topics))
#     elif model.endswith('2'):
#         results_2.append((model,accuracy,vlen,topics))
#     elif model.endswith('full'):
#         results_full.append((model,accuracy,vlen,topics))
#     elif model.endswith('full_expanded_00050_x3'):
#         results_full_ex3_00050.append((model,accuracy,vlen,topics))
#     elif model.endswith('full_expanded_00100_x3'):
#         results_full_ex3_00100.append((model,accuracy,vlen,topics))
#     elif model.endswith('full_expanded_01000_x3'):
#         results_full_ex3_01000.append((model,accuracy,vlen,topics))

# def plotScoreBars(channeling, results,rows,cols,subplot, title=""):
#     axes = plt.gca()
    
#     res_sortedby_vocabulary_len = sorted(results,key=lambda x: x[2])
#     res_sortedby_topics_len = sorted(results,key=lambda x: x[3])
    
#     x = range(len(results))
    
#     plt.subplot(rows,cols,subplot)
#     plt.bar(x, [i[1] for i in res_sortedby_vocabulary_len], align='center')
#     plt.ylabel('Accuracy Score')
#     plt.title(title+'(sorted by n° of tokens)')
#     plt.xticks(x, [i[0] for i in res_sortedby_vocabulary_len],rotation='vertical')
#     plt.ylim(0, 1)
    
#     plt.subplot(rows,cols,subplot+3)
#     plt.bar(x, [i[1] for i in res_sortedby_topics_len], align='center')
#     plt.ylabel('Accuracy Score')
#     plt.title(title+'(sorted by n° of topics)')
#     plt.xticks(x, [i[0] for i in res_sortedby_topics_len],rotation='vertical')
#     plt.ylim(0, 1)

# plt.close('all')
# # fig = plt.figure(figsize=(48,32))
# fig = plt.figure()

# # plotScoreBars(0,results_tr,1,3,1,"Truncated models")
# # plotScoreBars(2,results_2,6,2,3,"Standard models with "+r"$\tau$"+" = 0.0005 [GHz]")
# # plotScoreBars(5,results_full,6,2,5,"Full models with "+r"$\tau$"+" = 0.0005 [GHz]")

# plotScoreBars(0,results_full_ex3_00050,2,3,1,"Expanded models with "+r"$\tau$"+" = 0.0005 [GHz]")
# plotScoreBars(2,results_full_ex3_00100,2,3,2,"Expanded models with "+r"$\tau$"+" = 0.001 [GHz]$")
# plotScoreBars(5,results_full_ex3_01000,2,3,3,"Expanded models with "+r"$\tau$"+" = 0.01 [GHz]$")

# plt.tight_layout()

# plt.show()
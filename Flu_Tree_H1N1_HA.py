# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:49:22 2016

@author: Rohan Koodli
"""

from Bio import SeqIO

#Use this one
new = list(SeqIO.parse('~/H1N1-HA-1000.fasta','fasta'))

#print len(new[13])
X0 = []

#adding to X and y

for i in range(0,len(new)-1):
    X0.append(new[i].seq)
    
#print len(X0)

y0 = []
for j in range(1,len(new)):
    y0.append(new[i].seq)
    
from Encoding_v2 import encoding

X = []
for k in range(len(X0)):
    encoded_X = encoding(X0[k])
    X.append(encoded_X)
    
y = []
for l in range(len(y0)):
    encoded_y = encoding(y0[l])
    y.append(encoded_y)
'''
print len(X[0])
print len(y[298])

a = [1,2,3,4,5]
print len(a)

from Compare_Strains import test_length

print len(X[0])
print len(y[0])
print len(X[0]) == len(y[0])
#print test_length(X,y)
'''

from sklearn import tree
from sklearn import metrics

dtr = tree.DecisionTreeRegressor()
dtr.fit(X,y)

from sklearn import cross_validation
dtrscores = cross_validation.cross_val_score(dtr,X,y,cv=2)
print 'Decision Trees',dtrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (dtrscores.mean()*100, dtrscores.std() *100))

from sklearn import ensemble
rfr = ensemble.RandomForestRegressor(n_estimators=20)
rfr.fit(X,y)

rfrscores = cross_validation.cross_val_score(rfr,X,y,cv=2)
print 'Random Forests',rfrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (rfrscores.mean()*100, rfrscores.std() *100))

ext = ensemble.ExtraTreesRegressor(n_estimators=3)
ext.fit(X,y)

extscores = cross_validation.cross_val_score(ext,X,y,cv=2)
print 'Extra Trees',extscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (extscores.mean()*100, extscores.std() *100))

#print str.format('{0:.15f}',f)



X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.5,random_state=50)

dtr.fit(X_train,y_train)
print dtr.score(X_test,y_test)

rfr.fit(X_train,y_train)
print rfr.score(X_test,y_test)

ext.fit(X_train,y_train)
print ext.score(X_test,y_test)

'''
R^2 score (R2 score)
How well the model fits a particular dataset
Generally from 0 to 1 (1 is best)
0 means X does not help predicting y
negative values possible if model is that bad
'''

'''
variance_weighted - Scores of all outputs are averaged, weighted by the 
                        variances of each individual output
uniform_average - Scores of all outputs are averaged with uniform weight
'''
y_pred_rfr = rfr.predict(X_test)
print 'Random Forests R2 score:', metrics.r2_score(y_test,y_pred_rfr,multioutput='variance_weighted')
print 'Random Forests MSE:', metrics.mean_squared_error(y_test,y_pred_rfr)

y_pred_dtr = dtr.predict(X_test)
print 'Decision Trees R2 score:', metrics.r2_score(y_test,y_pred_dtr,multioutput='variance_weighted')

y_pred_ext = ext.predict(X_test)
print 'Extra Trees R2 score:', metrics.r2_score(y_test,y_pred_ext,multioutput='variance_weighted')

'''
Gradient Boosting
'''

params = {'n_estimators': 199, 'max_depth': 20, 'min_samples_split': 10,
          'learning_rate': 0.01, 'loss': 'ls'}
          
gbr = ensemble.GradientBoostingRegressor(**params)
#gbr.fit(X_train,y_train)

#y_pred_gbr = gbr.predict(X_test)
#print 'GBR R2 score:', metrics.r2_score(y_test,y_pred_gbr,multioutput='uniform_average')






'''
from sklearn import neighbors
knr = neighbors.KNeighborsRegressor()
knr.fit(X,y)

knrscores = cross_validation.cross_val_score(knr,X,y,cv=10)
print knrscores
'''
'''
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y)#,test_size=0.5,random_state=10)

dtr2 = tree.DecisionTreeRegressor()
dtr2.fit(X_train,y_train)
print dtr2.score(X_test,y_test)
'''


    
'''    
print X[0][0]
print y[0][0]

from Compare_Strains import compare_strains
print compare_strains(X[0],y[0])
'''





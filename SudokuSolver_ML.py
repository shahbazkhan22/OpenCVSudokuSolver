# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:23:43 2018

@author: shahb
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:03:56 2018

@author: shabs
"""

import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

print("---------------Loading Data----------")
data = pd.read_csv('F:/Docs/Py_ML/DataSet/train.csv').as_matrix()
print("----------- Data Loaded-------------")

print("---------------Running Classifier--------------")
clf = DecisionTreeClassifier()

xtrain = data[0:42000,1:]
train_label = data[0:42000,0]

clf.fit(xtrain,train_label)
print("------------Data Classified-------------")

test = pd.read_csv('F:/Docs/Python Progs openCV/test.csv').as_matrix()
#test_label = data[33600:,0]

print("--------------Predicting----------------")
pred = clf.predict(test)
print(pred)

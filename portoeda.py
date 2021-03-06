# -*- coding: utf-8 -*-
"""portoeda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jhg9E1yUj-aRfxul2HtJWYzlGgd_ZWAA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

porto = pd.read_csv("../input/porto-data/train.csv");
portotest = pd.read_csv("../input/porto-data/test.csv");

porto.info()

porto.target.plot.hist()

df = porto.copy()
target = df['target']
x =  target.value_counts()
#claim = (x[1]/df.shape[1])
print("Claimed Insurance : ", (x[1] / df.shape[0])* 100)
print("No Claimed Insurance : ", (x[0] / df.shape[0])* 100)

features_miss= []

for i in df.columns:
    missing = df[df[i] == -1][i].count()
    if missing > 0:
        features_miss.append(i)
        miss_percent = missing/df.shape[0]
        
        print(i," : ",  miss_percent*100)

df.drop(columns=['ps_car_03_cat','id'],axis=1,inplace=True)
df.drop(columns=['target'],axis=1,inplace=True)
col=df.columns

col

def boxplotgraph(dataset):
    plt.figure(figsize=(25,25))
    for i in enumerate(dataset):
        plt.subplot(7,3,i[0]+1)
        sns.boxplot(x = 'target',y = dataset[i[1]],hue = 'target', data = dataset)

def histplot(dataset):
    plt.figure(figsize=(20,20))
    for i in enumerate(dataset):
        plt.subplot(7,3,i[0]+1)
        plt.ylabel('Count')
        plt.xlabel(i[1])
        plt.hist(x = i[1], data = dataset, bins  =40)
        plt.tight_layout()

def cormap(dataset):
    plt.figure(figsize=(20,15))
    sns.heatmap(dataset.corr(), cmap='Reds', annot = True, linewidths=0.01)

calc=[cols for cols in df.columns if cols.find("calc")!=-1]
calc_data=df.loc[:,calc]
calc_data.head()

calc_data = pd.concat([calc_data, target], axis=1)

cormap(calc_data)

plt.figure(figsize=(20,20))
plt.title("Count Plots of CALC Features")
for i in enumerate(calc_data):
    plt.subplot(7,3,i[0]+1)
    plt.ylabel('Count')
    sns.countplot(i[1], hue = 'target', data = calc_data)
    plt.tight_layout()

histplot(calc_data)

boxplotgraph(calc_data)

val0 = porto[porto['target'] == 0]
t = val0['target']
cal_0=[cols for cols in val0.columns if cols.find("calc")!=-1]
calc0=val0.loc[:,cal_0]
calc0 = pd.concat([calc0, t], axis=1)

histplot(calc0)

val1 = porto[porto['target'] == 1]
t1 = val1['target']
cal_1=[cols for cols in val1.columns if cols.find("calc")!=-1]
calc1=val1.loc[:,cal_1]
calc1 = pd.concat([calc1, t], axis=1)

histplot(calc1)

df.drop(calc, axis = 1, inplace = True)
df.columns

bincol=[cols for cols in df.columns if cols.find("bin")!=-1 ]
cat=[cols for cols in df.columns if cols.find("cat")!=-1 ]
normalcom=[cols for cols in df.columns if cols.find("bin")==-1 & cols.find("cat")==-1 ]

normal_data = porto.loc[:,normalcom]
normal_data['target'] = target
normal_data.columns

boxplotgraph(normal_data)

cormap(normal_data)


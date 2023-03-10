# -*- coding: utf-8 -*-
"""ILPD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aa-zM5sQPS-Npk1BYjuur35UZQzy1ZI2
"""

#modul Exploratory Data Analisis Packages
import pandas as pd
import numpy as np
# packages visualisasi 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Load Machine Learning Packages
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# For Metrics
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.model_selection import train_test_split

"""## 1. Reading Dataset and Creating dataframe"""

data = pd.read_csv("Indian_Liver_Patient_Dataset_(ILPD).csv")
data

"""## 2. Analyzing the data

2.1 checking the data head
"""

data.head(10)

"""2.2 Checking the Number of Rows and Column"""

data.shape

"""number of rows in dataframe are : 583
\
number of columns in dataframe are : 11

2.3 Checking the names of columns in dataset
"""

data.columns

"""2.4 Chekcing the information of dataframe"""

data.info()

"""2.5 Checking null value"""

#checking data
data.isnull().sum()

"""2.6 fillna null value """

data.update(data.fillna(data.mean()))

"""2.7 Rechecking null value"""

data.isnull().sum()

"""2.8 Encoding Gender """

from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()

data['Gender'] = LE.fit_transform(data['Gender'].astype(str)) 

# 0 : Female
# 1 : Male

"""2.9 Checking Statistical data of dataframe"""

data.describe()

"""2.10 cheking unique values in dataframe"""

data.nunique()

"""Highest number of unique values are in column

2.11 Checking Class Distribution
"""

data["Selector_field"]=data["Selector_field"].replace(2,0)

no_disease = data[data["Selector_field"]==0]
disease = data[data["Selector_field"]==1]

print(no_disease.shape,disease.shape)

"""## 3. Data Visualization

3.1 Displot for various features
"""

columns=data.columns
columns=list(columns)
columns.pop()

colours=['b','c','g','k','m','r','y','b','b','c','g']

sns.set(rc={'figure.figsize':(12,17)})
sns.set_style(style='white')
for i in range(len(columns)):
    
    plt.subplot(7,2,i+1)
    sns.distplot(data[columns[i]], hist=True, rug=True, color=colours[i])

"""None of the graphs here are following a normal dstribution

4.2 Violinplot for outcome vs other attributes
"""

sns.set(rc={'figure.figsize':(15,17)})
colors_list = ['#78C850', '#F08030']
j=1
sns.set_style(style='white')

for i in (columns):
    plt.subplot(7,2,j)

    sns.violinplot(x="Selector_field", y=i,data=data, kind="violin", split=True, height=4, aspect=.7,palette=colors_list)
       
    sns.swarmplot(x='Selector_field', y=i,data=data, color="k", alpha=0.8)
    

    j=j+1

"""3.3 ScatterPlot of all atributes against each other"""

sns.set(rc={'figure.figsize':(20,100)})
j=1

sns.set_style(style='white')
for i in range(len(columns)):
    for k in range(i,len(columns)):
        try:
            if i==k:
                continue
            plt.subplot(22,2,j)
            sns.scatterplot(x=data[columns[i]],y=data[columns[k]],hue="Selector_field",data=data)
            j=j+1
        except:
            break

"""3.4 strip plot distribution of attributes vs outcome"""

sns.set(rc={'figure.figsize':(15,15)})
j=1
sns.set_style(style='white')

for i in range(len(columns)):
    plt.subplot(8,2,j)
    sns.stripplot(x='Selector_field', y=columns[i] , data=data)
    j=j+1

"""3.5 plotting the pair plot"""

sns.set(rc={'figure.figsize':(15,100)})
sns.set_style(style='white')

sns.pairplot(data, hue='Selector_field')

"""3.6 Correlation"""

correlation_matrix=data.corr().round(2)
correlation_matrix["Selector_field"].sort_values(ascending=False)

# Plot Correlation with Heatmap
plt.figure(figsize=(20,10))
sns.heatmap(data.corr(),annot=True)
plt.show()

"""3.7 Distribution of target variabel"""

plt.figure(figsize=(6,8))
sns.set_style(style='white')
sns.countplot(data['Selector_field'])

"""## 4. Data Preprocessing

4.1 Features Engineering
"""

from sklearn.preprocessing import MinMaxScaler
scaleIt = MinMaxScaler()
columns_to_be_scaled = [c for c in data.columns if data[c].max() > 1]
print("The columns which are to be scaled are :",columns_to_be_scaled)

scaled_columns = scaleIt.fit_transform(data[columns_to_be_scaled])
scaled_columns = pd.DataFrame(scaled_columns, columns=columns_to_be_scaled)
scaled_columns['Selector_field'] = data['Selector_field'] 



#copying the scaled DataFrame to original DataFrame

data=scaled_columns
data

"""4.2 Dividing the data into X and Y"""

X = data.drop(["Selector_field"],axis=1)
y = data["Selector_field"]

print(X.head(5))
print(y.head(5))

"""4.3 Using RandomOverSampler to handle class imbalance"""

from imblearn.over_sampling import RandomOverSampler
os = RandomOverSampler(random_state=10)

X_res,y_res=os.fit_resample(X,y)

X_res.shape,y_res.shape

"""4.4 Train Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_res,y_res , test_size = 0.2, random_state = 10)

"""## 5. Build a Model

## 5.1 Random Forest
"""

from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import GridSearchCV
param_grid={'n_estimators':range(80,201,5),'criterion':['gini','entropy'],'max_features':['auto','sqrt','log2',None]}

tuning = GridSearchCV(estimator=RandomForestClassifier(),param_grid=param_grid,cv=5,verbose=2,n_jobs=-1,scoring='f1')
tuning.fit(X_train,y_train)
tuning.best_params_,tuning.best_score_

classifierRF = RandomForestClassifier(n_estimators=85,criterion='gini',random_state=10,max_features='sqrt')

model_RF = classifierRF.fit(X_train,y_train)
y_pred_RF = model_RF.predict(X_test)

from sklearn.model_selection import cross_val_score
score_RF = cross_val_score(model_RF,X_train,y_train,cv=10)

#Random forest classifier
print("Maximum Accuracy : ",round(max(score_RF)*100,2),"%")
print("Average Accuracy : ",round(score_RF.mean()*100,2),"%")
print("Average Deviation : ",round(score_RF.std()*100,2),"%")

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test,y_pred_RF))

from sklearn.metrics import plot_roc_curve
plot_roc_curve(model_RF,X_test,y_test)

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(confusion_matrix(y_test,y_pred_RF))
print(classification_report(y_test,y_pred_RF))

import joblib

# Save Decision Tree Model
model_file_dt = open("random_forest_model_ILPD.pkl","wb")
joblib.dump(model_RF,model_file_dt)
model_file_dt.close()

"""## 5.2 Logistic Reggresion"""

from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

model_LR=LogisticRegression(max_iter=12,solver='newton-cg',random_state=10)
model_LR.fit(X_train, y_train)
y_pred_LR = model_LR.predict(X_test)

from numpy.core.numeric import cross
from sklearn.model_selection import cross_val_score
score_LR=cross_val_score(model_LR,X_train,y_train,cv=10)
score_LR

#Logistik classifier
print("Maximum Accuracy : ",round(max(score_LR)*100,2),"%")
print("Average Accuracy : ",round(score_LR.mean()*100,2),"%")
print("Average Deviation : ",round(score_LR.std()*100,2),"%")

from sklearn.metrics import roc_auc_score, plot_roc_curve
print(roc_auc_score(y_test,y_pred_LR))

plot_roc_curve(model_LR,X_test,y_test)

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(confusion_matrix(y_test,y_pred_LR))
print(classification_report(y_test,y_pred_LR))

"""## KNN"""

from sklearn.neighbors import KNeighborsClassifier

classifier_KNN = KNeighborsClassifier(n_neighbors=2,p=2,algorithm='auto',weights='uniform')
classifier_KNN.fit(X_train,y_train)
y_pred_KNN=classifier_KNN.predict(X_test)
print(y_pred_KNN)
print(y_test)

score_KNN = cross_val_score(classifier_KNN,X_train,y_train,cv=10)
score_KNN

#KNN classifier
print("Maximum Accuracy : ",round(max(score_KNN)*100,2),"%")
print("Average Accuracy : ",round(score_KNN.mean()*100,2),"%")
print("Average Deviation : ",round(score_KNN.std()*100,2),"%")

print(roc_auc_score(y_test,y_pred_KNN))

plot_roc_curve(classifier_KNN,X_test,y_test)

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(confusion_matrix(y_test,y_pred_KNN))
print(classification_report(y_test,y_pred_KNN))

"""## 5.4 Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

classifier_DT = DecisionTreeClassifier(max_depth = 3)
model_DT = classifier_DT.fit(X_train, y_train)
y_pred_DT = model_DT.predict(X_test)

from sklearn.model_selection import cross_val_score
score_DT = cross_val_score(model_DT,X_train,y_train,cv=10)

#DT classifier
print("Maximum Accuracy : ",round(max(score_DT)*100,2),"%")
print("Average Accuracy : ",round(score_DT.mean()*100,2),"%")
print("Average Deviation : ",round(score_DT.std()*100,2),"%")

roc_auc_score(y_test,y_pred_DT)

plot_roc_curve(model_DT, X_test, y_test)

print(confusion_matrix(y_test, y_pred_DT))
print(classification_report(y_test,y_pred_DT))

"""## 5.5 Naive Bayes"""

from sklearn.naive_bayes import GaussianNB

classifier_NB = GaussianNB()

model_NB = classifier_NB.fit(X_train,y_train)
y_pred_NB = model_NB.predict(X_test)

score_NB = cross_val_score(model_NB,X_train,y_train,cv=10)

#NB classifier
print("Maximum Accuracy : ",round(max(score_NB)*100,2),"%")
print("Average Accuracy : ",round(score_NB.mean()*100,2),"%")
print("Average Deviation : ",round(score_NB.std()*100,2),"%")

roc_auc_score(y_test, y_pred_NB)

plot_roc_curve(model_NB, X_test, y_test)

print(confusion_matrix(y_test,y_pred_NB))
print(classification_report(y_test,y_pred_NB))

"""## 5.6 XGBoost"""

import xgboost as xgb

classifier_XGB = xgb.XGBClassifier(use_label_encoder=False)
model_XGB = classifier_XGB.fit(X_train, y_train)
y_pred_XGB = model_XGB.predict(X_test)

score_XGB = cross_val_score(model_XGB,X_train,y_train,cv=10)

#NB classifier
print("Maximum Accuracy : ",round(max(score_XGB)*100,2),"%")
print("Average Accuracy : ",round(score_XGB.mean()*100,2),"%")
print("Average Deviation : ",round(score_XGB.std()*100,2),"%")

roc_auc_score(y_test, y_pred_XGB)

plot_roc_curve(model_XGB,X_test,y_test)

print(confusion_matrix(y_test,y_pred_XGB))
print(classification_report(y_test,y_pred_XGB))
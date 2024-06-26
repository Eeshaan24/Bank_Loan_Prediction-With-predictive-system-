# -*- coding: utf-8 -*-
"""Fraudulent_Bank_Loan_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zU01joRqGlCuca3dZf_fceJ1_jd0Zh7f
"""

import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

data = pd.read_csv('/content/train_u6lujuX_CVtuZ9i (1).csv')

data.head()

data.tail()

data.describe()

data.info()

data.shape

#no.of missing values in each column

data.isnull().sum()

data = data.dropna()

data.isnull().sum()

#label_encoding

data.replace({"Loan_Status":{'N':0, 'Y':1}}, inplace = True)

data.head()

# dependent columns

data['Dependents'].value_counts()

data = data.replace(to_replace = '3+' , value=4)

data['Dependents'].value_counts()

#DATA VISUALISATION

sns.countplot(x='Education', hue = 'Loan_Status', data = data)

sns.countplot(x = 'Married', hue = 'Loan_Status', data = data)

#converting all categorical to numerical

data.replace({'Married': {'No':0, 'Yes':1}, 'Gender':{'Male':1, 'Female':0}, 'Self_Employed':{'No':0, 'Yes':1},
              'Property_Area':{'Rural':0, 'Semiurban':1, 'Urban':2}, 'Education':{'Graduate':1, 'Not Graduate':0}}, inplace = True)

data.head()

#separating the data and label

X = data.drop(columns = ['Loan_ID', 'Loan_Status'], axis = 1)
Y = data['Loan_Status']

print(X)
print(Y)

#Splitting into training and testing

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

classifier = svm.SVC(kernel = 'linear')

#training the model

classifier.fit(X_train, Y_train)

#model_evaluation

X_train_prediction = classifier.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction, Y_train)



print("Accuracy on Training :" , training_accuracy)

X_test_prediction = classifier.predict(X_test)
test_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Accuracy on Testing :" , test_accuracy)

from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier()
rf_clf.fit(X_train, Y_train)

X_test_prediction_2 = rf_clf.predict(X_test)

Accuracy_RF = accuracy_score(X_test_prediction_2, Y_test)
print("Accuracy: ", Accuracy_RF)

from sklearn.naive_bayes import GaussianNB
nb_clf = GaussianNB()
nb_clf.fit(X_train, Y_train)

X_test_prediction_3 = nb_clf.predict(X_test)
Accuracy_NB = accuracy_score(X_test_prediction_3, Y_test)

print("Accuracy for GuassianNB: ", Accuracy_NB)

from sklearn.tree import DecisionTreeClassifier

dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, Y_train)

X_test_prediction_4 = dt_clf.predict(X_test)
Accuracy_DT = accuracy_score(X_test_prediction_4, Y_test)

print("Accuracy for DT: ", Accuracy_DT)

from sklearn.neighbors import KNeighborsClassifier

kn_clf = KNeighborsClassifier()
kn_clf.fit(X_train, Y_train)

X_test_prediction_5 = kn_clf.predict(X_test)
Accuracy_KN = accuracy_score(X_test_prediction_5, Y_test)

print("Accuracy for KN: ", Accuracy_KN)

import matplotlib.pyplot as plt

Y_set = [Accuracy_RF, Accuracy_NB, Accuracy_KN, Accuracy_DT, test_accuracy]
X_set = ['RF', 'NB', 'KNN', 'DT', 'SVM']

index = ['RF', 'NB', 'KNN', 'DT', 'SVM']

df = pd.DataFrame({'accuracy_score': Y_set, 'Models': X_set}, index = index)
ax = df.plot.bar(rot=0)

#INFERENCE
#puttin input data any values for prediction based on information given

#we can see from graph gaussianNB and SVM both have equal accuracy ( we can chose any 1 but since SVM takes bit time to train its recommendavle to use GuassianNB)
input_data = (1,1,2,1,1,5417,4196,267,360,1,2)

input_data_as_array = np.asarray(input_data)

input_data_reshaped = input_data_as_array.reshape(1,-1)

prediction = nb_clf.predict(input_data_reshaped)
#print(prediction)

if(prediction[0]==1):
  print("Yes")
else:
  print("No")
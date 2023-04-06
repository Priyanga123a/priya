# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gaWjZY3-M3dHbHMFD2l6oJV5tp03Q2E_
"""

import numpy as np

import pandas as pd

import os

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn import svm

from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

from sklearn import metrics

from sklearn.model_selection import cross_val_score

from sklearn import preprocessing

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import joblib

from sklearn.metrics import accuracy_score

df = pd.read_csv(r"/content/collegePlace.csv")
df.head()

df.info()

df.isnull().sum()

def transformationplot(feature):

  plt.figure(figsize=(12,5)) 
  plt.subplot(1,2,1) 
  sns.distplot(feature)

  transformationplot(np.log(df['Age']))

df = df.replace(['Male'], [8])
df = df.replace(['Female'], [1])

df = df.replace(['Computer Science', 'Information Technology', 'Electronics And Communication', 'Mechanical', 'Electrical', 'Civil'], [0,1,2,3,4,5])

df = df.drop(['Hostel'], axis=1)

df

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df['CGPA'], color='r')

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df['PlacedOrNot'], color='r')

plt.figure(figsize=(18,4))
plt.subplot(1, 4, 1)
sns.countplot(df['Gender'])
plt.subplot(1, 4, 2)
sns.countplot(df['Stream'])
plt.show()

plt.figure(figsize=(20,5))
plt.subplot(131)
sns.countplot(data=df, x="PlacedOrNot", hue="CGPA")

sns.swarmplot(x=df['PlacedOrNot'], y=df['CGPA'], hue=df['Stream'])
plt.show()

x = df.drop(['HistoryOfBacklogs'], axis=1)
y = df['Internships']

sc = StandardScaler()

x_bal = sc.fit_transform(x)

print(x_bal)

names = x.columns
x_bal = pd.DataFrame(x_bal,columns=names)
print(x_bal)

print(df.columns)

if 'Gender' in df.columns and 'Stream' in df.columns:
    df = pd.get_dummies(df, columns=['Gender', 'Stream'], drop_first=True)

X = df.drop(['PlacedOrNot'], axis=1)

scaler = StandardScaler()

standardized_data = scaler.fit_transform(X)

X = standardized_data

Y = df['PlacedOrNot']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)
print("X_test shape:", X_test.shape)
print("Y_test shape:", Y_test.shape)
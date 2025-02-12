#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
dataset = pd.read_csv("credit_card_fraud_dataset.csv")

# Visualizations
sns.violinplot(x="Amount", y="TransactionType", data=dataset)
sns.barplot(x="IsFraud", y="Location", data=dataset)

# Encoding categorical variables
le = LabelEncoder()
dataset['TransactionType'] = le.fit_transform(dataset['TransactionType'])
dataset['Location'] = le.fit_transform(dataset['Location'])

# Selecting features and target variable
x = dataset.iloc[:, 2:6]
y = dataset.iloc[:, -1]

# Splitting dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

# Training Logistic Regression model
regressor = LogisticRegression()
regressor.fit(x_train, y_train)

# Prediction based on user input
amount = int(input("Enter the amount: "))
id = int(input("Enter the merchant id: "))
type = int(input("Enter the transaction type: "))
location = int(input("Enter the location: "))

arr = [amount, id, type, location]
input1_as_numpy = np.asarray(arr)
input1_reshaped = input1_as_numpy.reshape(1, -1)
prediction = regressor.predict(input1_reshaped)

print("Prediction:", prediction)
if prediction == 1:
    print("The transaction is fraud")
else:
    print("The transaction is not fraud")

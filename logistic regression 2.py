#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


dataset=pd.read_csv("credit_card_fraud_dataset.csv")


# In[4]:


dataset


# In[5]:


sns.violinplot(x="Amount",y="TransactionType",data=dataset)


# In[6]:


sns.barplot(x="IsFraud",y="Location",data=dataset)


# In[15]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['TransactionType']=le.fit_transform(dataset['TransactionType'])
dataset['Location']=le.fit_transform(dataset['Location'])


# In[42]:


x=dataset.iloc[:,2:6]


# In[43]:


x


# In[44]:


y=dataset.iloc[:,-1]


# In[45]:


y


# In[46]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)


# In[47]:


x_train


# In[48]:


from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(x_train,y_train)


# In[ ]:





# In[49]:


amount=int(input("Enter the amount :"))
id=int(input("Enter the merchant id:"))
type=int(input("Enter the transaction type:"))
location=int(input("Enter the location:"))
arr=[amount,id,type,location]
input1=arr
input1_as_numpy=np.asarray(input1)
input1_reshaped=input1_as_numpy.reshape(1,-1)
prediction=regressor.predict(input1_reshaped)
print("Prediction:",prediction)
if(prediction==1):
    print("The transaction is fraud")
else:
    print("The transaction is not fraud")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# In[7]:


#import data
print('.....Loading......')
data_train = pd.read_excel(r'C:\Users\DELL\Documents\raw\SWaT_Dataset_Normal_v0.xlsx',header = 0, index_col = None)
data_attack = pd.read_excel(r'C:\Users\DELL\Documents\raw\SWaT_Dataset_Attack_v0.xlsx.xlsx',header = 0, index_col = None)


# In[7]:


# Remove unnecessary data
col_remove = ['Timestamp','P102','P401','P601','P603']


# In[ ]:


#Excecute column remove
data_train = data_train.drop(columns = col_remove, axis = 1)
data_attack = data_attack.drop(columns = col_remove, axis = 1)


# In[3]:


#Normalize data
data_train.replace('A ttack','Attack', inplace = True)
data_train.replace(['Normal','Attack'],[0,1], inplace = True)
data_attack.replace(['Normal','Attack'],[0,1], inplace = True)
scaler = MinMaxScaler()


# In[4]:


# Train data
data_train = scaler.fit_transform(data_train.iloc[:,:-1]);
data_attack = scaler.transform(data_attack.iloc[:,:-1]);
attack_anomaly = np.array[data_attack['Normal/Attack'] == 1].toList


# In[6]:


#Save File
np.savez('pr_processing.npz', train = data_train, test = data_attack,idx_anomaly = attack_anomaly)


# In[ ]:





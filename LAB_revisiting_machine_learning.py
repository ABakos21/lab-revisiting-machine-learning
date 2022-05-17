#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv('learningSet.csv')


# In[3]:


data.info()


# In[4]:


data.describe()


# In[5]:


categorical = data.select_dtypes(include=['object'])


# In[6]:


categorical.shape


# In[7]:


#Check for null values in all the columns:

nulls = pd.DataFrame(categorical.isna().sum()/len(categorical)).reset_index()
nulls.columns = ['column_name', 'percentage']
nulls.sort_values('percentage', ascending=False)


# In[8]:


nulls[nulls['percentage']>0]


# In[9]:


#Exclude the following variables by looking at the definitions. Create a new empty list called drop_list. We will append this list and then drop all the columns in this list later:
#OSOURCE - symbol definitions not provided, too many categories
#ZIP CODE - we are including state alread

categorical = categorical.drop(['OSOURCE', 'ZIP'], axis =1)
drop_list = []


# In[10]:


# Identify columns that over 85% missing values

nulls[nulls['percentage'] > 0.85]


# In[11]:


#Remove those columns from the dataframe

#there are none to remove


# In[12]:


#Reduce the number of categories in the column GENDER. The column should only have either "M" for males, "F" for females, and "other" for all the rest

categorical['GENDER'] = categorical['GENDER'].fillna('F')


# In[13]:


categorical['GENDER'].value_counts(dropna=False)


# In[14]:


categorical['GENDER'] = np.where(categorical['GENDER'].isin(['F','M']), categorical['GENDER'], "other")
categorical.GENDER.value_counts()


# In[ ]:





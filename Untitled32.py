#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(5)


# In[6]:


df.isnull().sum()/len(df)*100


# In[8]:


df.dtypes


# In[13]:


df['LaunchSite'].value_counts()


# In[15]:


df['Orbit'].value_counts()


# In[18]:


landing_outcomes=df['Outcome'].value_counts()
landing_outcomes


# In[20]:


for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)


# In[22]:


bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes


# In[31]:


landing_class= df['Outcome'].map(lambda x : 0 if x in bad_outcomes else 1)
landing_class.value_counts()


# In[33]:


df['Class']=landing_class
df.head()


# In[35]:


df['Class'].mean()


# In[37]:


df.to_csv('dataset_part_2.csv', index=False)


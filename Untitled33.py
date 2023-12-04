#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


import csv, sqlite3

connection= sqlite3.connect("my_data1.db")
cursor= connection.cursor()



# In[3]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ibm_db_sa')
get_ipython().system('pip install ipython-sql')
get_ipython().system('pip install -q pandas==1.1.5')


# In[11]:


get_ipython().system('pip install ibm_db_sa')




# In[12]:


get_ipython().system('pip install ipython-sql')
get_ipython().system('pip install -q pandas==1.1.5')


# In[18]:


get_ipython().run_line_magic('sql', 'sqlite:///my_data1.db')


# In[14]:


get_ipython().run_line_magic('reload_ext', 'sql')


# In[15]:


import csv, sqlite3

connection= sqlite3.connect("my_data1.db")
cursor= connection.cursor()


# In[16]:


import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", connection, if_exists='replace', index=False,method="multi")

df.head()


# In[19]:


import sqlalchemy
get_ipython().run_line_magic('sql', 'create table SPACEXTABLE as select * from SPACEXTBL where Date is not null')


# In[20]:


get_ipython().run_line_magic('sql', 'select distinct LAUNCH_SITE from SPACEXTABLE;')


# In[26]:


get_ipython().run_line_magic('sql', 'select * from SPACEXTABLE where LAUNCH_SITE like "CCA%" limit 5;')


# In[29]:


get_ipython().run_line_magic('sql', 'select sum(PAYLOAD_MASS__KG_) from SPACEXTABLE;')


# In[35]:


get_ipython().run_line_magic('sql', 'select avg(PAYLOAD_MASS__KG_) from SPACEXTABLE where "Booster_Version"="F9 v1.1";')


# In[38]:


get_ipython().run_line_magic('sql', 'select min(DATE) from SPACEXTABLE where "Landing_Outcome"="Success (ground pad)"')


# In[45]:


get_ipython().run_line_magic('sql', 'select distinct MISSION_OUTCOME, count(*) from SPACEXTABLE group by MISSION_OUTCOME')


# In[50]:


get_ipython().run_line_magic('sql', 'select BOOSTER_VERSION from SPACEXTABLE where "PAYLOAD_MASS_KG_" = (select max("PAYLOAD_MASS_KG_") from SPACEXTABLE);')


# In[58]:


get_ipython().run_line_magic('sql', 'SELECT BOOSTER_VERSION, LAUNCH_SITE from SPACEXTABLE WHERE "Landing_Outcome" = \'Failure (drone ship)\' AND substr(Date, 6,2) AND substr(Date,0,5)=\'2015\';')


# In[67]:


get_ipython().run_line_magic('sql', "select LANDING_OUTCOME, count(LANDING_OUTCOME) from SPACEXTABLE where Date between '2010-06-04' and '2017-03-20'group by LANDING_OUTCOME;")


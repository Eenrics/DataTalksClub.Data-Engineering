#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


df = pd.read_csv('data/yellow_tripdata_2021-01.csv', nrows=100)


# In[4]:


df.head(5)


# In[5]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[6]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))


# In[7]:


from sqlalchemy import create_engine


# In[8]:


engine = create_engine('postgresql://airflow:airflow@localhost:5432/airflow')


# In[9]:


engine.connect()


# In[10]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[12]:


df_iter = pd.read_csv('data/yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)


# In[14]:


df_iter


# In[15]:


df = next(df_iter)
df.head()


# In[16]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[17]:


df.head(n=0)


# In[18]:


df.head(n=0).to_sql(name='taxi_yellow_data', con=engine, if_exists='replace')


# In[19]:


get_ipython().run_line_magic('time', "df.to_sql(name='taxi_yellow_data', con=engine, if_exists='append')")


# In[23]:


from time import time
while True:
    t_start = time()
    
    df = next(df_iter)
    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name='taxi_yellow_data', con=engine, if_exists='append')

    t_end = time()
    print(f'another chunk inserted... took {t_end - t_start} seconds.')


# In[ ]:





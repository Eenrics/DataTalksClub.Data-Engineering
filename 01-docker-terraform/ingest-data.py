#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time

df = pd.read_csv('data/yellow_tripdata_2021-01.csv', nrows=100)
df.head(5)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

engine = create_engine('postgresql://airflow:airflow@localhost:5432/airflow')
engine.connect()

df_iter = pd.read_csv('data/yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

df = next(df_iter)
df.head()

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.head(n=0).to_sql(name='taxi_yellow_data', con=engine, if_exists='replace')


get_ipython().run_line_magic('time', "df.to_sql(name='taxi_yellow_data', con=engine, if_exists='append')")

while True:
    t_start = time()
    
    df = next(df_iter)
    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name='taxi_yellow_data', con=engine, if_exists='append')

    t_end = time()
    print(f'another chunk inserted... took {t_end - t_start} seconds.')

print('done!')
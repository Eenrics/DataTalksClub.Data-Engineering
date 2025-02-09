```sql
CREATE OR REPLACE EXTERNAL TABLE `taxi_rides_ny.hw3_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://eenrics_zoomcamp_hw3_2025/trip-data/yellow_tripdata_2024-*.parquet']
);

SELECT count(*) FROM `taxi_rides_ny.hw3_tripdata`;

```

--

```md
20332093
```

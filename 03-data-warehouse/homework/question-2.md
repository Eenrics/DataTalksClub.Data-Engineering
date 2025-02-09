```sql
CREATE OR REPLACE EXTERNAL TABLE `taxi_rides_ny.hw3_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://eenrics2_zoomcamp_hw3_2025/trip-data/yellow_tripdata_2024-*.parquet']
);

SELECT count(*) FROM `taxi_rides_ny.hw3_tripdata`;

-- Scanning 0 MB of Data
SELECT COUNT(DISTINCT(PULocationID)) FROM `taxi_rides_ny.hw3_tripdata`;

CREATE OR REPLACE TABLE `taxi_rides_ny.hw3_nonpartitioned_tripdata`
AS SELECT * FROM `taxi_rides_ny.hw3_tripdata`;

-- Scanning 155.12 MB of Data
SELECT COUNT(DISTINCT(PULocationID)) FROM `taxi_rides_ny.hw3_nonpartitioned_tripdata`;
```

--

```md
0 MB for the External Table and 155.12 MB for the Materialized Table
```

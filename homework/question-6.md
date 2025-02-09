```sql
CREATE OR REPLACE TABLE `taxi_rides_ny.hw3_partitioned_tripdata`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS (
  SELECT * FROM `taxi_rides_ny.hw3_tripdata`
);

-- Scanning 310.24 MB of Data
SELECT COUNT(DISTINCT(VendorID)) FROM  `taxi_rides_ny.hw3_nonpartitioned_tripdata`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Scanning 26.84 MB of Data
SELECT COUNT(DISTINCT(VendorID)) FROM  `taxi_rides_ny.hw3_partitioned_tripdata`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```

---

```md
310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
```

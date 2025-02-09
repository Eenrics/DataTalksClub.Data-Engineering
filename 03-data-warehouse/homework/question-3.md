```sql
-- Scanning 155.12 MB of Data
SELECT PULocationID FROM `taxi_rides_ny.hw3_nonpartitioned_tripdata`;

-- Scanning 310.24 MB of Data
SELECT PULocationID, DOLocationID FROM `taxi_rides_ny.hw3_nonpartitioned_tripdata`;
```

---

```md
A. BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.
```

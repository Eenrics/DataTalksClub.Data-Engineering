## Question 5. Three biggest pickup zones

Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18?

Consider only lpep_pickup_datetime when filtering by date.

- East Harlem North, East Harlem South, Morningside Heights
- East Harlem North, Morningside Heights
- Morningside Heights, Astoria Park, East Harlem South
- Bedford, East Harlem North, Astoria Park

## Answer

```sql
SELECT
    t."PULocationID",
    z."Borough",
    z."Zone",
    z.service_zone,
    SUM(t.total_amount) AS total_amount
FROM greentrip_data AS t
JOIN taxizone_data AS z
    ON t."PULocationID" = z."LocationID"
WHERE
    DATE(t.lpep_pickup_datetime) = '2019-10-18'
GROUP BY t."PULocationID", z."Borough", z."Zone", z.service_zone
HAVING SUM(t.total_amount) > 13000
ORDER BY total_amount DESC;
```

> East Harlem North, East Harlem South, Morningside Heights

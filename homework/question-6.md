## Question 6. Largest tip

For the passengers picked up in October 2019 in the zone named "East Harlem North" which was the drop off zone that had the largest tip?

Note: it's tip , not trip

We need the name of the zone, not the ID.

- Yorkville West
- JFK Airport
- East Harlem North
- East Harlem South

## Answer

```sql
SELECT
    z2."Zone" AS dropoff_zone,
    MAX(t.tip_amount) AS largest_tip
FROM greentrip_data AS t
JOIN taxizone_data AS z1
    ON t."PULocationID" = z1."LocationID"
JOIN taxizone_data AS z2
    ON t."DOLocationID" = z2."LocationID"
WHERE
    z1."Zone" = 'East Harlem North'
    AND t.lpep_pickup_datetime >= '2019-10-01'
    AND t.lpep_pickup_datetime < '2019-11-01'
GROUP BY z2."Zone"
ORDER BY largest_tip DESC
LIMIT 1;
```

> JFK Airport

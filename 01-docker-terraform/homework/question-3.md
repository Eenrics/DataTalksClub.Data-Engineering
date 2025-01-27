## Question 3. Trip Segmentation Count

During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:

1. Up to 1 mile
2. In between 1 (exclusive) and 3 miles (inclusive),
3. In between 3 (exclusive) and 7 miles (inclusive),
4. In between 7 (exclusive) and 10 miles (inclusive),
5. Over 10 miles

Choose the closest answer.

- 104,802; 197,670; 110,612; 27,831; 35,281
- 104,802; 198,924; 109,603; 27,678; 35,189
- 104,793; 201,407; 110,612; 27,831; 35,281
- 104,793; 202,661; 109,603; 27,678; 35,189
- 104,838; 199,013; 109,645; 27,688; 35,202

## Answer

Also see question-3.ipynb

```sql
SELECT
    COUNT(*) FILTER (WHERE trip_distance <= 1) AS up_to_1_mile,
    COUNT(*) FILTER (WHERE trip_distance > 1 AND trip_distance <= 3) AS between_1_and_3_miles,
    COUNT(*) FILTER (WHERE trip_distance > 3 AND trip_distance <= 7) AS between_3_and_7_miles,
    COUNT(*) FILTER (WHERE trip_distance > 7 AND trip_distance <= 10) AS between_7_and_10_miles,
    COUNT(*) FILTER (WHERE trip_distance > 10) AS over_10_miles
FROM greentrip_data
WHERE
    lpep_pickup_datetime >= '2019-10-01'
    AND lpep_pickup_datetime < '2019-11-01';

```

> 104,802; 198,924; 109,603; 27,678; 35,189

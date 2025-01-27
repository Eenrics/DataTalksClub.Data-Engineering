## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance.

- 2019-10-11
- 2019-10-24
- 2019-10-26
- 2019-10-31

## Answer

```sql
SELECT DATE(lpep_pickup_datetime), trip_distance as longest_distance FROM greentrip_data ORDER BY trip_distance DESC LIMIT 1;

```

> "2019-10-31" 515.89

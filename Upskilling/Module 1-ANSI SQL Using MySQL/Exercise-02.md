# Exercise 2 - Top Rated Events

## Aim

Identify events with the highest average rating, considering only those that have received at
least 10 feedback submissions.

---

## SQL Query

```sql
SELECT e.event_id, e.title, ratings.avg_rating FROM 
(SELECT event_id, COUNT(rating) AS count_rating, AVG(rating) AS avg_rating 
FROM feedback GROUP BY event_id) AS ratings
JOIN events e ON ratings.event_id=e.event_id 
WHERE ratings.count_rating>=10
ORDER BY ratings.avg_rating DESC
LIMIT 1;
```

---

## Output

<img width="718" height="97" alt="image" src="https://github.com/user-attachments/assets/8901d407-bdc2-4c8e-8254-dc1dd52658cb" />

# Exercise 19 - Completed Events with Feedback Summary

## Aim

For completed events, show total registrations and average feedback rating.

---

## SQL Query

```sql
SELECT event_id, COUNT(user_id),
(SELECT AVG(rating) FROM feedback f WHERE r.event_id=f.event_id) AS avg_Rating
FROM registrations r
GROUP BY r.event_id;
```

---

## Output

<img width="633" height="131" alt="image" src="https://github.com/user-attachments/assets/68ef2e33-ec29-4b61-8a9a-b02a9c6c1006" />

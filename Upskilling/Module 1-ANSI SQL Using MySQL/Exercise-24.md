# Exercise 24 - Average Session Duration per Event

## Aim

Compute the average duration (in minutes) of sessions in each event.

---

## SQL Query

```sql
SELECT e.event_id, e.title,
AVG(TIMESTAMPDIFF(MINUTE, s.start_time, s.end_time)) AS avg_duration_minutes
FROM events e
JOIN sessions s ON e.event_id = s.event_id
GROUP BY e.event_id, e.title;
```

---

## Output

<img width="621" height="148" alt="image" src="https://github.com/user-attachments/assets/9054b515-524c-4f04-bf3f-e6caa22ce956" />

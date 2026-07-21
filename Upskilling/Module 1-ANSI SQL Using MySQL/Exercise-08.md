# Exercise 8 - Sessions per Upcoming Event

## Aim

Display all upcoming events with the count of sessions scheduled for them.
---

## SQL Query

```sql
SELECT e.title, COUNT(session_id) AS session_count
FROM events e
JOIN sessions s ON e.event_id=s.event_id 
WHERE e.status='upcoming'
GROUP BY e.event_id, e.title;
```

---

## Output

<img width="633" height="117" alt="image" src="https://github.com/user-attachments/assets/3b9be156-5658-42a7-9696-cbe8db08b9ac" />

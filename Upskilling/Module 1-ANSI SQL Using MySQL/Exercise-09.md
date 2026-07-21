# Exercise 9 - Organizer Event Summary

## Aim

For each event organizer, show the number of events created and their current status
(upcoming, completed, cancelled).
---

## SQL Query

```sql
SELECT organizer_id, COUNT(event_id), status
FROM events
GROUP BY organizer_id, status;
```

---

## Output

<img width="643" height="132" alt="image" src="https://github.com/user-attachments/assets/e02e4e6f-35bb-4241-89bf-e1f4f2688f0c" />


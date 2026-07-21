# Exercise 25 - Events Without Sessions

## Aim

List all events that currently have no sessions scheduled under them.

---

## SQL Query

```sql
SELECT e.event_id, e.title
FROM events e
LEFT JOIN sessions s
    ON e.event_id = s.event_id
WHERE s.session_id IS NULL;
```

---

## Output

<img width="648" height="121" alt="image" src="https://github.com/user-attachments/assets/11ec15b1-4222-4587-995d-2182d9797c1f" />

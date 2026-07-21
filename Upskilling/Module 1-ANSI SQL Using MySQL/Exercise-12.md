# Exercise 12 - Event with Maximum Sessions

## Aim

List the event(s) with the highest number of sessions.

---

## SQL Query

```sql
SELECT event_id, COUNT(session_id)
FROM sessions
GROUP BY event_id
ORDER BY COUNT(session_id)
DESC LIMIT 1;
```

---

## Output

<img width="705" height="91" alt="image" src="https://github.com/user-attachments/assets/2f421bae-0faf-4459-b378-947bfd807c84" />

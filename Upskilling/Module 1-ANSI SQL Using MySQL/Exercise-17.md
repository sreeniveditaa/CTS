# Exercise 17 - Multi-Session Speakers

## Aim

Identify speakers who are handling more than one session across all events.

---

## SQL Query

```sql
SELECT speaker_name
FROM sessions
GROUP BY speaker_name
HAVING COUNT(session_id)>1;
```

---

## Output

<img width="636" height="127" alt="image" src="https://github.com/user-attachments/assets/0d973d63-9a33-474a-90f4-52269bff7498" />

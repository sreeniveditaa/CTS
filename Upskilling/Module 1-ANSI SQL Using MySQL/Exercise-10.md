# Exercise 10 - Feedback Gap

## Aim

Identify events that had registrations but received no feedback at all
---

## SQL Query

```sql
SELECT event_id, title
FROM events 
WHERE event_id IN (SELECT event_id FROM registrations) 
AND event_id NOT IN (SELECT event_id FROM feedback);
```

---

## Output

<img width="671" height="133" alt="image" src="https://github.com/user-attachments/assets/9da601d4-0042-419b-8590-a26d0fd7acb0" />

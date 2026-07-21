# Exercise 18 - Resource Availability Check

## Aim

List all events that do not have any resources uploaded.

---

## SQL Query

```sql
SELECT title
FROM events
WHERE event_id
NOT IN (SELECT event_id FROM resources);
```

---

## Output

<img width="617" height="93" alt="image" src="https://github.com/user-attachments/assets/0079718a-e599-4108-91b1-004d1bcb8843" />

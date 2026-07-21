# Exercise 22 - Duplicate Registrations Check

## Aim

Detect if a user has been registered more than once for the same event.

---

## SQL Query

```sql
SELECT user_id, event_id,
COUNT(*) AS registration_count
FROM registrations
GROUP BY user_id, event_id
HAVING COUNT(*) > 1;
```

---

## Output

<img width="635" height="120" alt="image" src="https://github.com/user-attachments/assets/212f4d8b-c351-49cb-8b37-9dc34dab3348" />

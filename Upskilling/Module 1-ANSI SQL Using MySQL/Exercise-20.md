# Exercise 20 - User Engagement Index

## Aim

For each user, calculate how many events they attended and how many feedbacks they submitted.

---

## SQL Query

```sql
SELECT u.user_id, u.full_name,
COUNT(DISTINCT r.event_id) AS events_attended,
COUNT(DISTINCT f.feedback_id) AS feedbacks_submitted
FROM users u
LEFT JOIN registrations r
ON u.user_id = r.user_id
LEFT JOIN feedback f
ON u.user_id = f.user_id
GROUP BY u.user_id, u.full_name
ORDER BY u.user_id;
```

---

## Output

<img width="622" height="197" alt="image" src="https://github.com/user-attachments/assets/0a8f6e8c-6133-4169-95f8-c3982a881f6c" />

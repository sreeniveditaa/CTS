# Exercise 21 - Top Feedback Providers

## Aim

List top 5 users who have submitted the most feedback entries.

---

## SQL Query

```sql
SELECT u.user_id, u.full_name,
COUNT(f.feedback_id) AS feedback_count
FROM users u
JOIN feedback f ON u.user_id = f.user_id
GROUP BY u.user_id, u.full_name
ORDER BY feedback_count
DESC LIMIT 5;
```

---

## Output

<img width="705" height="158" alt="image" src="https://github.com/user-attachments/assets/13de9476-c298-439b-8e08-ad863bb54c79" />

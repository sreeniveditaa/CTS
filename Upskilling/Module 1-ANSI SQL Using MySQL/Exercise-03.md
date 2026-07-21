# Exercise 3 - Inactive Users

## Aim

Retrieve users who have not registered for any events in the last 90 days

---

## SQL Query

```sql
SELECT u.user_id, u.full_name
FROM users u
WHERE u.user_id NOT IN (
SELECT user_id
FROM registrations
WHERE registration_date >= DATE_SUB(CURDATE(), INTERVAL 90 DAY));
```

---

## Output

<img width="687" height="112" alt="image" src="https://github.com/user-attachments/assets/a594f211-5766-4396-a4c4-95a8c5fc8253" />

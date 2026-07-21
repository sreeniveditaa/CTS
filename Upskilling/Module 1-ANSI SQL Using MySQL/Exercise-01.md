# Exercise 1 - User Upcoming Events

## Aim

Show a list of all upcoming events a user is registered for in their city, sorted by date.

---

## SQL Query

```sql
SELECT u.user_id, u.full_name, e.title, e.start_date
FROM users u
JOIN registrations r ON u.user_id = r.user_id
JOIN events e ON r.event_id = e.event_id
WHERE u.city = e.city
AND e.status = 'upcoming'
ORDER BY e.start_date;
```

---

## Output

<img width="620" height="156" alt="image" src="https://github.com/user-attachments/assets/b8eef4b1-5d19-4799-b32c-86685e4be9f8" />

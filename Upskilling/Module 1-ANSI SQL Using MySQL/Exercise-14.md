# Exercise 14 - Most Registered Events

## Aim

List top 3 events based on the total number of user registrations.

---

## SQL Query

```sql
SELECT r.event_id, e.title, COUNT(r.user_id) as user_count FROM registrations r 
JOIN events e ON e.event_id=r.event_id 
GROUP BY event_id 
ORDER BY user_count DESC 
LIMIT 3;
```

---

## Output

<img width="706" height="126" alt="image" src="https://github.com/user-attachments/assets/8f3a4be6-9012-4113-b37d-d1937a52a439" />

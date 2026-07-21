# Exercise 5 - Most Active Citie

## Aim

List the top 5 cities with the highest number of distinct user registrations.

---

## SQL Query

```sql
SELECT u.city, COUNT(DISTINCT u.user_id) AS distinct_users
FROM users u
JOIN registrations r ON u.user_id = r.user_id
GROUP BY u.city
ORDER BY distinct_users DESC
LIMIT 5;
```

---

## Output

<img width="612" height="132" alt="image" src="https://github.com/user-attachments/assets/4642f782-fc2f-465f-a98e-be91a2c94cfa" />

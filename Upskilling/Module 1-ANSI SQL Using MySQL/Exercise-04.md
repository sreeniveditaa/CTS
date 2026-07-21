# Exercise 4 - Peak Session Hours

## Aim

Count how many sessions are scheduled between 10 AM to 12 PM for each event.

---

## SQL Query

```sql
SELECT title, COUNT(*) AS count
FROM sessions 
WHERE TIME(start_time) BETWEEN '10:00:00' AND '12:00:00'
GROUP BY title;
```

---

## Output

<img width="651" height="147" alt="image" src="https://github.com/user-attachments/assets/e7ce4cd9-d7e9-4f1b-807e-b35c8922d647" />

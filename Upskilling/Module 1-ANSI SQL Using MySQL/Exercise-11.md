# Exercise 11 - Daily New User Count

## Aim

Find the number of users who registered each day in the last 7 days.

---

## SQL Query

```sql
SELECT registration_date, count(user_id) as user_count
FROM registrations 
WHERE DATEDIFF(CURDATE(),registration_date)<=7 
GROUP BY registration_date;
```

---

## Output

<img width="630" height="87" alt="image" src="https://github.com/user-attachments/assets/975c1188-a9e9-437f-97ac-6ee47e382c0b" />

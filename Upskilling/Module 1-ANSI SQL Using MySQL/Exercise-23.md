# Exercise 23 - Registration Trends

## Aim

Show a month-wise registration count trend over the past 12 months.

---

## SQL Query

```sql
SELECT
YEAR(registration_date) AS year,
MONTH(registration_date) AS month,
COUNT(*) AS registration_count
FROM registrations
WHERE registration_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
GROUP BY YEAR(registration_date), MONTH(registration_date)
ORDER BY YEAR(registration_date), MONTH(registration_date);
```

---

## Output

<img width="611" height="121" alt="image" src="https://github.com/user-attachments/assets/e825b38a-9db0-490e-8a73-908723d7bc7d" />

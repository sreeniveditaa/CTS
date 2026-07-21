# Exercise 7 - Low Feedback Alerts

## Aim

List all users who gave feedback with a rating less than 3, along with their comments and
associated event names.

---

## SQL Query

```sql
SELECT f.user_id, f.comments, e.title
FROM feedback f 
JOIN events e ON e.event_id=f.event_id
WHERE f.rating<=3;
```

---

## Output

<img width="633" height="81" alt="image" src="https://github.com/user-attachments/assets/57072fb0-a1ed-409d-aae7-9e69c67d8816" />

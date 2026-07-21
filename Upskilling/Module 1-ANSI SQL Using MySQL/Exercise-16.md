# Exercise 16 - Unregistered Active Users

## Aim

Find users who created an account in the last 30 days but haven’t registered for any events.

---

## SQL Query

```sql
SELECT full_name FROM users
WHERE DATEDIFF(CURDATE(),registration_date)<=30 
AND user_id NOT IN (SELECT user_id FROM registrations);
```

---

## Output

<img width="608" height="87" alt="image" src="https://github.com/user-attachments/assets/5702ec36-231c-495f-80f9-a6dbcc5db927" />

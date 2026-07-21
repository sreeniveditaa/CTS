# Exercise 13 - Average Rating per City

## Aim

Calculate the average feedback rating of events conducted in each city.

---

## SQL Query

```sql
SELECT e.city, AVG(f.rating)
FROM events e
JOIN feedback f
ON e.event_id = f.event_id
GROUP BY e.city;
```

---

## Output

<img width="627" height="113" alt="image" src="https://github.com/user-attachments/assets/bcf54037-4dba-4466-9ece-0fa781adaa94" />

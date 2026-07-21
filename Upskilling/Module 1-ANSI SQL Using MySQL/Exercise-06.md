# Exercise 6 - Event Resource Summary

## Aim

Generate a report showing the number of resources (PDFs, images, links) uploaded for each
event.
---

## SQL Query

```sql
SELECT event_id, 
SUM(CASE WHEN resource_type='pdf' THEN 1 ELSE 0 END) AS pdf_count,
SUM(CASE WHEN resource_type='image' THEN 1 ELSE 0 END) AS images_count,
SUM(CASE WHEN resource_type='link' THEN 1 ELSE 0 END) AS link_count
FROM resources GROUP BY event_id;
```

---

## Output

<img width="647" height="127" alt="image" src="https://github.com/user-attachments/assets/3bd7c2db-b9ae-4fff-be1c-462edeeb3d0b" />

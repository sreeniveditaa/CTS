# Exercise 15 - Event Session Time Conflict

## Aim

Identify overlapping sessions within the same event (i.e., session start and end times that conflict).

---

## SQL Query

```sql
SELECT s1.event_id, 
s1.title AS session_1, s2.title AS session_2,
s1.start_time, s1.end_time,
s2.start_time, s2.end_time
FROM sessions s1
JOIN sessions s2
ON s1.event_id = s2.event_id
AND s1.session_id < s2.session_id
AND s1.start_time < s2.end_time
AND s1.end_time > s2.start_time;
```

---

## Output

<img width="1002" height="115" alt="image" src="https://github.com/user-attachments/assets/3287d373-b04d-49a6-991d-7ae51e603ebc" />

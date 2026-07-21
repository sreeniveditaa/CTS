# Exercise 53 - Task Scheduler

## Objective

Use classes, the `datetime` module, lists, and sorting to manage tasks.

## Task

Create a task scheduler that prioritizes tasks by due date and identifies overdue tasks.

## Instructions

- Create a `Task` class with `due_date` and `priority`.
- Store tasks in a list.
- Sort tasks by due date using the `datetime` module.
- Filter overdue tasks.
- Print the sorted task schedule.

## Project Structure

- `Exercise_53.py` - Python source code
- `53_output.png` - Program output screenshot

## Code

```python
from datetime import datetime


class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return (
            f"{self.name} | Due: {self.due_date.strftime('%Y-%m-%d')} "
            f"| Priority: {self.priority}"
        )


tasks = [
    Task("Submit Assignment", "2026-07-05", "High"),
    Task("Project Review", "2026-06-28", "Medium"),
    Task("Pay Electricity Bill", "2026-06-20", "High"),
    Task("Buy Groceries", "2026-07-01", "Low")
]

tasks.sort(key=lambda task: task.due_date)

today = datetime.now()

overdue_tasks = [task for task in tasks if task.due_date < today]

print("Task Schedule")

for task in tasks:
    print(task)

print("\nOverdue Tasks")

if overdue_tasks:
    for task in overdue_tasks:
        print(task)
else:
    print("No overdue tasks.")
```

## Expected Output

```
Task Schedule
Pay Electricity Bill | Due: 2026-06-20 | Priority: High
Project Review | Due: 2026-06-28 | Priority: Medium
Buy Groceries | Due: 2026-07-01 | Priority: Low
Submit Assignment | Due: 2026-07-05 | Priority: High

Overdue Tasks
Pay Electricity Bill | Due: 2026-06-20 | Priority: High
```

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
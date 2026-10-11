salary = float(input())
late_days = int(input())
absent_days = int(input())

if late_days > 10:
    salary *= 0.90
elif late_days > 5:
    salary *= 0.95

if absent_days > 2:
    salary *= 0.95

print(round(salary, 2))
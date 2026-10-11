marks = list(map(int, input().split()))

if any(mark < 35 for mark in marks):
    print("FAIL")
elif sum(marks) / 5 >= 75:
    print("DISTINCTION")
else:
    print("PASS")

num = int(input())

while num >= 10:
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    num = total

print(num)

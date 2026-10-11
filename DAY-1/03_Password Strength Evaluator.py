password = input()
digit = False
upper = False

for ch in password:
    if ch.isdigit():
        digit = True
    if ch.isupper():
        upper = True

if digit and upper and len(password) >= 8:
    print("STRONG")
else:
    print("WEAK")
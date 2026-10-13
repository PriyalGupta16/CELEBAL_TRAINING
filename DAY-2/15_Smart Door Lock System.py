PIN = int(input("Enter PIN: "))

for i in range(3):
    attempt = int(input())

    if attempt == PIN :
     print("ACCESS GRANTED!")
     break
    else:
        print("ACCESS DENIED")
else:
     print("LOCKED")


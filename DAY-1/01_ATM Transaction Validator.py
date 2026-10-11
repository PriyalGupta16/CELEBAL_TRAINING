initial_balance = int(input())
n = int(input())

balance = initial_balance 

for i in range(n):
    amount = int(input())


    if (balance % 100 == 0 and balance >= amount):
     balance -= amount

    print("Success")

else: 
    print("Fail")

    print(balance)
                      
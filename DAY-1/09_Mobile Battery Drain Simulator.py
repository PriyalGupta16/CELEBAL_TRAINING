drain = int(input())

if drain <= 0:
    print(0)
else:
    battery = 100
    minutes = 0

    while battery > 0:
        battery -= drain
        minutes += 1

    print(minutes)
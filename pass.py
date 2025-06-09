n = int(input("Enter a number here:"))

for x in range(n):
    if x%10 == 0:
        pass
    elif x%15 == 0:
        print("big number")
    elif x%4 == 0:
        print("random")
    else:
        print("lwk useless")
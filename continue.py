price = float(input("Enter a price here:"))

while price > 0:
    price = price - 1
    if price == 5:
        print("Your price has reached the $5 minimum.")
        continue
    print("Current price:", price)
print("Thank you!")
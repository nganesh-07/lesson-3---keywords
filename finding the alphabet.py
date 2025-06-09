word = input("Enter any word:")

for i in word:
    if i == "s":
        print("This is an s.")
        break
    else:
        print("Not an s.")
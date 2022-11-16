n = int(input("number"))
for row in range(n):
    for column in range(n):
        if column ==0 or row == (n-1) or row == column:
            print("*", end="")
        else:
            print(end= " ")
    print()

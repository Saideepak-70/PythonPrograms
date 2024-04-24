rows = int(input("Enter number of rows : "))
for i in range(rows):
    print(" ", end="")
    for k in range(rows-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print("")
for i in range(rows-2, -1, -1):
    print(" ", end="")
    for k in range(rows - i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print("")
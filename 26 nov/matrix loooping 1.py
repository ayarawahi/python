s=int(input("enter the size:"))
for i in range(s):
    for j in range(s):
        if (i<=j):
            print (1, end=" ")
        else:
            print(0, end=" ")
    print()
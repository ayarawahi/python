A=int(input("eter the value of A"))
B=int(input("eter the value of B"))
C=int(input("eter the value of C"))

if (A >= B)and (A>= C):
 largest= A
elif(B>=A)and (B>=C):
 largest=B
else:
 largest=C
print ("largest number is :",largest)

sum2=0

for i in range(1,100):
    grade=float(input("enter the grade"))
    sum2+=grade
    x=input("do you wantto stop or continue(y,n)")
    if x=="y":
        avg=sum2/i
        print(avg)
        break
    else:
        continue

  
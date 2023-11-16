hour=int(input("enter the hour"))
minute=int(input("enter the min"))
t=(input("is it am and p"))

hour2=int(input("enter the hour"))
minute2=int(input("enter the min"))
t2=(input("is it am and p"))
       
if(t=="am"and t2=="pm"):
    print(hour,":",minute,t)
elif(t2=="am"and t=="pm"):
    print(hour2,":",minute2,t2)
else:
    if (hour<hour2):
        print(hour,":",minute,t)
        if (hour==hour):
            if (minute<=minute2):
                print (hour,":",minute,t2)
    else:
        print(hour,":",minute,t)
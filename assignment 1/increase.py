tution=10000
icrease=.05
years=10
i=0
current_year=1
while (current_year<=years):
    tution=tution*(1+icrease)
    print("tution in year is "+str(current_year)+":"+"$"+str(tution))
    if current_year<=4:
        i+=tution
    current_year+=1
print("this is total "+str(i))
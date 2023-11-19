#nub=int(input("guess the numb"))
from random import randint
nub=randint(0,30)
while(nub):
    if (nub==19): 
        print("win",nub)
        break
    else:
        if (nub>19):
            print("go down",nub)
            break
        
        else:
            if (nub<19):
             print ("go up",nub)
             break
nub=int(input("guess the numb"))
while(nub):
    if (nub==19): 
        print("WIN")
        break
    else:
        if (nub>19):
            print("go down")
            break
        
        else:
            if (nub<19):
             print ("go up")
             break
balance=1000
PIN=0
while(PIN==PIN):
    PIN=int(input("write PIN"))
    if PIN==1234:
        process=int(input("1.acc balance,2.withdraw,3.depositmoney"))
        if process==1:
            print(balance)
        elif process==2:
            withdraw=int(input("enter ur wihdrww"))
            print(balance-withdraw)
                   
#             print (process)
        elif process==3:
             depositmoney=int(input("enter the amount"))
    
    else:
        print("PIN is not correct",PIN)
  
  
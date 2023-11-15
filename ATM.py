balance=1000
PIN=int(input("write PIN"))
if PIN==1234:
     process=int(input("1.acc balance,2.withdraw,3.depositmoney"))
     if process==1:
          print(balance)
     else:
#         print(process)
        if process==2:
            withdraw=int(input("enter ur wihdrww"))
            print(balance-withdraw)
        else:
#             print (process)
            if process==3:
             depositmoney=int(input("enter the amount"))
            else:
             print("")
else:
 print("PIN is not correct")
            
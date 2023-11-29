class BankAccount:
    def __init__(self,balance,account_number):
        self.__balance=balance
        self.__account_number=account_number
        
    def display(self):
        print(self.__balance)
            
    def deposite(self,des):
        self.__balance+=des
        print(self.__balance)


    def withdraw(self,withd):
        self.__balance-=withd
        print(self.__balance)

            
l1=BankAccount(1000,98765)
l1.deposite(10)
l1.withdraw(-1)

    
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
        try:
            withd = float(withd)
            if withd < 0:
                return("Invalid input")
            if withd > self.__balance :
                return("amount > balance")
            
            self.__balance-=withd
            return("Successfully withdrawen")
            
            
        except Exception as exc:
            return("error: the type is ",exc)
            
l1=BankAccount(1000,98765)
l1.deposite(10)
print(l1.withdraw(-3))
l1.display()

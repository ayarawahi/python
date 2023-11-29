class numbers:
    def __init_(self):
        self.numbers=[]
    def add_number(self,num):
        self.numbers.append(num)
    def sum_num(self):
        summ=0
        for i in self.numbers:
            summ+=i
        return summ
n1=numbers()
n1.add_number(2)
n1.add_number(3)
n1.add_number(9)
print(n1.sum_num())
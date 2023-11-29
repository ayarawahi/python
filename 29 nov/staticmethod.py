class math:
    @staticmethod
    def dd_num(x,y):
        return x+y
    @staticmethod
    def pi():
        return 3.14
class shape:
    def __init__(self,name,color,r):
        self.name=name
        self.color=color
        self.r=r
    def area(self):
        return 2*math.pi()*self.r
sh1=shape("ca","red",4)
print(sh1.area())
    
print(math.dd_num(3,5))
        
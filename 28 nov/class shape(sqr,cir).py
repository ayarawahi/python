
class shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __str__(self):
      return("  this is  the area of {}and the color is {}".format(self.name,self.color,))
    def Area(self):
      print("  this is  the area of shape")
        
class cir(shape):
     def __init__(self,name,color,r):
         super().__init__(name,color)
         self.r=r
     def Area(self):
         area=(3.14*(self.r**2))
         return area
     def __str__(self):
      return("  this is  the area of {}and the color is {}".format(self.name,self.color))
     
    

class sqr(shape):
     def _init_(self,name,color,l):
         super().__init__(name,color)
         self.l=l
     def Area(self):
         area=self.l**2
         return area
     def __str__(self):
      return("  this is  the area of {}and the color is {}".format(self.name,self.color))
     

p1=shape("a","pink")
c1=cir("cir","black",4)

print(p1)
print(c1)



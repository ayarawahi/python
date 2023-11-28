class person:
    def __init__(self,name,age=78):
        self.name=name
        self.age=age
      
    def say_hi(self):
        print("hi {} from parent class".format(self.name))
class stu(person):
    def _init(self,name,age=78):
        super().__init__()
    def say_hi(self):
        print("hi {} from studet class".format(self.name))
p1=person("a",22)
s1=stu("b",22)
s1.say_hi()
p1.say_hi()
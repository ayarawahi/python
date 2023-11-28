class person:
    num_of_ob=0
    def __init__(self,name,age=78):
        self.name=name
        self.age=age
        person.num_of_ob+=1
    def __str__(self):
        return"he how {} yor are{} year sols".format(self.name,self.age)
    def talk(self):
        return"{}  is talking ".format(self.name)
per1=person("ahmed",24)
per2=person("hmed")
print(per1.talk())
print(per2.__str__())

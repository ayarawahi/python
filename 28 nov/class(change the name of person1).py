class person:
    num_of_ob=0
    def __init__(self,name,age=78):
        self.__name=name
        self.__age=age
        person.num_of_ob+=1
    def set_name(self,new_name):
        self.__name=new_name
        
    def __str__(self):
        return"he how {} yor are{} year sols".format(self.__name,self.__age)
    def talk(self):
        return"{}  is talking ".format(self.__name)
per1=person("ahmed",24)
per2=person("hmed")
print(per1.talk())
print(per2.__str__())
per1.set_name("ay")
print(per1)
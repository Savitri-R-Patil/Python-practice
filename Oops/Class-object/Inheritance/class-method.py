class person:
    name="anonymous"
    
    #def changename(self,name):
    #   self.__class__.name="Rahul"
    
    
    @classmethod #decorator
    def changename(cls,name):
        cls.name=name
        
        
m1=person()
print(person.name)
m1.changename("savitri")
print(m1.name)
print(person.name)

        
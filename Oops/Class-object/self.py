class Student:
    #default constructor
    def __init__(self):
      pass
    
    #paramitorized constructor
    def __init__(self,fullname):
        self.name=fullname
        print("added new student :")
        
        
s1=Student("karan")
print(s1.name) #karan

        
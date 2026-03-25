class car:
    #@staticmethod
    def start(self):
        print(self.name ,"car started : ")
     
     
    @staticmethod   
    def stop():
        print("car stopped : ")
        
class Toyotacar(car):
    def __init__(self,name):
        self.name=name
car1=Toyotacar("prius")
print(car1.start())
        
        
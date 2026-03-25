class car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("car stopped")
        
    @staticmethod
    def stop():
        print("car started ")
        
class Toyotacar(car):
    def __init__(self,name, type):
        self.name=name
        super().__init__(type)
        
car1= Toyotacar("prius", "electric")
print(car1.type)
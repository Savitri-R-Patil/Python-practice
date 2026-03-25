class car:
    
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("acr stopped ")
        
    
class Toyotacar(car):
    def __init__(self,brand):
        self.brand=brand
        
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
        
car1=Fortuner("diesel")
car1.start()
        
        

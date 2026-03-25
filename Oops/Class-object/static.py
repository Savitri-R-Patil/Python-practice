class student:
    def __init__(self,rollNo):
        self.Rollno=rollNo
     
    @staticmethod   
    def Hello():
        print("Hello ")
    
    def welcome(self):
        print("Welcome")
        
        
c1=student(89)
c1.Hello()
c1.welcome()      
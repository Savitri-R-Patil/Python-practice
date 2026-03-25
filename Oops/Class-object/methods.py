class student:
    collge_name="ABC College"
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    def welcome(self):
        print("hi welcome to .....")
        
s1=student("geeta",78)
s1.welcome()
class Employee:
    def __init__(self, Role, Dept, Salary):
        self.role=Role
        self.dept=Dept
        self.salary=Salary
    def showDetails(self):
        print("Employee Details :")
        print(self.role)
        print(self.dept)
        print(self.salary)
        
class Engineer(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age 
        super().__init__("Engineer", "c2", "rs.90,000")
        
    
        
Emp=Engineer("Savitri", 22)
Emp.showDetails()
        
class student:
    def __init__(self,phy,chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
        #self.percentage=str((self.phy+ self.chem+ self.math)/3)  + "%"
        
        #def cal_percentage(self):
        #    self.percentage=str((self.phy+ self.chem+ self.math)/3)  + "%"
        
    @property
    def percentage(self):
        return str((self.phy+self.chem +self.math)/3) + "%"

            
    
        
s1=student(98,80,90)
print(s1.percentage)

s1.phy=100
print(s1.phy)
print(s1.percentage)


     
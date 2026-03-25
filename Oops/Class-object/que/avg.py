class student:
    
    def __init__(self,name, phy,chem,maths):
        self.name=name
        self.phy_marks=phy
        self.chem_marks=chem
        self.maths_marks=maths
    
    #we have to self as parameter    
    def avg(self):
        total=self.phy_marks+self.chem_marks +self.maths_marks
        avg=(total)//3
        print("The avg marks obtained is : " ,avg)

s1=student("Teju",97,94,98)

s1.avg()
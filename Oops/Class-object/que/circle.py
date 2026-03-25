class circle:
    def __init__(self, r):
        
        self.R=r
        
    def Area(self):
        self.area = 3.142*(self.R)**2
        print(self.area)
        
    def Per(self):
        self.perimeter=2*3.142*(self.R)
        print(self.perimeter)


c1=circle(10)

c1.Area()
c1.Per()
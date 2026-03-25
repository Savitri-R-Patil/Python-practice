class Account:
    def __init__(self,bal,accnt):
        self.Balance=bal
        self.account=accnt
        
    def debit(self,amnt):
        self.Balance-=amnt
        print("Rs." ,amnt ," is Debited")
        print("Toatal balance :" ,self.getbal())
        if(amnt>self.Balance):
            print("Insufficient balance ")
        
        
    def credit(self,amnt):
        self.Balance+=amnt
        print("Rs." ,amnt,  " is credited")
        print("Toatal balance :" ,self.getbal())
        
    def getbal(self):
         #print("Total bal: ", self.Balance)  #if we do this then this total balance prints before printing " DEbited " or "credit"
         return self.Balance
A1=Account(24000,12345)
A1.debit(2000)
A1.credit(21000)
        
    
        
        
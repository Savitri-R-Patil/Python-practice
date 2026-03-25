class Account:
    def __init__(self,acc_no,acc_passrd):
        self.acc_no=acc_no
        self.__acc_pass=acc_passrd   #.__=means private : cant access from outside the class 
        
    def reset_passrd(self):
        print(self.__acc_pass)
        
acc1 = Account("1234", "abcd")
print(acc1.acc_no)
acc1.reset_passrd()
print(acc1.__acc_pass)
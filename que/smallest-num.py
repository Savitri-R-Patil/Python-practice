
n=int(input("enter how many numbers you want to enter :"))
list=[0]*n                                     # here if you use -> list=[]*n  then it gives output as [] empty so 
for i in range(n):
    list[i]=int(input())
    

small=list[0]                     #initialize small -> list[0] because if i do small =0 then it checks for 0> all numbers so 0 is the lowest number itself so it will never change 
for i in range(n):
    
    if(small>list[i]):
        small=list[i]
print(small)
    
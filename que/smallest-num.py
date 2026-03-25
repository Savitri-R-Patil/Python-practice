
n=int(input("enter how many numbers you want to enter :"))
list=[0]*n                                     # here if you use -> list=[]*n  then it gives output as [] empty so 
for i in range(n):
    list[i]=int(input())
    

small=list[0]
for i in range(n):
    
    if(small>list[i]):
        small=list[i]
print(small)
    
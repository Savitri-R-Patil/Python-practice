n=int(input("enter a size of list"));

list=[0]*n
for i in range(n):
    list[i]=int(input())

large=0                         # for only to print largest number we initialize large = 0 otherwise for finding smallest
                                 #  number we initialize (smallest as =first element of list) beacuse go to smallest.py file

for i in range(n):
    if(large<list[i]):
        large=list[i]
        
print(large)
x= int(input("enter a number to search :"))
list=[1,2,4,5,6,7]
i=0
while i<len(list):

    if(x==list[i]):
        print("found")
        break
    i+=1
    
else:
        print("not found")   
    
  
 
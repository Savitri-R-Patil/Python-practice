x=int(input("enter  a num :"))
list=[1,3,5,7,8]

for i in range(len(list)):
    if(x==list[i]):
        print("found")
        break
    
else:
    print("not found ")
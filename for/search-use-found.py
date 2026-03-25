x=int(input())
found =False
arr =(21,31,41,51)         #tuple
for i in range(len(arr)):
    if(x==arr[i]):
        found=True
        print("found")
        break        
if(found==False):
    print("not found")

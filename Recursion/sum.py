def sum(n):
    if(n==0):                       # if(  n==1):
        return 0                    # return 1
    return sum(n-1)+n               

Total=sum(5)
print(Total)
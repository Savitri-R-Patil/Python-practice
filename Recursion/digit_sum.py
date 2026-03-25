def digit_sum(n):
    sum=0
    if (n==0):
        return 0
    N=n%10
    n=n//10
    
    Total= digit_sum(n)+N 

    return Total 

print(digit_sum(3421))

    
    
    
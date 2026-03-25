def digit_count(n):
    
    if n==0:
        return 0
    
    if n != 0:
        n=n//10
        count=1 + digit_count(n)
        
    return count    
    
print(digit_count(124567))
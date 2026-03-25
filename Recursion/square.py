def a_power_b(a,b):
    if(b==0):
        return 1
    return a*a_power_b(a,b-1)
    
    
print(a_power_b(2,5))
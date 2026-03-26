def greet(n):
    if(n==0):
        return
    print("Hello world")
    
    return greet(n-1)

greet(5)
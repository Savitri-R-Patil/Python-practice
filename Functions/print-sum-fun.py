#storing a function result by assigning a function call to a var 'result '
def sum(a, b):
    s=a+b
    print(s)
    
result=sum(2,3) # sum prints 5 but there is no return statement so function returns None and this becomes #5
                                                                                                #result=None
print(result)     
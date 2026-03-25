class A:
    varA="welcome to claass A"
    
class B:
    varB="welcome ro class B"
    
class c(A,B):
    varc="welcome to class c"
    
c1=c()
print(c1.varc)
print(c1.varB)
print(c1.varA)
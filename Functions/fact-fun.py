def fact(N):
    fact=1
    for i in range(1,N+1):
     fact*=i 
    print(fact)

n=int(input("factorial of :"))
fact(n)
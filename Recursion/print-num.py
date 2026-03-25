def print_n(n):
    if(n==0):
        return 
    print(n)
    return print_n(n-1)

print_n(5)

        
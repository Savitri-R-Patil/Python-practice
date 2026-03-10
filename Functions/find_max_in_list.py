def find_max(list):
    
    max=0
    for el in list:
        if(el>max):
           max=el
        continue
    return max
print(find_max([1,3,20,5,7,9]))

     
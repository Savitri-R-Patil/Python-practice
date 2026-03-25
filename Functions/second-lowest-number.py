def second_largest(list):
    n=len(list)
    for i in range(n):
      for j in range(n):
          if(list[j]>list[i]):
              temp=list[i]
              
              
              list[i]=list[j]
              list[j]=temp
    return list
              
              
sorted_list=second_largest([9,8,4,2,6])
N=len(sorted_list)
print(sorted_list[N-2])





              
          
         
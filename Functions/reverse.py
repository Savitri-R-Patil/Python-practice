def reverse(word):
    
    n=len(word)
    rev=""
    for i in range(n-1,-1,-1):
        rev= rev+ word[i]      #string is immutable but we can juts add--> ,means we  are creating new string
        
    return rev 
print(reverse("python"))

        
        
        
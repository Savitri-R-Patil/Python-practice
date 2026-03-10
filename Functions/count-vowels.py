def count(word1):
    count=0
    for L in word1.lower():
        if(L=='a' or L=='e' or L=='i' or L=='o' or L=='u'):
            count+=1
    print(count)
            
        
        


Word=input("Enter a word : ")
count(Word)
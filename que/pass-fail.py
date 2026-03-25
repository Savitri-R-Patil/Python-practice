name=input("enter a name :")

marks =int(input("enter a marks :"))

if(70>=marks>30):
    print(f" {name} pass with garade- B+")
elif(90>=marks>70):
    print(f"{name} passed with grade - A")
elif(marks>90):
    print(f"{name} passed with grade - A+")   
    
else:
    print("fail ")
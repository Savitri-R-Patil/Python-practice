#this behaves like :
#    Do
#    while


while True:
    n=int(input(" 1go on entering a numbers stops automatically when odd number enters :"))

    if(n%2!=0):
      print("odd")
      break
    else:
      continue
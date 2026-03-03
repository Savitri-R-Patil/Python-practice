#in python we can swap num without need of another temporary variable
a=9
b=7
# a,b=b,a  #this works 
a=b
b=a
print(a,b) # why doesn't work -->
                                #when i assign like a=b then value 9 is lost now a=7 bis already 7 and when iassign b=a becomes 7 (bcz a now has 7)
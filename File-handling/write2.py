f=open("File-handling/py.txt","r+")   #r+=both read and write 
f.write("added")                      #here this overwrites the first letters "This " with "added"
print(f.read())                        # gives output  as "file" because now pointer replace with "added" and reads remaining line
f.close()
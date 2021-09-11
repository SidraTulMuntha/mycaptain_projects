f=open(r"C:\Users\Mr. Kaif\Desktop\sid.files\New folder\New Text Document.txt","r")
# you can also use  print(f.readlines())

content=f.read()
print(content)
f.close()

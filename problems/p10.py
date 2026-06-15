
with open("text.txt","r") as f:
    file=f.read()

file2=file.replace("donkey","######")
    
with open("text.txt","w") as f:
     f.write(file2)

print(file2)
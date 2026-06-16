
words=["donkey","is","cute"]
with open("text.txt","r") as f:
    file=f.read()
for word in words:
    file=file.replace(word,"#" * len(word))
    
with open("text.txt","w") as f:
     f.write(file)

print(file)
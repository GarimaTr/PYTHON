
with open("text.txt","r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"python is present. Line no:{lineno}")   
        break
    lineno += 1 

else:
    print("No python is not present") 

print("###############")
line=1
with open("text.txt") as f:
    lines=f.readlines()

    if("python" in lines):
        print((int)(lines))






 
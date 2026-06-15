f = open("poem.txt")
c=f.read()
if("twinkle" in c):
    print("twinkle is present in content")
else:    
    print("twinkle is  not present in content")

f.close()
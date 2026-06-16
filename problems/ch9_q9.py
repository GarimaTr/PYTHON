with open("text.txt") as f:
    content1=f.read()


with open("this_copy.txt") as f:
    content2=f.read()

if(content1==content2):
    print("contents are identical")  
else:      
    print("contents are  not identical")    
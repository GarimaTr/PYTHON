a=int(input("Enter  number "))
b=int(input("Enter  number "))
c=int(input("Enter  number "))
d=int(input("Enter  number "))
if(a>b and a>c and a>d):
    print(f"Greatest number is: {a}")
elif(b>a and b>c and b>d):
    print(f"Greatest number is: {b}")
elif(c>b and a<c and c>d):
    print(f"Greatest number is: {c}")

else:
    print(f"Gretest number is:{d}")

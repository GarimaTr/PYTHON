def greatest():
    a = int(input("enter your number"))
    b = int(input("enter your number"))
    c = int(input("enter your number"))
    if a > b and a > c:
        print(a)
    elif b > c :
        print(b)
    else:
        print(c)
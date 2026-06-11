n=int(input("Enter the row: ")) 
def revstarpattern(n):
    if(n==0):
        return 
    else:
        print("*"*n,end="")
        print("")
        revstarpattern(n-1)

print(revstarpattern(n))
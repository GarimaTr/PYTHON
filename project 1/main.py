import random
'''
1 for snake
-1 for water
0 for gun'''
l=[1,-1,0]
n=input("Enter your choice by their first letter")
dict={"s":1,"w":-1,"g":0}
unidict={1:"Snake",-1:"Water",0:"Gun"}
you=dict[n]
computer=random.choice(l)
print("your choice "+unidict[you])
print("Computer's choice: "+unidict[computer])
if(computer==you):
    print("Its a draw")
else:
    if(computer==1 and you==-1):
        print("You lose")                                                    
    elif(computer==1 and you==0):
        print("You win")
    elif(computer==-1 and you==1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You lose")
    elif(computer== 0 and you==1):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You win")
    else:
        print("Something went wrong")

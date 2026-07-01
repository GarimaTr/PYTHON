a=89
def fun():
    global a #changes global variable
    a=3
    print(a)

fun()  
print(a)
  
   
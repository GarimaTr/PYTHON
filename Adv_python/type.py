
n: int=5
name:str="Harry"

def sum(a: int,b: int) -> int:
    return a+b
      
sum(3,5)
# print(sum)          print(sum) prints the function object itself, not the result of the call.  
print(sum(3,5))
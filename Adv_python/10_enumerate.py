l=[3,456,66,678]
# index=0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index+=1

#simplify this using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
print("****************************")

#if we want to start from second elements in index 
for index, item in enumerate(l[1:], start=1):
    print(f"The item at index {index} is {item}")  
print("********************************")
#OR
for item in l[1:]:
    print(item)
print("*****************************")    
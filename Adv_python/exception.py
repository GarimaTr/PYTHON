try:
    a=int(input("hey, enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyyy") 
    print(v)
except Exception as e:
    print("geyyyyyy")
    print(e)    

print("thank you")     


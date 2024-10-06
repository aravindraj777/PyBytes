# Addition
a = 2
b = 70.6

def add():
    print(a+b)


add() 

# Floor division

def floor_division():
    print(b // a)
    
floor_division()       

# Exponential
base = 2
exponent = 3
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")


# Identity operators

by = [1,2,34,4,5]
bx = by
resultx = by is b  #there is is and isnot 
resulty = by is not b
print(resultx," Result")
print(resulty, " Resulty")
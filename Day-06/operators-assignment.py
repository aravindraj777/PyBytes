
a = 50
b = 10


def sum():
    print("Sum is ",(a + b) )

def difference():
    print("Difference is ",(a - b))

def product():
    print("Product is ",(a * b))

def quotient():
    print(f"Quotient of {a} divided by {b} is {a // b}")
    

def comparison():
    print(a > b)
    print(a < b)
    print(a <= b)
    print(a >= b)
    print(a == b)
    print(a != b)
    

def logical():
    x = True
    y = False
    
    if not y:
        print("it is y")
    else:
        print("it is x")        


def assignment_operators():
    total = 10 
    
    total+= 1
    print(total)
    
    total-= 1
    print(total)
    
    total *= 2
    print(total)
    
    total /= 2
    print(total)
    
    


sum()
difference()
product()
quotient()
comparison()
logical()
assignment_operators()
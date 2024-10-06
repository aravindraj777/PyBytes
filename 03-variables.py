import sys

a = 10
b = 20
def addition(num1, num2):
    print("Method calling")
    return num1 + num2

def substraction():
    print(a - b)

# addition()
substraction()

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    output = addition(num1,num2)
    print("command line outout ",output)
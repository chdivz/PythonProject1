def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1/num2

#input
x = float(input("Enter first number"))
y = float(input("Enter Second number"))
operation = input("Choose operation (+, -, *, /): ")

if(operation == '+'):
    print(add(x,y))
elif(operation == '-'):
    print(subtract(x,y))
elif(operation == '*'):
    print(multiply(x,y))
elif(operation == '/'):
    print(division(x,y))
else:
     print("Invalid input")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

expression = input().split()
a = int(expression[0])
o = expression[1]
c = int(expression[2])

if o == '+':
    result = add(a, c)
elif o == '-':
    result = subtract(a, c)
elif o == '*':
    result = multiply(a, c)
elif o == '/':
    result = divide(a, c)
else:
    result = False

print(f"{a} {o} {c} = {result}")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2==0:
        return "The denominator cant be zero"
    else:
        return num1/num2

operation=input("Enter the operation to be performed:")
if operation in '+-*/':
    num1= int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if operation=='+':
        print(add(num1,num2))
    elif operation=='-':
        print(sub(num1,num2))
    elif operation=='*':
        print(mul(num1,num2))
    elif operation=='/':
        print(div(num1,num2))
else:
    print("Operation Invalid")

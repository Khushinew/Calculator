import operations

print("Simple Calculator")

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
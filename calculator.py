op=input("Enter a operation: ")
operations = '+-*/'
if op in operations:
    num1=int(input("enter a num1: "))
    num2=int(input("enter a num2: "))
    
    if op=='+':
            print(num1+num2)
    elif op=='-':
            print(num1-num2)
    elif op=='*':
            print(num1*num2)
    elif op=='/':
        if num2==0:
            print("The denominator cant be zero")
        else:
            print(num1/num2)
else:
    print("Invalid")

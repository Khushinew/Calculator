import operations

def input1():
    global num1,num2
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("List of Operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Change Numbers\n6.Exit")
    
    return True
input1()
just_showed_menu = True

while True:
    
    print()
    if just_showed_menu:
        op = input("Choose your operation:")
    else:
        print("List of Operations:|1.Addition|2.Subtraction|3.Multiplication|4.Division|5.Change Numbers|6.Exit")
        op = input("Choose your operation:")
    just_showed_menu=False
    print()
    if op=='1':
        operations.add(num1,num2)
    elif op=='2':
        operations.sub(num1,num2)
    elif op=='3':
        operations.mul(num1,num2)
    elif op=='4':
        operations.div(num1,num2)
    elif op=='5':
        input1()
        just_showed_menu=True
        continue
    elif op=='6':
        break
    else:
        print("Invalid choice")


    
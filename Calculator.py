import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return (a*b)

def div(a,b):
    if (b==0):
        return'INVALID OPERAND!, ERROR'
    return a/b

def remain(a,b):
    if (b==0):
        return'INVALID OPERAND!, ERROR'
    return a%b

def power(a,b):
    return a**b

def square_root(a):
    if (a<0):
        return 'Error:Cannot take the square root of Negative Number!'
    return math.sqrt(a)

while True:
   
    print('\nCalculator Operation')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication ')
    print('4.Division')
    print('5.Modulus')
    print('6.Power')
    print('7.Square Root')
    print('8.Exit')

    try:
        choice=int(input('Enter the operation(1-8): '))
    except ValueError:
        print('Invalid input!, Please enter a number in the range of (1,8)')

    if (choice==8):
        print('Exiting Calculator, Goodbye!')
        break

    if (choice==7):
        try:
            num=float(input('Enter the Number:'))
            print('Solution:',square_root(num))
        except ValueError:
            print('Enter the valid Number, Calculator do not except negative values!, Please enter the valid Numeric Value')
        continue

    if choice in [1,2,3,4,5,6]:
        try:
            num1=float(input('Enter the first number:'))
            num2=float(input('Enter the second number:'))
        except ValueError:
            print('Invalid input! Please enter the Numeric Value')
            continue

        if choice==1  :
            print('Solution:', add(num1,num2))
        elif choice==2 :
            print('Solution:', sub(num1,num2))
        elif choice==3 :
            print('Solution:',mul(num1,num2))
        elif choice==4 :
            print('solution:',div(num1,num2))
        elif choice==5:
            print('Solution:',remain(num1,num2))
        elif choice==6:
            print('Solution:',power(num1,num2))
        
    else:
        print("Invalid Operation")
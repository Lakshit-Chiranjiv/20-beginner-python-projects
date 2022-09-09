
def add(a,b):
    res = a + b
    print(str(a)+' + '+str(b)+' = '+str(res))

def sub(a,b):
    res = a - b
    print(str(a)+' - '+str(b)+' = '+str(res))

def mul(a,b):
    res = a * b
    print(str(a)+' x '+str(b)+' = '+str(res))

def div(a,b):
    res = a / b
    print(str(a)+' / '+str(b)+' = '+str(res))

def mod(a,b):
    res = a % b
    print(str(a)+' % '+str(b)+' = '+str(res))

choice = 1

while choice != 0:
    op = input("""
        A: Addition
        S: Subtraction
        M: Multiplication
        D: Division
        R: Modulation
        E: Exit
        Enter operation : 
    """)
    op = op.lower()
    match op:
        case 'a':
            print('ADDITION')
            x = int(input("Enter 1st number : "))
            y = int(input("Enter 2nd number : "))
            add(x,y)
        case 's':
            print('SUBTRACTION')
            x = int(input("Enter 1st number : "))
            y = int(input("Enter 2nd number : "))
            sub(x,y)
        case 'm':
            print('MULTIPLICATION')
            x = int(input("Enter 1st number : "))
            y = int(input("Enter 2nd number : "))
            mul(x,y)
        case 'd':
            print('DIVISION')
            x = int(input("Enter 1st number : "))
            y = int(input("Enter 2nd number : "))
            div(x,y)
        case 'r':
            print('REMAINDER / MODULATION')
            x = int(input("Enter 1st number : "))
            y = int(input("Enter 2nd number : "))
            mod(x,y)
        case 'e':
            print('EXIT')
            choice = 0
            continue
        case _:
            print('You entered wrong operation')
    
    choice = int(input('Do you want another operation 1/0 : '))
    if choice == 0:
        print('EXIT')





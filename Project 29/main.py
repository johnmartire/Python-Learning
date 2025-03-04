first_number= int (input("Type the first number: "))
operator=(input("Choose your operator: + - * /:  "))
second_number=int(input("Type the second number: " ))


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2 

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
result=operations[operator](first_number,second_number)
print(operations[operator](first_number,second_number))

continue_=input(f"Type y to continue calculating with {result} or type n to start a new calculation: " )
while True:
 if continue_=='n':
    first_number=int(input("Type the first number: "))
    operator=(input("Choose your operator: + - * /:  "))
    second_number=int(input("Type the second number: " ))
    print(operations[operator](first_number,second_number))
    result=operations[operator](first_number,second_number)
    continue_=input(f"Type y to continue calculating with {result} or type n to start a new calculation: " ) 
 if continue_== 'y':
    operator=(input("Choose your operator: + - * /:  "))
    second_number=int(input("Type the second number: " ))
    first_number=result
    print(operations[operator](first_number,second_number))
    result=operations[operator](first_number,second_number)
    continue_=input(f"Type y to continue calculating with {result} or type n to start a new calculation: " )
                    

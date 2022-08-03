import art 

def add(n1,n2):
    """ adding function """
    return n1+n2
def substract(n1,n2):
    """ substract function """
    return n1-n2
def multiply(n1,n2):
    """multiply function"""
    return n1*n2
def devide(n1,n2):
    """devide function"""
    return (n1/n2)

operations = {"+":add,
             "-":substract,
             "*":multiply,
             "/":devide
             }

def calculator():
    print(art.logo)
    y = True
    num1 = float(input("Whats is your first number?: "))
    while y:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line            above:     ")
        num2 = float(input("Whats is your second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculation with {answer},            or type 'n' to start new calculation: ").lower() == 'y':
           num1 = answer
        else: 
            y = False
            calculator()


calculator() 
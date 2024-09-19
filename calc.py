from art import logo
import sys, os

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
result_storage = {}
print(logo)
def calculator():
    try:
        f_number = float(input("Choose your first number: "))
        operation = input("Choose an operation you want to perform: +, -, * or / ")
        second_number = float(input("Choose your second number: "))
        result =operations[operation](f_number,second_number)
        result_storage["holder"] = result
        print(f" Your result: {result}")
    except ValueError:
        print("That was NOT a number!")
        os.execl(sys.executable, sys.executable, *sys.argv)


calculator()
def calculator_continuation():
    try:
        operation_choice = input("Choose an operation you want to perform: +, -, * or / ")
        nd_number =float(input("Choose your second number: "))
        result = operations[operation_choice](result_storage["holder"], nd_number)
        print(f" Your new result: {result}")
        result_storage["holder"] = result
    except ValueError:
        print("That was NOT a number!")


should_continue = True
while should_continue:
    try:
        question = input(f"Do you wish to continue calculating with {result_storage.get("holder")} ? (y/n) ")
        if question == "y":
            calculator_continuation()
        elif question == "n":
            os.system('clear')
            os.execl(sys.executable, sys.executable, *sys.argv)
    except ValueError:
        print("bzzt")










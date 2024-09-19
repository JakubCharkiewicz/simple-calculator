## Calculator Program
This Python program is a simple command-line calculator that performs basic arithmetic operations. It allows users to perform continuous calculations with the result from the previous operation and restart the process when needed.

## Features
Basic Operations: Supports addition, subtraction, multiplication, and division.
Chained Calculations: Users can continue calculating with the result from the last operation.
Error Handling: Handles non-numeric inputs and restarts the program when an invalid input is detected.
Session Continuation: Asks the user if they wish to continue calculating or restart the program.
## Requirements
Python 3.x
art module for ASCII art (you can install it via pip install art)
## Usage
Run the program.
Enter the first number.
Choose an arithmetic operation (+, -, *, /).
Enter the second number.
The result will be printed, and you'll be asked if you want to continue using the result for further calculations.
If you wish to stop, type n, and the program will restart.
## Functions
add(n1, n2): Returns the sum of n1 and n2.
subtract(n1, n2): Returns the difference of n1 and n2.
multiply(n1, n2): Returns the product of n1 and n2.
divide(n1, n2): Returns the quotient of n1 and n2 (if n2 is not zero).
## Example Interaction 
Choose your first number: 5
Choose an operation you want to perform: +, -, * or / +
Choose your second number: 3
Your result: 8.0

Do you wish to continue calculating with 8.0 ? (y/n) y
Choose an operation you want to perform: *
Choose your second number: 2
Your new result: 16.0

Do you wish to continue calculating with 16.0 ? (y/n) n
## Notes 
If an invalid input (non-number) is entered, the program will restart and prompt the user to try again.
The program uses os.execl() to restart itself, making it behave like a fresh run of the script.
The program prints an ASCII logo from the art package at the start.



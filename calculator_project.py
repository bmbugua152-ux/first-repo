def add (a,b):
    return a + b
def subtract (a,b):  
     return a - b
def multiply (a,b): 
     return a * b         
def divide (a,b):  
     if b == 0:
        return  "Error: Division by zero is not allowed."
     return round(a / b, 4)

def modulus (a,b): 
     return a % b
def power (a,b):   
     return a ** b
def calculator():
    print("Welcome to the calculator!")
    print("Select an operation:+, -, *, /, %, **")
    while True:
        try:
            operation = input("Enter the operation you want to perform: ")
            if operation in ['+', '-', '*', '/', '%', '**']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
                elif operation == '%':
                    result = modulus(num1, num2)
                elif operation == '**':
                    result = power(num1, num2)
                if isinstance(result, (int, float)):
                    result = round(result, 4)
                print(f"The result is: {result}")
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")    
calculator()


#self memory
class calcultor:
    def __init__(self):
        self.memory = 0
        self.history = []
    def calculate(self, operation, num1, num2):
        operations ={
            '+':num1 + num2,
            '-':num1 - num2,
            '*':num1 * num2, 
            '/':num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed.",
            '%':num1 % num2,
            '**':num1 ** num2
}
        result = operations.get(operation, "Invalid operation. Please try again.")
        if result != "Invalid operation. Please try again." and result != "Error: Division by zero is not allowed.":
            calculation = f"{num1} {operation} {num2} = {result}"
            self.history.append(calculation)
        return result 


def store_in_memory(self, value):
        self.memory = value
        print(f"Value {value} stored in memory.")
def recall_memory(self):
        print(f"Recalled value from memory: {self.memory}")
        return self.memory
def show_history(self):
        if self.history:    
            print("\n Calculation History:")
        for calculation in self.history[-5:]:  # Show last 5 calculations
            print(calculation)
        else:
            print("No calculations in history.")
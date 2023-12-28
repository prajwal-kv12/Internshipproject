def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Cannot divide by 0."

def calculator():
    print("command line calculator\nOperations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator: ")
            num2 = float(input("Enter the second number: "))

            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please enter +, -, *, or /")
                continue

            result = {
                '+': add(num1, num2),
                '-': subtract(num1, num2),
                '*': multiply(num1, num2),
                '/': divide(num1, num2)
            }.get(operator, f"Invalid operator: {operator}")

            print(f"Result: {result}")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation != 'yes':
                print("No more calculations.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Cannot divide by 0.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()

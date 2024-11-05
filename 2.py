def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ValueError("Division by zero error")
                result = num1 / num2
            else:
                print("Invalid operator. Please try again.")
                continue

            print("Result:", result)
            break

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculator()
import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    first_number = int(input("What is the first number?: "))
    should_continue = True
    answer = first_number

    while should_continue:
        print("+\n-\n*\n/")
        chosen_operator = input("Pick an operation: ")

        second_number = int(input("What is the second number?: "))

        if chosen_operator in operations:
            operation_function = operations[chosen_operator]
            answer = operation_function(answer, second_number)

            print(f"{first_number} {chosen_operator} {second_number} = {answer}")

            should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

            if should_continue == "y":
                continue
            elif should_continue == "n":
                calculator()
                break
        else:
            print("Invalid operator, please choose a valid one.")

calculator()


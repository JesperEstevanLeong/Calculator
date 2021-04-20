def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("-----------------------------------")
print("----------   Main Menu  -----------")
print("-----------------------------------")
print("-              1.Add              -")
print("-            2.Subtract           -")
print("-            3.Multiply           -")
print("-             4.Divide            -")
print("-            5. Exit              -")
print("-----------------------------------\n")

while True:
    # Take input from the user
    choice = input("Enter choice(1 to 4): \n")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("number1: \n"))
        num2 = int(input("number2: \n"))

        if choice == '1':
            print("<Solution>\n", "<Step1>\n", "   number1 + number2\n", "<Step2>\n", "   ", num1, "+", num2, "\n",
                  "<Solved>\n", "   Answer ==", add(num1, num2))

        elif choice == '2':
            print("<Solution>\n", "<Step1>\n", "   number1 - number2\n", "<Step2>\n", "   ", num1, "-", num2, "\n",
                  "<Solved>\n", "   Answer ==", subtract(num1, num2))

        elif choice == '3':
            print("<Solution>\n", "<Step1>\n", "   number1 * number2\n", "<Step2>\n", "   ", num1, "*", num2, "\n",
                  "<Solved>\n", "   Answer ==", multiply(num1, num2))

        elif choice == '4':
            print("<Solution>\n", "<Step1>\n", "   number1 / number2\n", "<Step2>\n", "   ", num1, "/", num2, "\n",
                  "<Solved>\n", "   Answer ==", divide(num1, num2))
        break
    else:
        print("Invalid Input.. Please Try Again")

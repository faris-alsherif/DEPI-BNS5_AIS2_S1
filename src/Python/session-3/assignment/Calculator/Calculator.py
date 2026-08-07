from Operations import *


def calc() -> None:
    """
    Run a simple calculator program.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Displays a menu, performs calculations, and exits when requested.
    """

    print("Welcome to the Simple Calculator!")

    while True:

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice (1/2/3/4) or 'exit' to quit: ")

        if choice.lower() == "exit":
            print("Exiting the calculator. Thank you!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Please enter valid numbers.")

        if choice == "4" and num2 == 0:
            print("Cannot divide by zero.")
            continue

        if choice == "1":
            result = add(num1, num2)
            print(f"The result of adding {num1} and {num2} is {result}")

        elif choice == "2":
            result = sub(num1, num2)
            print(f"The result of subtracting {num1} and {num2} is {result}")

        elif choice == "3":
            result = multi(num1, num2)
            print(f"The result of multiplying {num1} and {num2} is {result}")

        elif choice == "4":
            result = div(num1, num2)
            print(f"The result of dividing {num1} and {num2} is {result}")

        while True:
            again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

            if again == "yes":
                break

            elif again == "no":
                print("Exiting the calculator. Thank you!")
                return

            else:
                print("Please enter 'yes' or 'no'.")
from Operations import Operations


class Calculator:
    """
    Calculator class handles the calculator menu and
    performs mathematical operations.

    Methods:
        display_menu(): Displays the available operations.
        get_numbers(): Gets two numbers from the user.
        run(): Runs the calculator program.
    """

    def __init__(self):
        """
        Initializes the Calculator object.
        """
        pass

    def display_menu(self) -> None:
        """
        Displays the calculator menu.

        Returns
        -------
        None
            Displays the available operations.
        """
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Type 'exit' to quit.")

    def get_numbers(self) -> tuple[float, float]:
        """
        Gets two valid numbers from the user.

        Returns
        -------
        tuple[float, float]
            The first and second numbers.
        """
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                return num1, num2

            except ValueError:
                print("Please enter valid numbers.")

    def run(self) -> None:
        """
        Runs the simple calculator program.

        Returns
        -------
        None
            Displays the menu, performs calculations,
            and exits when requested.
        """
        print("Welcome to the Simple Calculator!")

        while True:
            self.display_menu()

            choice = input(
                "Enter your choice (1/2/3/4) or 'exit' to quit: "
            )

            if choice.lower() == "exit":
                print("Exiting the calculator. Thank you!")
                break

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice.")
                continue

            num1, num2 = self.get_numbers()

            if choice == "4" and num2 == 0:
                print("Cannot divide by zero.")
                continue

            operation = Operations(num1, num2)

            if choice == "1":
                result = operation.add()
                print(
                    f"The result of adding {num1} and {num2} is {result}"
                )

            elif choice == "2":
                result = operation.sub()
                print(
                    f"The result of subtracting {num1} and {num2} is {result}"
                )

            elif choice == "3":
                result = operation.multi()
                print(
                    f"The result of multiplying {num1} and {num2} is {result}"
                )

            elif choice == "4":
                result = operation.div()
                print(
                    f"The result of dividing {num1} and {num2} is {result}"
                )

            while True:
                again = input(
                    "\nDo you want to perform another calculation? (yes/no): "
                ).lower()

                if again == "yes":
                    break

                elif again == "no":
                    print("Exiting the calculator. Thank you!")
                    return

                else:
                    print("Please enter 'yes' or 'no'.")
class Operations:
    """
    Operations class performs basic mathematical operations
    on two numbers.

    Attributes:
        num1 (float): The first number.
        num2 (float): The second number.
    """

    def __init__(self, num1: float, num2: float):
        """
        Initializes the Operations object.

        Parameters
        ----------
        num1 : float
            The first number.
        num2 : float
            The second number.
        """
        self.num1 = num1
        self.num2 = num2

    def add(self) -> float:
        """
        Adds the two numbers.

        Returns
        -------
        float
            The addition of the two numbers.
        """
        return self.num1 + self.num2

    def sub(self) -> float:
        """
        Subtracts the second number from the first number.

        Returns
        -------
        float
            The subtraction of the two numbers.
        """
        return self.num1 - self.num2

    def multi(self) -> float:
        """
        Multiplies the two numbers.

        Returns
        -------
        float
            The multiplication of the two numbers.
        """
        return self.num1 * self.num2

    def div(self) -> float:
        """
        Divides the first number by the second number.

        Returns
        -------
        float
            The division of the two numbers.
        """
        return self.num1 / self.num2
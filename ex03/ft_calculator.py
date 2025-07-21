class calculator:
    """
    A calulator for vector-scalar operations
    """

    def __init__(self, values: list[float]) -> None:
        """
        Calculator function initializer
        """
        self.values = values

    def __add__(self, object) -> None:
        """
        Addition operation override
        """
        result = [x + object for x in self.values]
        self.values = result
        print(result)

    def __mul__(self, object) -> None:
        """
        Multiplication operation override
        """
        result = [x * object for x in self.values]
        self.values = result
        print(result)

    def __sub__(self, object) -> None:
        """
        Substraction operation override
        """
        result = [x - object for x in self.values]
        self.values = result
        print(result)

    def __truediv__(self, object) -> None:
        """
        Division operation override
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by 0")
            result = [x / object for x in self.values]
            self.values = result
            print(result)
        except ZeroDivisionError as msg:
            print("Error has occured:", msg)

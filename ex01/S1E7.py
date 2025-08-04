from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Baratheon initializer
        """
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Returns a value of the object in string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string (for development)"""
        return self.__str__()

    def die(self):
        """Change is_alive status to False"""
        self.is_alive = False


class Lannister(Character):
    """Lannister class"""

    def __init__(self, first_name, is_alive=True):
        """Lannister class constructor"""
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """__str__ override
Returns a readable string representation of the Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ override
Returns a officialstring represntation of the Lannister"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Make a new Lannister character
Parameter:
first_name(str)
is_alive(bool) : optional"""
        return cls(first_name, is_alive)

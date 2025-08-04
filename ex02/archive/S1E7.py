from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

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
        """
        Returns a value of the object in string
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Returns a string (for development)
        """
        return self.__str__()

    def die(self):
        """
        Change is_alive status to False
        """
        self.is_alive = False


class Lannister(Character):
    """
    Lannister class
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

        # decorator
    def create_lannister(first_name, is_alive=True):
        newCharacter = Lannister(first_name)
        newCharacter.first_name = first_name
        newCharacter.family_name = "Lannister"
        newCharacter.eyes = "blue"
        newCharacter.hairs = "light"
        return newCharacter

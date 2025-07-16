from abc import ABC, abstractmethod


class Character(ABC):
    """
    Character Class
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructeor for Character class
        Parameters:
            name(str): Name of the character
            is_alive(bool): life status of the character (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """
    Stark Class herits Character class
    """

    def die(self):
        """
        This changes the character's status to
        is_alive: False
        """
        self.is_alive = False

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

	def die(self):
		"""
		Change is_alive status to False
		"""
		self.is_alive = False
		return 0


# class Lannister(Character):
    #your code here
    # decorator


# def create_lannister(your code here):/
    #your code here


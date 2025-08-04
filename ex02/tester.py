from DiamondTrap import King

Joffrey = King("Joffrey")
# MRO : Method Resolution Order
# When declare King class Baratheon is indicated before Lannister
# so it will copies attributes Baratheon
# print(King.__mro__)
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

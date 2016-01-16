#Required Imports
#None

#In-Game Items
class Item(object):
	def __init__(self, name, worth, strength, defense, intelligence, dexterity):
		self.name = name
		self.worth = worth
		self.strength = strength
		self.defense = defense
		self.intelligence = intelligence
		self.dexterity = dexterity

#Weapons
ironlongsword = Item('iron longsword', 50, 5, 0, 0, 0)
steellongsword = Item('steel longsword', 75, 10, 0, 0, 0)
shortbow = Item('short bow', 50, 0, 0, 0, 5)
longbow = Item('long bow', 100, 0, 0, 0, 10)
woodstaff = Item('wooden staff', 50, 0, 0, 5, 0)
silverstaff = Item('silver staff', 100, 0, 0, 10, 0)

#Spells
fireball = Item('fireball', 50, 5, 0, 5, 0)
lightningbolt = Item('lightning bolt', 50, 5, 0, 5, 0)

#Armor
ironarmor = Item('iron armor set', 300, 0, 15, 0, 0)
steelarmor = Item('steel armor set', 500, 5, 20, 0, 0)
leatherarmor = Item('leather armor set', 200, 0, 10, 0, 5)
chainmail = Item('chainmail armor set', 400, 5, 15, 0, 10)
grayrobes = Item('gray robes', 75, 0, 5, 10, 0)
bluerobes = Item('blue robes', 350, 0, 10, 15, 0)


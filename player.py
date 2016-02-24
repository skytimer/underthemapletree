#Required Imports
import random
 
#Class Objects (Player / Enemy)
#User Player
class Player(object):
	def __init__(self, name, strength, defense, dexterity, charisma, intelligence, caste):
		self.name = name
		self.health = 100					#Here is where I define player values.
		self.strength = strength			##Later down the line, I will be adding
		self.defense = defense				###More skills to add a little more variety.
		self.dexterity = dexterity			#Strength, dexterity and intelligence are 
		self.charisma = charisma			##The skills that play the biggest role in
		self.intelligence = intelligence	###Combat currently.  Defense plays a small
		self.caste = caste					#Role in adjusting enemy damage and charisma
		self.level = 1						##Affects prices at the bartender.
		self.xp = 0
		self.victory = False
		self.inventory = {'Weapons': [], 'Armor': [],
						'Spells': [], 'Gold': 0, 'Misc': [], 'Potions': 0}
		self.equipped = {'Weapon': '', 'Armor': '', 'Spell': []}
		
#Enemies
class Enemy(object):
	def __init__(self, name, health, dmg):
		self.name = name
		self.health = health
		self.dmg = dmg
		
	def enemy_health(self):
		while True:
			if goblin.health != 50:
				goblin.health = 50
				break
			elif skeleton.health != 75:
				skeleton.health = 75
				break
			elif troll.health != 100:
				troll.health = 10
				break
			elif undead.health != 100:
				undead.health = 10
				break
			elif ogre.health != 100:
				ogre.health = 10
				break
			elif boss.health != 400:
				boss.health = 400
				break


""" ENEMY TYPES: """
goblin = Enemy('goblin', 50, 50)
skeleton = Enemy('skeleton', 75, 60)
troll = Enemy('troll', 100, 70)
undead = Enemy('undead', 150, 80)
ogre = Enemy('forest ogre', 200, 90)
boss = Enemy('giant forest ogre', 400, 100)
""""""""""""""""""""""""""""""""""""""""""""""""""
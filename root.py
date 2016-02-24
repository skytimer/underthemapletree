###ROOT FILE###
#Required Imports
from player import *
from texts import *
from items import *
from random import randint
import sys
import pickle
import os
import time

#Variable Booleans
beenchild = False		#These variables represent whether the player
beenwoman = False		##Has visted an area, or has bought an item.
beenguards = False
beendrifter = False
beenbar = False
equipsteelsword = False
equipsteelarmor = False
equiplongbow = False
equipchainmail = False
equipsilverstaff = False
equipbluerobes = False
equiplightning = False

#Save File Name
SAVEGAME = 'savefile.dat'

#Default Boot
def begin_game():	#The begin_game function is needed to boot a new  game
	create_character()	
	intro_story()
	game_loop()
	
#Game Loop
def game_loop():
	while True:	
		main()

###MAIN###
#Intro, Character Creation and Leveling
def intro_story():
	print "To read basic instructions about the game..."
	print ""
	manual = raw_input("Press [M]. Otherwise, press [Y] to continue.: ").lower()
	print ""
	if manual == 'm':
		print ""
		print rules_a
		print ""
		print rules_b
		print ""
		while True:
			cont_a = raw_input("Press [Y] to continue.: ").lower()
			if cont_a == 'y':
				print ""
				print rules_c
				print ""
				print rules_d 
				print ""
				break
			else:
				print "Syntax Error! You MUST press [Y] to continue!"
				print ""
				continue

		while True:
			cont_b = raw_input("Press [Y] to continue.: ").lower()
			if cont_b == 'y':
				print intro_a
				print ""
				print intro_b
				break
			else:
				print ""
				print "Syntax Error! You MUST press [Y] to continue!"
				print ""
				continue
		while True:
			cont_c = raw_input("Press [Y] to continue.: ").lower()
			if cont_c == 'y':
				print ""
				print intro_c
				print ""
				break
			else:
				print ""
				print "Syntax Error! You MUST press [Y] to continue!"
				print ""
				continue

	elif manual == 'y':
			print intro_a
			print ""
			print intro_b
			while True:
				inp = raw_input("Press [Y] to continue.: ").lower()
				if inp == 'y':
					print ""
					print intro_c
					print ""
					break
				else:
					print ""
					print "Syntax Error! You MUST press [Y] to continue!"
					print ""
					continue

			
def create_character():
	print intro
	print ""
	begin = raw_input("Press [Y] to begin!: ").lower()
	while begin:
		if begin == "y" :
			print ""
			print "Okay, Let's begin!"
			print ""
			break
		else:
			print ""
			print "Syntax Error! You MUST press [Y] to continue!"
			print ""
			begin = raw_input("Press [Y] to begin!: ").lower()
			continue
	choose_name = raw_input("Please type the name of your character!: ")
	print ""
	while choose_name:
		if choose_name != "":
			print "Your name is {0}!".format(choose_name)
			print ""
			confirm = raw_input("Is this correct? [Y] for yes and [N] for no.: ").lower()
			print ""
			if confirm == 'y':
				break
			elif confirm == 'n':
				print "Well, okay!  Would you type it again for me then?"
				print ""
				choose_name = raw_input("Please type the name of your character!: ")
				print ""
				continue
			else: 
				print "Syntax Error! Not a valid command!"
				print ""
				print "Could you just type your name one more time for me?"
				print ""
				choose_name = raw_input("Please type the name of your character!: ")
				print ""
				continue
	print castes
	choose_caste = raw_input("Please type the name of the class you wish to be.: ").lower()
	while choose_caste:
		global user
		state = dict()
		if choose_caste == 'knight':
			user = Player(choose_name, 15, 15, 10, 15, 10, 'Knight')
			user.inventory["Weapons"].append(ironlongsword.name)			
			user.inventory["Armor"].append(ironarmor.name)					
			user.inventory["Potions"] = 1								
			user.equipped["Weapon"] = (ironlongsword.name)
			user.equipped["Armor"] = (ironarmor.name)
			user.strength += ironlongsword.strength
			user.defense += ironarmor.defense
			print ""
			print "An Iron Armor set and Iron Longsword have been added to your inventory."
			print""
			break
		elif choose_caste == 'archer':
			user = Player(choose_name, 10, 15, 15, 10, 15, 'Archer')
			user.inventory["Weapons"].append(shortbow.name)
			user.inventory["Armor"].append(leatherarmor.name)
			user.inventory["Potions"] = 1
			user.equipped["Weapon"] = (shortbow.name)
			user.equipped["Armor"] = (leatherarmor.name)
			user.strength += (shortbow.strength + leatherarmor.strength)
			user.defense += leatherarmor.defense
			print ""
			print "A Leather Armor set and a Short Bow have been added to your inventory."
			print ""
			break
		elif choose_caste == 'mage':
			user = Player(choose_name, 10, 15, 10, 15, 15, 'Mage')
			state['players'] = [user]
			user.inventory["Weapons"].append(woodstaff.name)
			user.inventory["Spells"].append(fireball.name)
			user.inventory["Armor"].append(grayrobes.name)
			user.inventory["Potions"] = 1
			user.equipped["Weapon"] = (woodstaff.name)
			user.equipped["Armor"] = (grayrobes.name)
			user.equipped["Spell"].append(fireball.name)
			user.intelligence += (woodstaff.intelligence + grayrobes.intelligence)
			print ""
			print "Gray Robes, a Wooden Staff, and a Fireball spell have been added to your inventory!"
			print ""
			break
		else:
			print ""
			print "Syntax Error! Invalid class!"
			print ""
			choose_caste = raw_input("Please type the name of the class you wish to be.: ").lower()
			print ""
			continue
	stats = """
			NAME: {0},
			HEALTH: {1},
			LEVEL: {2} 
			CLASS: {3}
			STRENGTH: {4},
			DEFENSE: {5},
			DEXTERITY: {6},
			CHARISMA: {7},
			INTELLIGENCE: {8}
			""".format(user.name, user.health, user.level, 
			user.caste, user.strength, user.defense, user.dexterity,
			user.charisma, user.intelligence)
	print "Your stats are now as follows...:"
	print stats
	user.inventory["Gold"] += 50
	print""
	print "... and your inventory: {0}".format(user.inventory)
	print ""
	print "Let's start!"
	print ""

def level_up():
	global user
	while True:
		user.xp = 0		
		user.level += 1	
		print "You have leveled up!"						
		print ""
		print leveling
		inp = raw_input("Type the name of the skill you'd like to level up.: ").lower()
		lst = [x for x in skills if x.startswith(inp)]
		while inp:
			if len(lst) == 0:
				print ""
				print "No such skill."
				print ""
				continue
			elif len(lst) == 1:
				skill_level = lst[0]
				print ""
				print "You have chosen to level up {0}! It will be raised by 5 points.".format(skill_level)
				print ""
				correct = raw_input("Is this correct? Press [Y] for yes and [N] for no.: ").lower()
				if correct == 'y':
					print ""
					break
				else:
					print ""
					inp = raw_input("Type the name of the first skill you'd like to level up.: ").lower()
					print ""
					continue
			else:
				print ""
				print "Which of the following skills did you mean?: {0}".format(lst)
				print ""
				inp = raw_input("Type the name of the first skill you'd like to level up.: ").lower()
				continue
		while True:
			if skill_level == 'strength':
				user.strength += 5
				break
			elif skill_level == 'defense':
				user.defense += 5
				break
			elif skill_level == 'dexterity':
				user.dexterity += 5
				break
			elif skill_level == 'charisma':
				user.charisma += 5
				break
			elif skill_level == 'intelligence':
				user.intelligence += 5
				break
			else:
				print "Not a valid choice."
				print ""
				continue
		break

#Main Function
def main():
	global user
	if not os.path.isfile(SAVEGAME):
		with open('savefile.dat', 'wb') as f:
			pickle.dump(user, f)
			print "Game saved!"
			print ""
	else:
		 with open('savefile.dat', 'rb') as f:
			user = pickle.load(f)
			
	while True:
		if user.level == 1 and user.xp > 100:
			level_up()
		elif user.level == 2 and user.xp > 150:
			level_up()
		elif user.level == 3 and user.xp > 200:
			level_up()
		elif user.level == 4 and user.xp > 250:
			level_up()
		elif user.level == 5 and user.xp > 300:
			level_up()
		elif user.level > 5 and user.xp > 400:
			level_up()
		print options_a
		inp = raw_input("What would you like to do?: ").lower()
		print ""
		if inp == 'a':
			while True:
				print options_b
				inp_a = raw_input("What would you like to do?: ").lower()
				print ""
				if inp_a == 'a':
					while True:
						x = random.randint(1, 100)
						if x > 95 and user.level >= 5:
							print "You travel a couple miles east to East Glennrhoad Forest..."
							print ""
							pre_combat(boss)
							break
						elif (x > 90 and x <= 95) and user.level >= 4 :
							print "You travel a couple miles east to East Glennrhoad Forest..."
							print ""
							pre_combat(ogre)
							break
						elif (x > 75 and x <= 90) and user.level >= 3:
							print "You travel a half mile north to Vveldward Catacombs..."
							print ""
							pre_combat(undead)
							break
						elif (x > 55 and x <= 75) and user.level >= 2:
							print "You travel three or more miles west to Xzairellmorf Plains..."
							print ""
							pre_combat(troll)
							break
						elif x > 30 and x < 55:
							print "You travel about a mile north west to Slourendioor Graveyard..."
							print ""
							pre_combat(skeleton)
							break
						elif x > 0 and x <= 30:
							print "You travel a couple miles south to Llarvendae Forest..."
							print ""
							pre_combat( goblin)
							break
						else:
							continue
				elif inp_a == 'b':
					village()
					break
				elif inp_a == 'c':
					break
				else:
					print ""
					print "Syntax Error! Not a valid entry!"
					print ""
					continue
		elif inp == 'b':
			firsttime = True
			while True:
				if firsttime == True:
					print bar_a
					print ""
					print bar_b
					print ""
					inp = raw_input("Press [Y] to continue.: ").lower()
					while inp:
						if inp == 'y':
							firsttime = False
							barter()
							break
						else:
							print ""
							print "Syntax Error!"
							print ""
							inp = raw_input("Press [Y] to continue.: ").lower()
							print ""
							continue
							
				elif firsttime == False:
					barter()
					break
		elif inp == 'c':
			with open('savefile.dat', 'wb') as f:
				pickle.dump(user, f)
			print "Game saved!"
			print ""
			continue
		elif inp == 'd':
			sys.exit()
		else:
			print ""
			print "Syntax Error! You MUST press [Y] to continue!"
			print ""
			continue
			
#Village Functions			
def village():
	global beenchild
	global beenwoman
	global beenguards
	global beendrifter
	print village_a
	print ""
	while True:
		print village_b
		inp = raw_input("What do you wish to investigate?: ").lower()
		print ""
		if inp == 'a' and beenchild == False:
			beenchild = True
			child()
			break
		elif inp == 'a' and beenchild == True:
			print "You have already spoken with the child!"
			print ""
			break
		elif inp == 'b' and beenwoman == False:
			beenwoman = True
			woman()
			break
		elif inp == 'b' and beenwoman == True:
			print "You have already spoken with the woman!"
			print ""
			break
		elif inp == 'c' and beenguards == False:
			beenguards == True
			guards()
			break
		elif inp == 'c' and beenguards == True:
			print "You have already spoken with the guards!"
			print ""
			break
		elif inp == 'd' and beendrifter == False:
			beendrifter = True
			drifter()
			break
		elif inp == 'd' and beendrifter == True:
			print "You have already spoken with the guards!"
			print ""
			break
		else:
			print "Syntax Error!  Not a valid command!"
			print ""
			continue
def child():
	print child_a
	print ""
	print child_b
	print ""
	while True:
		inp = raw_input("How would you like to respond?: ")
		print ""
		if inp == 'a':
			print child_family
			print ""
			break
		elif inp == 'b':
			print child_angry
			print ""
			break
		elif inp == 'c':
			print child_sarc
			print ""
			break
		else:
			print "Syntax Error!  Not a valid command!"
			print ""
			continue

def woman():
	print woman_a	
	print ""
	print woman_choice
	print ""
	while True:
		inp = raw_input("How would you like to respond?: ")		
		print ""
		if inp == 'a':
			print woman_polite
			print ""
			break
		elif inp == 'b':
			print woman_rude
			print ""
			break
		elif inp == 'c':
			print woman_sarc
			print ""
			break
		else:
			print "Syntax Error!  Not a valid command!"
			print ""
			continue

def guards():
	while True:
		print guards_a
		print ""
		break

def drifter():
	print drifter_a
	print ""
	while True:
		print drifter_choice
		print ""
		inp = raw_input("What would you like to do?")
		print ""	
		if inp == 'a':
			print drifter_c
			print ""
			print "5 gold has been removed from your inventory."
			print ""
			user.inventory["Gold"] = (user.inventory["Gold"] - 5)
			break
		elif inp == 'b':
			print drifter_b
			print ""
			print "You, {0}, the renowned {1} of Llaroyn has died. ".format(user.name, user.caste)
			print ""
			print death_b
			print ""
			break
			
#Bartering, inventory, and equipping
def barter(): 
	global user
	global beenbar
	stats = """
		NAME: {0},
		HEALTH: {1},
		LEVEL: {2} 
		CLASS: {3}
		STRENGTH: {4},
		DEFENSE: {5},
		DEXTERITY: {6},
		CHARISMA: {7},
		INTELLIGENCE: {8}
		""".format(user.name, user.health, user.level, 
		user.caste, user.strength, user.defense, user.dexterity,
		user.charisma, user.intelligence)
	global game_state
	global equipsteelsword
	global equipsteelarmor
	global equiplongbow
	global equipchainmail
	global equipsilverstaff
	global equipbluerobes
	global equiplightning
	#Main
	while True:
		if beenbar == False:
			beenbar = True
			print bartender
			print ""
			break
		elif beenbar == True:
			break
	while True:
		print bartender_a
		print ""
		bar = raw_input("What would you like to do?: ").lower()
		print ""
		if bar == 'a':
			print "Your inventory: {0}".format(user.inventory)
			print "Items equipped: {0}".format(user.equipped)
			print ""
			continue
		elif bar == 'b':
			print stats
			print ""
			continue
		elif bar == 'c':
			print "The bartender mentions, 'We have the best deals in town!' "
			print ""
			print "You have {0} gold!".format(user.inventory["Gold"])
			print sale
			print ""
			while True:
				buy = raw_input("Type the name of the item you would like to buy, or press [X] to exit!: ").lower()
				print ""
				lst = [x for x in item_list if x.startswith(buy)]
				if buy != 'x':
					if len(lst) == 0:
						print "No such item."
						print""
						continue
					elif len(lst) == 1:
						item = lst[0]
						if item == 'steel longsword':
							if equipsteelsword == False and user.inventory["Gold"] >= steellongsword.worth:
								equipsteelsword = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								print "You now have {0} gold!".format(user.inventory["Gold"])
								user.equipped["Weapon"] = steellongsword.name
								user.strength += 10
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - steellongsword.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (steellongsword.worth - (steellongsword.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equipsteelsword == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < steellongsword.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
						elif item == 'steel armor set':
							if equipsteelarmor == False and user.inventory["Gold"] >= steelarmor.worth:
								equipsteelarmor = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								print "You now have {0} gold!".format(user.inventory["Gold"])
								user.equipped["Armor"] = steelarmor.name
								user.strength += 5
								user.defense += 20
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - steelarmor.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (steelarmor.worth - (steelarmor.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equipsteelarmor == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < steelarmor.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
						elif item == 'long bow':
							if equiplongbow == False and user.inventory["Gold"] >= longbow.worth:
								equiplongbow = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								print "You now have {0} gold!".format(user.inventory["Gold"])
								user.equipped["Weapon"] = longbow.name
								user.dexterity += 10
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - longbow.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (longbow.worth - (longbow.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equiplongbow == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < longbow.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
						elif item == 'chainmail armor set':
							if equipchainmail == False and user.inventory["Gold"] >= chainmail.worth:
								equipchainmail = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								print "You now have {0} gold!".format(user.inventory["Gold"])
								user.equipped["Armor"] = chainmail.name
								user.strength += 5
								user.defense += 15
								user.dexterity += 10
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - chainmail.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (chainmail.worth - (chainmail.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equipchainmail == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < chainmail.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
						elif item == 'silver staff':
							if equipsilverstaff == False and user.inventory["Gold"] >= silverstaff.worth:
								equipsilverstaff = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								print "You now have {0} gold!".format(user.inventory["Gold"])
								user.equipped["Weapon"] = silverstaff.name
								user.intelligece += 10
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - silverstaff.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (silverstaff.worth - (silverstaff.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equipsilverstaff == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < silverstaff.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue	
						elif item == 'blue robes':
							if equipbluerobes == False and user.inventory["Gold"] >= bluerobes.worth:
								equipbluerobes = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								user.equipped["Armor"] = bluerobes.name
								user.defense += 10
								user.intelligence += 15
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - bluerobes.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (bluerobes.worth - (bluerobes.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equipbluerobes == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < bluerobes.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
						elif item == 'lightning bolt':
							if equiplightning == False and user.inventory["Gold"] >= lightningbolt.worth:
								equiplightning = True
								print "You have bought a(n) {0}!  The item will now be equipped!".format(item)
								print ""
								user.equipped["Spell"].append(lightningbolt.name)
								user.strength += 10
								user.intelligence += 10
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - lightningbolt.worth)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								elif use.charisma >= 25:
									a = (lightningbolt.worth - (lightningbolt.worth * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
								continue
							elif equiplightning == True:
								print "This item is already equipped!"
								continue
							elif user.inventory["Gold"] < lightningbolt.worth:
								print "You do not have enough gold to purchase this item."
								print ""
								continue	
						elif item == 'health potion':
							if user.inventory["Gold"] >= 50:
								user.inventory["Potions"] += 1
								print "A health potion was added to your inventory!"
								print ""
								if user.charisma < 25:
									user.inventory["Gold"] = (user.inventory["Gold"] - 50)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
									continue
									
								elif use.charisma >= 25:
									a = (50 - (50 * (1 / 4)))
									user.inventory["Gold"] = (user.inventory["Gold"] - a)
									print "You now have {0} gold!".format(user.inventory["Gold"])
									print ""
									continue
							else:
								print "You do not have enough gold to purchase this item."
								print ""
								continue
					else:
						print "Which of the following items did you mean?: {0}".format(lst)
						print ""
						continue			
				elif buy == 'x':
					print ""
					break
		elif bar == 'd':
			print "You ask the bartender for the time."
			print ""
			timenow = time.strftime("%H:%M:%S")
			print "'The time is currently...: {0}'".format(timenow)
			print ""
			continue
		elif bar == 'e':
			print leave_bar
			print ""
			main()
			break

#Combat
def pre_combat(enemy = None):
	if enemy:
		print "As you enter the area, you see a {0}!  You enter combat...".format(enemy.name)
		print ""
		if combat(enemy):
			print ""
			
def combat(enemy):
	global user
	if enemy.health < 50:
		print "You see the {0} from earlier that killed you!  Get him!".format(enemy.name)
		print ""
	print "You health is at {0}.".format(user.health)
	print ""
	print "Your inventory: {0}".format(user.inventory)
	print "Items equipped: {0}".format(user.equipped)
	print ""
	while True:	
		if user.health > 0 and enemy.health > 0:
			inp = raw_input("Press [A] to attack or [H] to heal with a potion.: ").lower()
			print ""
			if inp == 'a':		
				if user.caste == 'Mage':
					dmgvalue = ((3 * user.strength) * (1 / 2))  
					userdmg = random.randint(1, (user.intelligence + dmgvalue))
					while True:
						print "Your available spells are: {0}.".format(user.equipped["Spell"])
						print ""
						choose_spell = raw_input("Type the name of the spell you wish to use.: ")
						print ""
						lst = [x for x in user.equipped["Spell"] if x.startswith(choose_spell)]
						if len(lst) == 0:
							print "No such spell! "
							continue
						elif len(lst) == 1:
							spell = lst[0]
							print "You cast {0}!".format(spell)
							print ""
							if spell == 'fireball':
								user.intelligence += fireball.intelligence
								user.strength += fireball.strength
							elif spell == 'lightning bolt':
								user.intelligencce += lightningbolt.intelligence
								user.strength += lightningbolt.strength
							break
						else:
							print "Which of the following spells did you mean?: {0}".format(lst)
							continue
				elif user.caste == 'Knight':
					while True:
						userdmg = random.randint(1, (user.strength + 10))
						break
				elif user.caste == 'Archer':
					while True:
						userdmg = random.randint(1, (user.dexterity + 10))
						break	
			elif inp == 'h':
				if user.inventory["Potions"] > 0:
					user.health += 50
					user.inventory["Potions"] -= 1
					user.inventory["Potions"] -= 1
					print ""
					print "You have healed by 50 points.  Your health is now at {0}.".format(user.health)
					print ""
					continue
				elif user.inventory["Potions"] == 0:
					print "You are out of health potions!"
					print ""
					continue
			else:
				print "Syntax Error! Not a valid command!"
				print ""
				continue
			x = (enemy.dmg - user.defense)
			var_x = random.randint(1, x)
			dieroll = random.randint(1, 20)
			if dieroll > 18:
				print "You did {0} damage to the {1}".format(userdmg, enemy.name)
				enemy.health = (enemy.health - userdmg)
				print ""
				continue
			elif dieroll > 12 and dieroll <= 18:
				hit = random.randint(1, 2)
				if hit == 1:
					print "You did {0} damage to the {1}".format(userdmg, enemy.name)
					enemy.health = (enemy.health - userdmg)
					print ""
					print "Its health is now at: {0}".format(enemy.health)
					print ""
					continue
				elif hit == 2:
					print "You did {0} damage to the {1}".format(userdmg, enemy.name)
					enemy.health = (enemy.health - userdmg)
					print ""
					print "Its health is now at: {0}".format(enemy.health)
					print ""
					print "It counter attacks, dealing {0} damage to you!".format(var_x)
					print ""
					user.health = (user.health - var_x)
					print "Your health is now at: {0}".format(user.health)
					print ""
					continue
			elif dieroll > 6 and dieroll <= 12:
				print "You did {0} damage to the {1}".format(userdmg, enemy.name)
				enemy.health = (enemy.health - userdmg)
				print ""
				print "Its health is now at: {0}".format(enemy.health)
				print ""
				print "It counter attacks, dealing {0} damage to you!".format(var_x)
				print ""
				user.health = (user.health - var_x)
				print "Your health is now at: {0}".format(user.health)
				print ""
				continue
			elif dieroll > 0 and dieroll <= 6:
				print "You miss completely!"
				print ""
				print "It counter attacks, dealing {0} damage to you!".format(var_x)
				print ""
				user.health = (user.health - var_x)
				print "Your health is now at: {0}".format(user.health)
				print ""
				continue
		elif user.health < 1:
				print "You, {0}, the renowned {1} of Llaroyn has died. ".format(user.name, user.caste)
				print ""
				print death
				print ""
				user.xp = 0
				user.health = 100
				print ""
				main()
				break	
		elif enemy.health < 1:
			print "You have killed the {0}".format(enemy.name)
			loot = random.randint(1, 20)
			while True:
				if loot > 18:
					user.xp += 100
					user.inventory["Gold"] += 200
					break
				elif loot > 15 and loot <= 18:
					user.xp += 75
					user.inventory["Gold"] += 150
					break
				elif loot > 11 and loot <= 15:
					user.xp += 50
					user.inventory["Gold"] += 100
					break
				elif loot > 6 and loot <= 11:
					user.xp += 25
					user.inventory["Gold"] += 50
					break
				elif loot > 0 and loot <= 6:
					user.xp += 10
					user.inventory["Gold"] += 25
					break
			print "You picked up some experience and gold!"
			print ""
			print "You are now at [{0} xp out of 100], and have {1} gold.".format(user.xp, user.inventory["Gold"])	
			print ""
			Enemy.enemy_health(self)
			break	
		elif user.health < 1 and enemy.health < 1:
			enemy.health = eh
			print "Both you, {0}, the renowned {1} of Llaroyn, and the {2} have died. ".format(user.name, user.caste, enemy.name)
			print ""
			print death
			user.xp += 10
			user.health = 100
			print ""
			print "You are now at [{0} xp out of 100]".format(user.xp)
			print ""
			Enemy.enemy_health(self)
			break

#Initialize Game
def initialize():
    global game_state
    if not os.path.isfile(SAVEGAME):
        begin_game()
    else:
        main()
	game_loop()
	
if __name__ == '__main__':
	initialize()
		


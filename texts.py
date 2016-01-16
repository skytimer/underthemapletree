#Required Imports
#None

#Intro and Rules and Default stats
intro = """
		[]Under the Maple Tree[]
		"""

castes = """CLASSES:
		 Knight: STR: 15, DEF: 15, DEX: 10, CHR: 15, INT: 10
		 Archer: STR: 10, DEF: 15, DEX: 15, CHR: 10, INT: 15
		 Mage: STR: 10, DEF: 15, Dex: 10, CHR: 15, INT: 15
		 """		

rules_a = """
		GAME MANUAL:
		(Noting basic instruction for gameplay.)
		1. To equip and buy items, or view your inventory, visit a bartender 
		at a local pub.  The equipping system is a part of the bartering
		mechanic.  When you buy an item, it will be equipped for you.
		You will sell your previous equipment, and it will be replaced with
		your new item.  As the item system is sincerely a very linear 
		progression of slight skill improvements, when you buy an item,
		your old item will become obsolete.  If you already own the item,
		you will be notified upon purchase, the item will be equipped and 
		the transaction will cancel.  
		"""
rules_b = """
		2. If you choose to play as a mage: do not type out full spell
		names in combat!  It is the way the spell system was designed.
		For example, if you have 'fireball' as an available spell, you
		only have to type 'f' to select it.  If you have two spells with 
		the same name, i.e. 'fireball' and 'firestorm', you will be prompted
		to specify further than just 'f', e.g. 'fires' for 'firestorm'.e
		THIS CONCEPT IS ALSO APPLIED WHEN BARTERING WITH THE BARTENDER!!
		So don't waste your time spelling out full item and spell names
		when you don't have to!
		"""
rules_c = """
		3. As you level up, different enemies and areas open up, and the
		story will progress! There is an assortment of dialogue, items, 
		and settings to explore.  There's a little more to the game than 
		repeated combat!  
		"""
rules_d = """
		4. Remember to have fun!  This game is not supposed to be overly
		intricate or hard.  It was built out of love for the text based 
		role-playing games I played as a child, and the desire to 
		improve my skills in Python programming.  Thank you so much for
		playing!   
		"""
intro_a = """
		You awake lying under an old, tall maple tree positioned on top 
		a large hill.  You look upwards through the criss-cross of 
		branches and leaves, through a small window in the web of 
		foliage, to be greeted by the rise of the moon and the setting 
		of dusk. 
		"""
intro_b = """
		You push yourself up, now sitting cross-legged in the grass, and
		gaze across the village at the bottom of the hill.  The rooftops
		form a collage of hay, wood, and stone.  You stand up now and 
		start to walk towards the village...
		"""
intro_c = """
		As you enter the village, you see mothers gathering their children
		for the night and drunkards just starting theirs.  The stench of
		urine, alcohol and ash flood the roads, forefully, and successfully
		escaping from the world around you to take refuge in your nose.
		You decide to stop by a pub and inn for a drink and a bed.  It
		has been non-stop travelling since Illengaurd a few days back.
		"""
bar_a = """
		You slither in through the front door of the pub, going virtually
		unnoticed by the other bar patrons, much like actual snakes in
		most of their daily affairs.  You drag yourself to the bar and 
		ask, in fashion that proclaims you have little importance and 
		just want to drink yourself dead, for a glass of ale.  The
		bartender asks, "Having a bad night, eh?"  You sigh slightly
		and explain you're from out of town.  "Well, this one's on me!"
		he exlaims.  He goes on to mention that you could buy most supplies
		you would need from him, including food, drink, weapons and armor.
		You buy a room and go to bed after too many drinks and too many
		hours bullshitting with the bartender.  If your sense of time 
		was correct, and granted it may not be due to the number of 
		beverages you consumed in the last few hours, it was close to 
		4 AM. You lie silently in your rented bed, spinning endlessly
		around, you close your eyes and try not to vomit.  Sleep creeps
		upon you moments later...
		""" 
bar_b = """
		The next morning you awake and instantly vomit on the floor next
		to your bed.  A small goblin is now living in your skull, banging
		on every inside edge until you commit suicide... or at least your
		headache felt very similar to that.  You get out of bed and equip
		yourself for the day... 
		
		You walk over to the bartender.
		"""

#Options and Choices
options_a = """
		a. Continue your adventure?
		b. Visit the bartender?
		c. Save game?
		d. Exit?
		"""

options_b = """
		Do you want to...
		a. Adventure nearby areas for enemies?
		b. Explore village?
		c. Return to previous menu?
		"""
leveling =  """
			You will type the name of a skill to increase.
			Only a fraction of the full word needs to be typed. (i.e. Stength = Str) 
			The skill you choose will be raised by five points.
			SKILLS:
			'STRENGTH'
			'DEFENSE'
			'DEXTERITY'
			'CHARISMA'
			'INTELLIGENCE'
			"""
bartender_a = """
			a. Inventory screen
			b. Stats screen
			c. Bartering / Equipping
			d. Ask for the time
			e. Leave the bar
			"""
sale = """
		ITEMS FOR SALE (if item is owned, when selected it will be equipped).:
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Steel Longsword (75 gold)[+10 STR]
		Steel Armor Set (500 gold)[+5 STR, +20 DEF]
		Long Bow (75 gold)[+10 DEX]
		Chainmail Armor Set (400 gold)[+5 STR, +15 DEF, +10 DEX]
		Silver Staff (100 gold)[+10 INT]
		Blue Robes (350 gold)[+10 DEF, +15 INT]
		Lightning Bolt -- SPELL (100 gold)[+10 STR, +10 INT]
		Health Potion (50 gold)[+50 HP]
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
village_b = """
			a. Talk to the small child throwing stones.
			b. Talk to the beautiful woman.
			c. Talk to the guards.
			d. Talk to the drifter.
			"""
child_b = """
		a. Ask about his family.
		b. Get angry and make a scene.
		c. Sarcasticly respond.
		"""
woman_choice = """
			a. Respond politely.
			b. Respond rudely.
			c. Respond sarcastically. 
			"""	
drifter_choice = """
			a. Give the man money.
			b. Don't give the man money.
			"""
			
#Dialogue / Story Text
bartender = """			
			The bartender recognizes you and calls you over.
			
			'What can I do for yeah...?'
			"""
leave_bar = """
			You decide to suddenly walk away from the bar without saying 
			goodbye to the bartender.  He doesn't take it personally, 
			because he figures you might be slow, or just crippled in 
			some way or another.  You push open the pub doors and walk 
			outside.  It is probably time to get back to adventuring!
			"""			
death = """
		A ranger from a nearby village has discovered your body.  As he
		loots your body; a powerful energy rises from the ground and 
		reanimates your lifeless body.  Truly, the Gods bless you.  As 
		you stand up, the ranger shouts gibberish loudly and runs into
		surrounding landscape.  You chuckle and continue adventuring...
		""" 
death_b = """
		A guard discovered your body lying on the stone roadway.  He
		loots your body; a powerful energy rises from the ground and 
		reanimates your lifeless body.  Truly, the Gods bless you.  As 
		you stand up, the guard shouts gibberish loudly and runs into
		surrounding village.  You chuckle and continue adventuring...
		""" 
village_a = """
		You stand in the village center.  As you look around, you see
		a small child throwing stones about, a beautiful young woman
		dressed in a rather appealing way, two guards arguing amongst 
		themselves, and a drifter pressed up against a wall in a small
		alleyway.
		"""
child_a = """
		You walk up to the child and introduce yourself.  Somewhat 
		listening to you speak, the child continues to launch pebble 
		after pebble at nearby birds and squirrels. After finishing 
		your introduction, you ask for his name and age.
		
		'Ayy, my name is Billy, I'm nine years old.  If yeah need to know, 
		I guess.  Something else you want?' he asks.
		
		"""
child_family = """
		You politely ask the child for information about his family.  He
		gives you an odd look, as if you asked him the most ridiculous 
		question ever asked by anybody ever.
		
		'Eh... well... why?  You know, my teacher says there are no stupid
		questions, yet I think I've finally found one, from some weird perv
		nonetheless.  Would you scram?  If you don't I'm gonna yell...'
		
		You walk away awkwardly, a passerby heard the conversation and 
		is chuckling behind your back.  You bow your head and walk towards
		the city square.
		"""
child_angry = """
		The kid continues to throw stones.  You decide it is of the upmost
		importance to act like a giant douchebag towards this child.  You
		grab his hand and take the pebbles.
		
		'This is what you get for being a little jackass!' you yell in
		a weirdly over-confident voice.  People start looking at you.
		
		You start repeatedly throwing stones at the little boy, aiming
		primarily for his face.  He runs away crying in a manic fashion.
		
		Feeling proud, you walk away with a large smile.
		
		Good job, dick.
		"""
child_sarc = """
		You mention that you think his stone throwing is 'super cool' and 
		that you think he's the coolest kid in the village.
		He looks up at you and says,
		
		'Do you really think so?'
		
		You reply, 'Who would ever think that?  I mistook you for a very
		ugly small pig at first glance.  If that's what people first see
		in you, you'll never be cool, kid.  Try working on that. '
		
		Tears slowly fill his eyes.  He drops the rocks and walks away
		slowly wiping tears from his face.  
		
		Good job.  You made a small child cry.
		"""
woman_a = """
		You walk towards the woman.  As you approach, her face curls
		in a rather unsightly way.  
		
		'Hello! How's a beautiful lady like yourself doing today?', you
		say to her.
		
		'Oh look, another member of the patriarchy here to save a poor
		woman like myself from being so beautiful!  How can I ever repay you?',
		she asks.
		"""
woman_polite = """
			You chuckle politely and ask if she would like to grab a drink
			with you.  She responds by spitting in your face and calling 
			you a sexist pig for asking her out.  Confused, you walk away
			silently.
			"""
woman_rude = """
			You tell her to go fuck herself with the bullshit that just
			oozed from her mouth.  'Member of the patriarchy... fuck you!,
			you say.  You then offer to take her into a back alleyway for
			ten gold pieces.  She tells you to stick it up your ass and
			walks away agrily.  Pleased with yourself, you walk away smiling.
			
			Good job, asshat.
			"""
woman_sarc = """
			You play along with her sarcasm and respond, 
			
			'I do not need payment, for you are a princess!  I can tell
			by the large number of sweat stains that you must be royalty
			and deserve only the best.'
			
			She tells you to shove it, and walks away angrily.
			"""
guards_a = """
			You walk to the guards and say hello.  One guard mentions that
			you're looking rather suspicious.  When you speak to the contrary
			of the observation made by the gaurd, he takes it as a 
			personal attack.  The other guard mentions that you're a light 
			skinned man, and not one of those darkies from Ereraldi, but
			the other guard insists on your arrest.  The two guards grab
			onto you and wrestle you to the ground yelling 'Stop resisting!'.
			After you have been properly beaten, you are tied and taking
			to the village prison for the night...
			
			You wake up the next morning bruised and beaten.  Angrily,
			you sign your release papers and head back to the main village.
			"""
drifter_a = """
			You walk over to the alleyway where the old homeless man sits.
			You introduce yourself and then ask a bit about him and his
			current situation. 
			
			'Oh, you know... times are tough.  Ever since the housing
			collapse in 1008, under Mayor Amabo, things have been really
			hard.  Think you could spare some coin for me...?'
			"""
drifter_b = """
			You laugh loudly in the drifter's face.  
			
			'Give out my hard earned money?  That'll just be a crutch for 
			you!  The reason you're poor is because you're not working hard
			enough!  People don't need help if they work hard!'
			
			You pull a hard candy from your pocket and toss it back in your
			mouth.  Immediately, the candy get lodged in your throat.  As
			you ask for help, the drifter laughs and notes that 'You just
			not trying hard enough.'  Within another forty-five seconds,
			you faint from a lack of oxygen.  As you hit the ground, your
			head bounces off the stone roadway, killing you instantly.
			"""
drifter_c = """
			You pull a few gold coins out of your wallet and give them to him.
			The drifter smiles pleasently and thanks you for your kindness.
			
			'May the Gods bless you...'
			
			His shaking hands put the coins in his pocket.  As you're 
			walking away, a man runs up to the drifter and stabs him repeatedly,
			taking the gold you just donated.  You yell for the man, and he
			replies
			
			'You were too strong to mug, so I took on the old man instead!
			Too bad you'll never catch me!'
			
			The theif runs into the shadows of the village.  You sprint
			to the old man and pull him into your arms.  His blood trickles
			down your hands.  
			
			'Thank you... thank you so much.  But alas, there is nothing
			that can be done.  I was born on the street, now I will die here.
			Farewell, friend...'
			
			The man's eyes close as he passes away.  You lower the body
			to the ground and alert the guards.  Shocked, you sit down
			on a park bench and simply think about things for the next
			hour or so, watching people as they walk by...  What a day...
			
			After you pull yourself together, you stand up walk forward,
			ready for more adventure. 
			"""
			
#Lists
skills = ['strength', 'defense', 'dexterity', 'charisma', 'intelligence']
item_list = ['steel longsword', 'steel armor set', 'long bow', 'chainmail armor set', 
'silver staff', 'blue robes', 'lightning bolt', 'health potion']			

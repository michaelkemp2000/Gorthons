# scenes.py

from sys import exit
from random import randint

# Scene Parent Class Placeholder

class Scene(object):


	def enter(self):
		print "This scene is not yet configured.  Subclass it and implement enter()."
		exit(1)

# Death Scene Child Class to Scene.
class Death(Scene):


	# Dictionary of different messages when you die.
	quips = ["\nYou Died.  You kinda suck at this.", 
			"\nYou Died.  Your mom would be proud if you were smarter",
			"\nYou Died. Such a luser.", 
			"\nYou Died. I have a small puppy thats better than this."
	]

	# Function to define what happens when you enter the scene.
	def enter(self):

		print Death.quips[randint(0, len(self.quips) -1)]
		exit(1)


# Escape Pod Child Class to Scene
class EscapePod(Scene):
	

	# Function to define what happens when you enter the scene.
	def enter(self):

		print "You rush through the ship desperatly trying to make it to the"
		print "escape pod before the whole ship explodes."
		print "It seems like hardly any Gorthons are on the ship, so you run"
		print "clear of interference.\n"
		print "You enter the escape pod room and see a large Gorthon with" 
		print "advanced battle armor.  He must be the invasion party leader."
		print "\nThere are also five escape pods that he has been tampering" 
		print "with to retrofit with bombs."
		print "Do you take an escape pod or fight (E or F)?"
		# Take input from command line.
		ans2 = raw_input("-->")

		if ans2 == 'e' or ans2 =='E':
			print "The Gorthon general start to laughing in your mind."
			print "Is this some kind of telepathic abillity?"
			print "You hear a voice in your head,"
			print " \'Stupid HUMAN, The majority of those pods are not functioning!"
			print "Good luck!\'"
			# Randomize a number and enter into a variable.
			good_pod = randint(1,5)
			# Take input for command line.
			guess = raw_input("[pod #]>")

			if int(guess) != good_pod:
				print "You jump into pod %s and hit the eject button." % guess
				print "The pod exscapes out into the void of space, then implodes as"
				print "the hull ruptures, crushing your body."
				return 'death'

			else:
				print "You jump into pod %s and hit the eject button." % guess
				print "The pod easierly slides out into space, heading to the planet below."
				print "As it flies to the planet, you look back and see your ship explode" 
				print "like a bright star, taking out the Gorthon ship also."
				return 'planet'
		
		elif ans2 == 'f' or ans2 == 'F':
			print "You hear a voice in your mind, could this be from the Gorthon general."  
			print "Does he have some kind of telepathic ability."
			print "You cannot defeat me!"
			weapon = a_hero.items.get('weapon')

			if weapon == 'plasma cannon':
				print "you pull out your plasma cannon"
				print "The Gorthon looks concerned and backs up"
				winner = b_battle.attack()

				if winner == 'hero':
					print "You fall to the ground you head is hurting."
					print "All of a sudden you feel very different."
					print "You aquire the general\'s telepathic abilities."
					print "You have to get off the ship.  You look at the 5 pods."
					print "Somehow, you know pod 2 is functioning well."
					print "You jump in pod 2 and hit the eject."
					print "The pod easierly slides out into space, heading to the planet below."
					print "As it flies to the planet, you look back and see your ship explode"
					print "like a bright star, taking out the Gorthon ship also."
					return 'planet'

				elif winner == 'alien':
					print "Fatal shot, you cannot sustain this injury!"
					return 'death'

				else:
					return 'death'

			else:
				print "This Gorthon is much bigger than you are with some serious armor."
				print "This may not go well"
				winner = b_battle.attack()

				if winner == 'hero':
					print "You fall to the ground you head is hurting."
					print "All of a sudden you feel very different."
					print "You aquire the general\'s telepathic abilities."
					print "You have to get off the ship.  You look at the 5 pods."
					print "Somehow, you know pod 2 is functioning well."
					print "You jump in pod 2 and hit the eject."
					print "The pod easierly slides out into space, heading to the planet below."
					print "As it flies to the planet, you look back and see your ship explode"
					print "like a bright star, taking out the Gorthon ship also."
					return 'planet'

				elif winner == 'alien':
					print 'Try looking for a better weapon to defeat the general somewhere in this game (L)'
					return 'death'

				else:
					return 'death'


# Planet Child Class to Scene
class Planet(Scene):


	# Function to define what happens when you enter the scene.
	def enter(self):

		print "\nYou land saftly on your planet only to find that its now inhabited by Gorthons #!?#."  
		print "What happened?"
		print "Enjoy the next chapter in this space adventure Gortham #2 - What happened to my planet?"
		exit(1)


# Central Corridor Child Class to Scene
class CentralCorridor(Scene):


	# Function to define what happens when you enter the scene.
	def enter(self):

			print "\nYou find yourself in a central corridor with three door labeled Armory, Bridge and Escape Pod."
			print "There is a Gorthon guarding.  Do you:"
			print "Attack the Gorthon (A)"
			print "Go to the Laser Weapons Armory (L)"
			print "Go to the Bridge (B)"
			print "Go to the escape pod (E)"
			cc_opt = raw_input("-->")

			if cc_opt == 'a' or cc_opt == 'A':
				winner = a_battle.attack()

				if winner == 'hero':
					print "\nYou pickup a passcode from his dead corpse"
					a_hero.add_item('passcode', '1234')
					print "Go to the Laser Weapons Armory (L)"
					print "Go to the Bridge (B)"
					print "Go to the escape pod (E)"
					cc_opt = raw_input("-->")

					if cc_opt == 'b' or cc_opt == 'B':
						return 'the_bridge'

					elif cc_opt == 'e' or cc_opt == 'E':
						return 'escape_pod'

					elif cc_opt == 'l' or cc_opt == 'L':
						return 'lwa'

					else:
						print "DOES NOT COMPUTE!: The Gorthon resurects itself"
						return 'central_corridor'

				else:
					return 'death'
				
			elif cc_opt == 'b' or cc_opt == 'B':
				return 'the_bridge'

			elif cc_opt == 'e' or cc_opt == 'E':
				return 'escape_pod'

			elif cc_opt == 'l' or cc_opt == 'L':
				return 'lwa'

			else:
				print "DOES NOT COMPUTE!"
				return 'central_corridor'


# lwa Child Class to Scene
class LaserWeaponArmory(Scene):
	

	# Function to define what happens when you enter the scene.
	def enter(self):

		print "You do a dive roll into the Weapons Armory, crouch and scan the room for more Gorthons"
		print "that might be hiding.  It\'s dead quite, too quite.\n"
		print "You stand up and run to the far side of the room and find the neutron bomb container."  
		print "There is a keypad lock on the box and you need the code to get thebomb out."
		print "If you get the code wrong 10 timesthen the lock closes forever and you can't get the bomb."  
		print "The code is 3 digits.\n"
		ans1 = 'Null'

		while ans1 != 'm' or ans1 != 'M':
			print "Do you enter the code manually, check your inventory first or go back to the central corridor?"
			print "Select (M, I, C)"
			ans1 = raw_input("-->")

			if ans1 == 'M' or ans1 == 'm':
				code = "%d%d%d" % (randint(1,9), randint(1,9),
									 randint(1,9))
				guess = raw_input("[keypad]>")
				guesses = 0

				if guess == Hero.items.get('passcode'):
					print "The container clicks open and the seal breaks, letting gas out."
					print "You grab the neutron bomb and head to the bridge."
					Hero.items['bomb'] = "neutron"
					return 'the_bridge'

				# Increment keypad guesses
				while guess != code and guesses < 10:
					print "BZZZZZEDDD!"
					guesses += 1
					guess = raw_input("[keypad]>")

				if guess == code:
					print "The container clicks open and the seal breaks, letting gas out."
					print "You grab the neutron bomb and head to the bridge."
					return 'the_bridge'

				else:
					print "The lock buzzes one last time and then you hear a sickening melting sound"
					print "as the mechanism is fused together.\n"
					print "You decide to sit there for a while, and finally Gorthans blow up you home"
					print "planet below and your ship.\n"
					return 'death'

			elif ans1 == 'C' or ans1 == 'c':
				pc = Hero.items.get('passcode')
				if pc != '1':
					print "You need the Neutron Bomb! You're not in time to save the ship and planet."
					return 'death'

				else:
					return 'central_corridor'

			elif ans1 == 'I' or ans1 == 'i':
				print "you look in you pocket and find: ", Hero.items['passcode']

			elif ans1 == 'L' or ans1 == 'l':
				print "You examine the room and find a plasma cannon hidden under some large"
				print "containers that must have falled due to the attach on your ship."
				a_hero.set_weapon('weapon', 'plasma cannon')

			else:
				print "DOES NOT COMPUTE!"
				return "lwa" 


# Bridge Child Class to Scene
class TheBridge(Scene):


	# Function to define what happens when you enter the scene.
	def enter(self):

		# See if the hero has the bomb from laser weapon armory.
		bomb = Hero.items.get('bomb')
		if bomb == 'neutron':
			print "\nYou burst into the Bridge with the neutron destruction bomb under your arm" 
			print "and surprise 5 Gorthons who are trying to take control of the ship.\n"
			print "They haven\'t taken thier weapons out yet, and they see the active bomb under your arm"
			print "and don't want to set it off.\n"
			print "Do you throw the bomb or slowly place the bomb (T or P)?"
			action = raw_input("-->")

			if action == 't' or action == 'T':
				print "In a panic you throw the bomb and the group of Gorthons and make a leap for the door."
				print "Right as you drop it a Gorthon shoots you right in the back, killing you."
				print "As you die, you see another Gorthon frantically trying to disarm the bomb."
				print "You die knowing that they will probably blow up when it goes off."
				return 'death'

			elif action == 'p' or action == 'P':
				print "You point your blaster at the bomb under your arm and the Gorthons put thier hands up" 
				print "and start to sweat"
				print "You inch backwards to the door, open it, and then carefully place the bomb on the floor."
				print "You then jump back through the door, punch the close button abd blast the lock"
				print "so the Gorthons cant get out."
				print "Now the bomb is placed, you run to the escape pod to get off this tin."
				return 'escape_pod'

			else:
				print "DOES NOT COMPUTE! You get shot!"
				return "death"

		else:
			print "You burst into the Bridge and surprise 5 Gorthons who are trying to take control of the ship.\n"
			print "They turn and look at you.  You\'re toast, the show you mercy with a quick death!"
			return 'death'

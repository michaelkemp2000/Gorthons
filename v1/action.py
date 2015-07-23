# actions.py

from sys import exit
from random import randint

class Engine(object):


	def __init__(self, scene_map):

		# This is now the Map instance (a_map) that contains start_scene 
		# in a.map (central_corridor was passed #194).
		self.scene_map = scene_map

	def play(self):
		
		# Step 4 & 7.  This calles a.map opening scene function and 
		# puts the return in current_scene.
		curent_scene = self.scene_map.opening_scene()
		
		# Steo 8.
		while True:
			print "\n-----------------------------------------------"
			# Step 9.  Calling current scene (centralCorridtor().enter) function.
			next_scene_name = curent_scene.enter()
			curent_scene = self.scene_map.next_scene(next_scene_name)

#Battle class
class Battle(object):


	# Define Battle and pass in who is doing battle,
	# In this games case, alien and hero, probably should be a list of potential
	# characters if the game was to be extended, not hard coded expectations.
	def __init__(self, alien, hero):

		self.alien = alien
		self.hero = hero

	# Hero attack function.
	def attack(self):
		
		# Depending on the weapon defined, we hard code attack power.
		# If we were to extend the game, probably attack power would be
		# passed in with the item, vs hard coded.
		# The same could be true with behaviour.
		weapon = Hero.items.get('weapon')
		print weapon
		if self.alien.health > 0:
			print "\nThe Alien shouts ggrazadbog!"
			print "You fire your weapon at the Gorthon."
			while self.alien.health > 0:
				if weapon == 'laser gun':
					a_damage = randint(1,4)
					print "zap: [-%d] hit point!" % a_damage 
					self.alien.reduce_health(a_damage)
					if self.alien.health > 0:
						print "He is not dead!"
						self.defend()
					
					else:
						print "You killed the Gorthon"
						return 'hero'
				else:
					a_damage = randint(5,10)
					print "zap: [-%d] hit point!" % a_damage 
					self.alien.reduce_health(a_damage)
					if self.alien.health > 0:
						print "He is not dead!"
						self.defend()
						return 'hero'
					else:
						print "You killed the Gorthon"
						return 'hero'
				return 'alien'
			if self.alien.health < 0:
				print "You killed the Gorthon"
				return 'hero'

		else:
			print "\nThe Gorthon is already dead"
			return 'hero'

	# Function for when the Hero is defending against an alien attack.
	def defend(self):

		print "\nThe Gortham starts shooting at you!"

		while self.hero.health > 0 and self.alien.health >0:
			h_damage = randint(1,4)
			print "zap: [-%d] damage!" % h_damage
			self.hero.reduce_health(h_damage)
			print "Health remaining: [%d]" % self.hero.health

			if self.hero.health > 0:
				print "Shoot or Run (S or R)"
				atk = raw_input("-->")

				if atk == 's' or atk == 'S':
					self.attack()

				elif atk == 'r' or atk == 'R':
					print "You flee like a coward and get shot."
					return 'alien'

				else:
					print "DOES NOT COMPUTE: You fumble around and get shot."
					return 'alien'

			else:
				print "You sustain a fatal wound."
				return 'alien'

# Map Class
class Map(object):


	# Dictionary of all the different scenes that are looked up
	# by the Engine class to determine what is the next scene.
	scenes = {
		'central_corridor': CentralCorridor(),
		'lwa': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'planet': Planet(),
		'death': Death()
		}

	# Specifies the start scene, where the game starts.
	def __init__(self, start_scene):

		self.start_scene = start_scene

	# Specifies the next scene.
	def next_scene(self, scene_name):

		# Step 6.  This looks up scene name in dict, originally central corridor 
		# and returns CentralCorridor().
		return Map.scenes.get(scene_name) 

	# Function which provides the opening scene
	def opening_scene(self):

		print "\nYou wake up from hyper-sleep and Gorthons have invaded your ship and its"
		print "completly incapacitated."
		print "You are the last surviving crew member and ou have learned of their plans to"
		print "nuke your home planet below!\n"
		print "You must stop the Gorthons!\n"
		print "1. Your mission is to get the neutron destruct bomb from the"
		print "Weapons Armory put it in the Bridge"
		print "2. Blow up the ship, after you have accessed the escape pod and"
		print "launched to the plannet below\n"
		print "Are your ready to proceed (y / n)?"

		start = raw_input("-->")
		
		if start == 'N' or start == 'n':
			print "Your trapped on the ship you fool!  Ok you jetty yourself into space and die"
			self.start_scene = 'death'
			return self.next_scene(self.start_scene)
		
		elif start == 'Y' or start == 'y':
			# Step 5.  This calles a.map next scene function and puts the return to output to current 
			#scene in play function (#186).
			return self.next_scene(self.start_scene)

		else:
			print "DOES NOT COMPUTE!, your planet is destroyed below by a neutron bombs."
			print "The shockwave takes out you and your ship"
			self.start_scene = 'death'
			return self.next_scene(self.start_scene)

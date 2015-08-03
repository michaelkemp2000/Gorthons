# start.py

# Now import your v1 Package.
import v1
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


# Map Class
class Map(object):


	hero = v1.Person('y', 10)
	gorthon_guard = v1.Person('y', 5)
	gorthon_soldier = v1.Person('y', 100)
	gorthon_general = v1.Person('y', 15)
	hero.set_alive(True)
	gorthon_guard.set_alive(True)
	gorthon_general.set_alive(True)
	hero.set_contents('weapon', 'laser gun')
	gorthon_guard.set_contents('weapon', 'laser gun')
	gorthon_soldier.set_contents('weapon', 'laser sword')
	gorthon_general.set_contents('armor', 'battle class')
	gorthon_general.set_contents('weapon', 'laser sword')
	gorthon_general.set_contents('weapon2', 'laser gun')
	a_battle = v1.Fight(hero, gorthon_guard)
	b_battle = v1.Fight(hero, gorthon_general)	

	# Dictionary of all the different scenes that are looked up
	# by the Engine class to determine what is the next scene.
	scenes = {
		'central_corridor': v1.CentralCorridor(hero, a_battle),
		'lwa': v1.LaserWeaponArmory(hero),
		'the_bridge': v1.TheBridge(hero),
		'escape_pod': v1.EscapePod(hero, b_battle),
		'planet': v1.Planet(),
		'death': v1.Death()
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



# ------------------------Module tests------------------------------------------

# Instanciate Character defaults
# hero = v1.Person('y', 100)
# gorthon_guard = v1.Person('y', 50)
# gorthon_soldier = v1.Person('y', 100)
# gorthon_general = v1.Person('y', 200)
# hero.set_alive(True)
# gorthon_guard.set_alive(True)

# # Set Character Items
# hero.set_contents('weapon', 'laser gun')
# gorthon_guard.set_contents('weapon', 'laser gun')
# gorthon_soldier.set_contents('weapon', 'laser sword')
# gorthon_general.set_contents('armor', 'battle class')
# gorthon_general.set_contents('weapon', 'laser sword')
# gorthon_general.set_contents('weapon2', 'laser gun')

# # Set Battles

# a_battle = v1.Fight(hero, gorthon_guard)
# b_battle = v1.Fight(hero, gorthon_general)

# Print Character state
# h_state = hero.check_alive()
# h_health = hero.check_health()
# gg_state = gorthon_guard.check_alive()
# gg_health = gorthon_guard.check_health()
# gs_state = gorthon_soldier.check_alive()
# gs_health = gorthon_soldier.check_health()
# gb_state = gorthon_general.check_alive()
# gb_state = gorthon_general.check_health()


# print "\nHero: [%s] - %d" % (h_state, h_health)
# print "\nGorthon Guard: [%s] - %d" % (h_state, h_health)
# print "\nGorthon Soldier: [%s] - %d" % (h_state, h_health)
# print "\nGorthon General: [%s] - %d" % (h_state, h_health)

# # Print Character items
# h_items = hero.check_contents()
# gg_items = gorthon_guard.check_contents()
# gs_items = gorthon_soldier.check_contents()
# gb_items = gorthon_general.check_contents()
# print "\nHero - List of items: %r" % (h_items)
# print "\nGorthon - List of items: %r" % (gg_items)
# print "\nGorthon Soldier - List of items: %r" % (gs_items)
# print "\nGorthon General - List of items: %r" % (gb_items)

# # Adjust State and check
# # hero.set_health(0)
# # hero.set_alive('n')
# # gorthon_guard.set_health(0)
# # gorthon_guard.set_alive('n')

# Test battle

# a_battle = v1.Fight(hero, gorthon_guard)
# result = a_battle.attack()
# print result

# Test Play
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

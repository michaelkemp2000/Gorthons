# actions.py

from sys import exit
from random import randint
import scenes

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


	# Dictionary of all the different scenes that are looked up
	# by the Engine class to determine what is the next scene.
	scenes = {
		'central_corridor': scenes.CentralCorridor(),
	#	'lwa': scenes.LaserWeaponArmory(),
	#	'the_bridge': scenes.TheBridge(),
	#	'escape_pod': scenes.EscapePod(),
	#	'planet': scenes.Planet(),
		'death': scenes.Death()
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

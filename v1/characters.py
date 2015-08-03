# characters.py

from sys import exit
from random import randint


class State(object):


	# Is a being character alive, in this instance, Hero and Alien.
	def __init__(self, alive, health):
		
		self.alive = alive
		self.health = health

	def check_alive(self):

		if self.alive == True or self.alive == True:
			return True

		elif self.alive == False or self.alive == False:
			return False

		else:
			print "DOES NOT COMPUTE: You fumble around and get shot."
			exit(1)

	def set_alive(self, update):

		self.update = update
		self.alive = self.update

	def check_health(self):

		health = self.health
		return health

	def set_health(self, update):

		self.update = update
		self.health = self.update


class Inventory(object):

	#Dictionary of items that a person can hold.
	def __init__(self):
	
		self.inventory = {}

	# Hero is defined by passing in his health when the object is instanciated.

	def check_contents(self):

		content = self.inventory.items()
		return content

	def check_one(self, item):

		content = self.inventory.get(item)
		return content

	def set_contents(self, iname, ivalue):

		self.iname = iname
		self.ivalue = ivalue
		self.inventory[self.iname] = self.ivalue


class Person(object):


	def __init__(self, alive, health):

		self.alive = alive
		self.health = health
		self.state = State(self.alive, self.health)
		self.inventory = Inventory()

	def check_alive(self):
		
		a_check = self.state.check_alive()
		return a_check

	def set_alive(self, update):

		self.update = update
		self.state.set_alive(self.update)

	def check_health(self):

		h_check = self.state.check_health()
		return h_check

	def set_health(self, update):

		self.update = update
		self.state.set_health(self.update)

	def check_contents(self):

		content = self.inventory.check_contents()
		return content

	def check_one(self, item):

		content = self.inventory.check_one(item)
		return content

	def set_contents(self, iname, ivalue):

		self.iname = iname
		self.ivalue = ivalue
		self.inventory.set_contents(self.iname, self.ivalue)

# Local Module Tests

# Instanciate Character defaults
#hero = Person('y', 100)
#gorthon_guard = Person('y', 50)
#gorthon_soldier = Person('y', 100)
# gorthon_general = Person('y', 200)

# # Set Character Items
# hero.set_contents('weapon', 'laser gun')
# ivalue = "%d%d%d" % (randint(1,9), randint(1,9),
# 									randint(1,9))
# hero.set_contents('passcode', ivalue)
# gorthon_guard.set_contents('weapon', 'laser gun')
# gorthon_soldier.set_contents('weapon', 'laser sword')
# gorthon_general.set_contents('armor', 'battle class')
# gorthon_general.set_contents('weapon', 'laser sword')
# gorthon_general.set_contents('weapon2', 'laser gun')

# # Print Character state
# h_state = hero.check_alive()
# h_health = hero.check_health()
# gg_state = gorthon_guard.check_alive()
# gg_health = gorthon_guard.check_health()
# gs_state = gorthon_soldier.check_alive()
# gs_health = gorthon_soldier.check_health()
# gb_state = gorthon_general.check_alive()
# gb_state = gorthon_general.check_health()


# print "\nHero: [%s] - %s" % (h_state, h_health)
# print "\nGorthon Guard: [%s] - %s" % (h_state, h_health)
# print "\nGorthon Soldier: [%s] - %s" % (h_state, h_health)
# print "\nGorthon General: [%s] - %s" % (h_state, h_health)

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
# hero.set_health(0)
# hero.set_alive('n')
# gorthon_guard.set_health(0)
# hero.set_alive('n')














		

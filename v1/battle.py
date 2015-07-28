# battle.py

# Now import your v1 Package.
from characters import Person
from sys import exit
from random import randint

class Fight(object):

	def __init__(self, ch1, ch2):

		self.ch1 = ch1
		self.ch2 = ch2

	def attack(self):

		state1 = Person.check_alive(self.ch1)
		health1 = Person.check_health(self.ch1)
		state2 = Person.check_alive(self.ch2)
		health2 = Person.check_health(self.ch2)
		return ": %s ... %s ... %s ... %s ..." % (state1, health1, state2, health2)

# Test

#hero = Person('y', 100)
# gorthon_guard = Person('y', 50)
# gorthon_soldier = Person('y', 100)
# gorthon_general = Person('y', 200)

# a_battle = Fight(hero, gorthon_guard)
# result = a_battle.attack()
# print result

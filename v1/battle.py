# battle.py

# Now import your v1 Package.
from characters import Person
from sys import exit
from random import randint

class Weapons(object):

	def __init__(self):

		self.arsenal = {
					'laser gun': randint(1,4), 
					'laser sword': randint(3,7),
					'plasma cannon': randint(6,15),
					'neutron bomb': 100000
					}

	def get_hp(self, weapon):

		self.weapon = weapon
		hp = self.arsenal.get(self.weapon)
		return hp



class Fight(object):


	def __init__(self, ch1, ch2):

		self.ch1 = ch1
		self.ch2 = ch2

	def attack(self):

		arsenal = Weapons()
		#state1 = Person.check_alive(self.ch1)
		health1 = Person.check_health(self.ch1)
		#state2 = Person.check_alive(self.ch2)
		health2 = Person.check_health(self.ch2)
		items1 = self.ch1.check_one('weapon')
		damage1 = arsenal.get_hp(items1)
		items2 = self.ch2.check_one('weapon')
		damage2 = arsenal.get_hp(items2)

		#  return ": %s ... %s ... %s ... %s ... %d ... %d" % (state1, health1, state2, health2, damage1, damage2)
		
		while Person.check_alive(self.ch1) == True and Person.check_alive(self.ch2) == True:
			whoFirst = randint(1,2)

			if whoFirst == 1:
				if items1 == 'laser gun':
					print "zap: you shoot you\'re laser Gun and deliver [-%d] hit point!" % damage1
					health2 = Person.check_health(self.ch2)
					health2 = health2 - damage1
					self.ch2.set_health(health2)
					print health2
				
				elif items1 == 'laser sword':
					print "zap: you slash you\'re laser sword and deliver [-%d] hit point!" % damage1
					health2 = Person.check_health(self.ch2)
					health2 = health2 - damage1
					self.ch2.set_health(health2)
					print health2

				elif items1 == 'plasma cannon':
					print "zap: you boom you\'re plasma cannon and deliver [-%d] hit point!" % damage1
					health2 = Person.check_health(self.ch2)
					health2 = health2 - damage1
					self.ch2.set_health(health2)
					print health2

				else:
					print "You use your fists and die!"
					exit(1)

			elif whoFirst == 2:
				if items2 == 'laser gun':
					print "Ahrrg: you\'re hit from a laser gun and recieve [-%d] hit damage!" % damage2
					health1 = Person.check_health(self.ch1)
					health1 = health1 - damage2
					self.ch1.set_health(health1)
					print health1
				
				elif items2 == 'laser sword':
					print "Ahrrg: you\'re slashed from a laser gun and recieve [-%d] hit damage!" % damage2
					health1 = Person.check_health(self.ch1)
					health1 = health1 - damage2
					self.ch1.set_health(health1)
					print health1

				elif items2 == 'plasma cannon':
					print "Ahrrg: you\'re badly hit from a plasma cannon blast"
					print " and recieve [-%d] hit point!" % damage2
					health1 = Person.check_health(self.ch1)
					health1 = health1 - damage2
					self.ch1.set_health(health1)
					print health1

				else:
					print "You use your fists and die!"
					exit(1)

			else:
				print "You stare each other out and die of starvation"
				exit(1)

			if health1 <= 0:
				self.ch1.set_alive(False)

			elif health2 <= 0:
				self.ch2.set_alive(False)

			elif health1 > 0:
				self.ch1.set_alive(True)

			elif health2 > 0:
				self.ch2.set_alive(True)

			else:
				print "error"


		if health1 <= 0:
			print "enemy"

		elif health2 <= 0:
			return "hero"

		else:
			return "error"


# Local Module Tests

# hero = Person('y', 100)
# gorthon_guard = Person('y', 50)
# gorthon_soldier = Person('y', 100)
# gorthon_general = Person('y', 200)
# hero.set_contents('weapon', 'plasma cannon')
# gorthon_guard.set_contents('weapon', 'laser gun')
# hero.set_alive(True)
# gorthon_guard.set_alive(True)

# a_battle = Fight(hero, gorthon_guard)
# result = a_battle.attack()
# print result

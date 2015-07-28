# start.py

# Now import your v1 Package.
import v1
from sys import exit
from random import randint

# ------------------------Module tests------------------------------------------

# Instanciate Character defaults
hero = v1.Person('y', 100)
gorthon_guard = v1.Person('y', 50)
gorthon_soldier = v1.Person('y', 100)
gorthon_general = v1.Person('y', 200)

# Set Character Items
hero.set_contents('weapon', 'laser gun')
ivalue = "%d%d%d" % (randint(1,9), randint(1,9),
									randint(1,9))
hero.set_contents('passcode', ivalue)
gorthon_guard.set_contents('weapon', 'laser gun')
gorthon_soldier.set_contents('weapon', 'laser sword')
gorthon_general.set_contents('armor', 'battle class')
gorthon_general.set_contents('weapon', 'laser sword')
gorthon_general.set_contents('weapon2', 'laser gun')

# Print Character state
h_state = hero.check_alive()
h_health = hero.check_health()
gg_state = gorthon_guard.check_alive()
gg_health = gorthon_guard.check_health()
gs_state = gorthon_soldier.check_alive()
gs_health = gorthon_soldier.check_health()
gb_state = gorthon_general.check_alive()
gb_state = gorthon_general.check_health()


print "\nHero: [%s] - %d" % (h_state, h_health)
print "\nGorthon Guard: [%s] - %d" % (h_state, h_health)
print "\nGorthon Soldier: [%s] - %d" % (h_state, h_health)
print "\nGorthon General: [%s] - %d" % (h_state, h_health)

# Print Character items
h_items = hero.check_contents()
gg_items = gorthon_guard.check_contents()
gs_items = gorthon_soldier.check_contents()
gb_items = gorthon_general.check_contents()
print "\nHero - List of items: %r" % (h_items)
print "\nGorthon - List of items: %r" % (gg_items)
print "\nGorthon Soldier - List of items: %r" % (gs_items)
print "\nGorthon General - List of items: %r" % (gb_items)

# Adjust State and check
hero.set_health(0)
hero.set_alive('n')
gorthon_guard.set_health(0)
gorthon_guard.set_alive('n')

# Test battle

a_battle = v1.Fight(hero, gorthon_guard)
result = a_battle.attack()
print result
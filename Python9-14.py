#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-14 Dice

from random import randint

print("\n#9-14 Dice\n")

class Die:
	def __init__(self, sides):
		self.sides = sides
	def roll_die(self):
		roll = randint(1, self.sides)
		return roll
	def get_sides(self):
		return self.sides

die1 = Die(6)
die2 = Die(10)
die3 = Die(20)
x = 1
y = 1
z = 1

print("die1 is a", str(die1.get_sides()) + "-sided die.")
print("die1 Rolling:")
while x <= 10:
	print("Roll", str(x) + ":", die1.roll_die())
	x += 1
print()
print("die2 is a", str(die2.get_sides()) + "-sided die.")
print("die2 Rolling:")
while y <= 10:
	print("Roll", str(y) + ":", die2.roll_die())
	y += 1
print()
print("die3 is a", str(die3.get_sides()) + "-sided die.")
print("die3 Rolling:")
while z <= 10:
	print("Roll", str(z) + ":", die3.roll_die())
	z += 1
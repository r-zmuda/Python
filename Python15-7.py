#Ryan Zmuda
#SOFT 204 Open Source Programming
#15-7 Two D8s

#Imports
import pygal
from random import randint

#Class Definitions
class Die():
	def __init__(self, sides=6):
		self.num_sides = sides
	def roll(self):
		return randint(1, self.num_sides)

#Create two D6 dice
die_1 = Die(8)
die_2 = Die(8)

#Make rolls
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize
hist = pygal.Bar()
hist.title = "Results of rolling two D8 dice 1000 times"
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency"
hist.add("Frequencies", frequencies)
hist.render_to_file("dice_visual.svg")
print("Histogram exported as dice_visual.svg.")
print("Program finished.")
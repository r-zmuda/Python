#Ryan Zmuda
#SOFT 204 Open Source Programming
#15-4 Modified Random Walks

#Imports
import matplotlib.pyplot as plt
from random import choice

#Filter Warnings
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

#Class Definitions
class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]
	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distance
			
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distance
			
			if x_step == 0 and y_step == 0:
				continue
			
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)

#Program Loop
while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	#Set size of plotting window
	plt.figure(dpi=256, figsize=(2, 2))
	
	#Draw scatter plot
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor="none", s=1)
	
	#Emphasize the first and last points
	plt.scatter(0, 0, c="blue", edgecolors="none", s=2)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=2)
	
	#Remove axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	#Show window
	plt.show()
	
	#Again?
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == "n":
		break
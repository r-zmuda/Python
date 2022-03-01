#Ryan Zmuda
#SOFT 204 Open Source Programming
#15-1 Cubes

#Imports
import matplotlib.pyplot as plt

#Draw scatter plot
x_values = list(range(1, 5001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, edgecolor="none", s=2)

#Labels
plt.title("Cubes", fontsize=12)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cubes of Value", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=6)

#plt.savefig("cubes_plot.png", bbox_inches="tight")
plt.show()
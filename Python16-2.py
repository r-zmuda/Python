#Ryan Zmuda
#SOFT 204 Open Source Programming
#16-2 Sikta-Death Valley Comparison

#Imports
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#Functions
def get_data(filename, dates, highs, lows):
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		missingData = 0
		print("\nParsing", filename + ":")
		for row in reader:
			try:
				current_date = datetime.strptime(row[0], "%Y-%m-%d")
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(current_date, "is missing data.")
				missingData += 1
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)
		print("Parsing finished with", missingData, "error(s).")
def plot_data(dates, highs, lows, a, b):
	plt.plot(dates, highs, c="red", alpha=a)
	plt.plot(dates, lows, c="blue", alpha=a)
	plt.fill_between(dates, highs, lows, facecolor="blue", alpha=b)

#Get dates, high, low temps, and plot them
fig = plt.figure(dpi=128, figsize=(8, 4))
dates, highs, lows = [], [], []
get_data("sitka_weather_2014.csv", dates, highs, lows)
plot_data(dates, highs, lows, 0.5, 0.2)
dates, highs, lows = [], [], []
get_data("death_valley_2014.csv", dates, highs, lows)
plot_data(dates, highs, lows, 0.3, 0.1)

#Format plot
title = "Daily high/low temps - 2014"
title += "\nDeath Valley, CA vs. Sitka, AK"
plt.title(title, fontsize=8)
plt.xlabel(" ", fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=8)
plt.tick_params(axis="both", which="major", labelsize=8)
plt.show()
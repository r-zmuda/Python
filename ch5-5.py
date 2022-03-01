# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-5 Alien Colors #3

# Switch between versions (1, 2, or 3)
VERSION = 1

print("#5-5 Alien Colors #3")
print("Version: " + str(VERSION) + "\n")

points = 0

if VERSION == 1:
    alien_color = 'green'
elif VERSION == 2:
    alien_color = 'yellow'
elif VERSION == 3:
    alien_color = 'red'
else:
    alien_color = 'colorless'

if alien_color == 'green':
    points += 5
    print("You got 5 points.")
elif alien_color == 'yellow':
    points += 10
    print("You got 10 points.")
else:
    points += 15
    print("You got 15 points.")

print("\nPoints: " + str(points))

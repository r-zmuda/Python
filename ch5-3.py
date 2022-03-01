# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-3 Alien Colors #1

# Switch between versions (1 or 2)
VERSION = 1

print("#5-3 Alien Colors #1")
print("Version: " + str(VERSION) + "\n")

points = 0

if VERSION == 1:
    alien_color = 'green'
elif VERSION == 2:
    alien_color = 'red'
else:
    alien_color = 'colorless'

if alien_color == 'green':
    points += 5
    print("You got 5 points.")
    
print("\nPoints: " + str(points))

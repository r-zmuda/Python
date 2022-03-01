#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#8-14 Cars

print("\n#8-14 Cars")
cars = []
def make_car(manufacturer, model, **features):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in features.items():
        car[key] = value
    return car
cars.append(make_car("suburu", "outback", year="2009",
    color="blue", tow_package=True))
cars.append(make_car("honda", "civic", year="2010",
    color="black", tow_package=False))
cars.append(make_car("mazda", "3", year="2018",
    color="red", tow_package=False))
cars.append(make_car("nissan", "versa", year="2012",
    color="gray", tow_package=True))
for car in cars:
    print(car)
#Ryan Zmuda
#SOFT 204 Open Source Programming
#16-6 Gross Domestic Product
#Based on world_population.py

#Imports
import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

#Functions
def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

#Load json
filename = "global_gdp.json"
with open(filename) as f:
	gdp_data = json.load(f)

#Collect data
cc_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict["Year"] == "2014":
		country_name = gdp_dict["Country Name"]
		gdp = int(float(gdp_dict["Value"]))
		code = get_country_code(country_name)
		if code:
			cc_gdp[code] = gdp / 1000000000

#Draw map
wm_style = RS("#336699", base_style=LCS)
wm = World(style=wm_style)
wm.title = "Global GDP in 2014, by Country (in billions USD)"
wm.add("Global GDP (in billions USD)", cc_gdp)
wm.render_to_file("global_gdp.svg")

#Show number of countries, confirmation
print("Loaded data for", len(cc_gdp), "countries.")
print("Map exported as global_gdp.svg.")
print("Program finished.")
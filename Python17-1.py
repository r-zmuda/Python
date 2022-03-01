#Ryan Zmuda
#SOFT 204 Open Source Programming
#17-1 Other Languages

#Imports
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Bool
got_lang = False

#Program loop
while True:
	#Get valid language, API call
	while got_lang == False:
		print("\nEnter language in lower case (e.g. python, c, java, perl).")
		language = input("language = ")
		url = "https://api.github.com/search/repositories?q=language:"
		url += language + "&sort=stars"
		r = requests.get(url)
		print("Status Code:", r.status_code)
		if r.status_code == 200:
			got_lang = True
		else:
			print("ERROR: Invalid language.")
	response_dict = r.json()
	print("Total Repositories:", response_dict["total_count"])
	repo_dicts = response_dict["items"]
	print("Items Returned:", len(repo_dicts))

	#Populate lists (repo_dict["description"] is causing AttributeError)
	#Descriptions with URLs, emojis, etc. probably messing the code.
	names, plot_dicts = [], []
	for repo_dict in repo_dicts:
		names.append(repo_dict["name"])
		plot_dict = {
			"value": repo_dict["stargazers_count"],
			#"label": repo_dict["description"],
			"xlink": repo_dict["html_url"]
		}
		plot_dicts.append(plot_dict)

	#Format chart
	style = LS("#333366", base_style=LCS)
	chart_config = pygal.Config()
	chart_config.x_label_rotation = 45
	chart_config.title_font_size = 48
	chart_config.label_font_size = 24
	chart_config.major_label_font_size = 36
	chart_config.truncate_label = 16
	chart_config.width = 1000

	#Draw chart
	chart = pygal.Bar(chart_config, style=style, show_legend=False)
	chart.title = "Most Starred " + language.title() + " Projects on GitHub"
	chart.x_labels = names
	chart.add("", plot_dicts)

	#Save chart
	chart.render_to_file(language + "_repos.svg")
	print("Chart exported as " + language + "_repos.svg.")
	
	#Again?
	answer = input("Run again? ('n' to quit): ")
	if answer == "n":
		break
	got_lang = False

#End program
print("Program finished.")
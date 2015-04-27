from django import template
from velgbedre.settings import BASE_DIR, STATIC_URL
import os, os.path

register = template.Library()

@register.simple_tag
def load_scss():
	scss_folder = os.path.join(BASE_DIR, "staticfiles/scss")
	scss_files = os.listdir(scss_folder)

	out = []
	for file in scss_files:
		if file != '.DS_Store':
			path = STATIC_URL + "scss/" + file
			link = r'<link rel="stylesheet" type="text/x-scss" href="{}" />'.format(path)
			out.append(link)

	return "\n".join(out)
from django import template
from velgbedre.settings import BASE_DIR, STATIC_URL
from django.core.urlresolvers import reverse
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

@register.simple_tag
def add_active(request, name, by_path=False):
    """ Return the string 'active' current request.path is same as name
    
    Keyword aruguments:
    request  -- Django request object
    name     -- name of the url or the actual path
    by_path  -- True if name contains a url instead of url name
    """
    if by_path:
        path = name
    else:
        path = reverse(name)

    if request.path == path:
        return ' active '

    return ''
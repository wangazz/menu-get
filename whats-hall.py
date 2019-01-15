# https://meals.some.ox.ac.uk/pallmenu.php

from lxml import html
import requests

page = requests.get('https://meals.some.ox.ac.uk/pallmenu.php', auth=('some3985','********'))
tree = html.fromstring(page.content)
print(page.content)

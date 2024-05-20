# import re
# from colorama import Fore
# import requests

# website = "https://www.dia.es/"

# # Otenemos una respuesta de la url
# resultado = requests.get(website)
# content = resultado.text

# print(content)

import requests
print(requests.get("https://www.youtube.com/").text)
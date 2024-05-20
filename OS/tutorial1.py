# from twilio.rest import Client

# account_sid = 'AC3528c46e5d5eedab9ac3e95250a90988'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   to='whatsapp:+34640604543'
# )

# print(message.sid)

# from twilio.rest import Client

# account_sid = 'AC3528c46e5d5eedab9ac3e95250a90988'
# auth_token = 'ae8c4df7032338d0d2bf4a509284b246'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='hOLA COMPADRE',
#   to='whatsapp:+34640604543'
# )

# print(message.sid)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'C:/Users/sergi/Desktop/chromedriver.exe')
driver = webdriver.Chrome()
input("Esperando que no se cierre webdriver: ")
url = "https://www.google.es/"
driver.get(url)
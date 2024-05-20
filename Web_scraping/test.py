import requests

# URL del servidor local
url = 'http://127.0.0.1:5000/sergi'

# Definir los parámetros de consulta
params = {
    'name': 'sergi',
    'age': 26
}

# Hacer la solicitud GET con los parámetros
response = requests.get(url, params=params)

# Mostrar la URL completa con los parámetros
print(response.url)

# Comprobar el estado de la respuesta
if response.status_code == 200:
    # Mostrar el contenido de la respuesta
    print(response.json())
else:
    print(f'Error: {response.status_code}')
import requests
data = '2000-11-11'

resultado = requests.get('https://api.nasa.gov/planetary/apod?api_key=asyJpgx11PR09hCxWjIdH308gCP4n5LSwIn1cxpX&date={}'.format(data))
print(resultado.json())
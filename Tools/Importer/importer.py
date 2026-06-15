import requests

URL = "https://2shankz.github.io/optc-db.github.io/"

response = requests.get(URL)

print(response.status_code)

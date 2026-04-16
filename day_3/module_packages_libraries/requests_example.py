import requests

response_bbc = requests.get('https://www.bbc.com')

print(response_bbc.status_code)

print(response_bbc.content)
import requests

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
print("Status code:", response.status_code)
print("Raw response:", response.text)

print(response.json())
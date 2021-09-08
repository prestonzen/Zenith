import requests

ip = requests.get("https://api.ipify.org")

print(ip.text)
import requests

# Utiliser un service web pour obtenir l'adresse IP publique
response = requests.get('https://api.ipify.org?format=json')
ip_data = response.json()
print(f"Adresse IP publique : {ip_data['ip']}")

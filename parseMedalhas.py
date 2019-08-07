import requests

r = requests.get(url='https://snippets.r7.com/snippet/5d1fba47bbb3eb7f21000011')

with open('medalhas.txt', 'w') as f:
    for pais in r.json()["itens"]:
        f.write(f"{pais['countryName']},{pais['medalGold']},{pais['medalSilver']},{pais['medalbronze']}\n")
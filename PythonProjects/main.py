import requests # подключение библиотеки
token='58db7a28f15592e9a5d9376cb6e220c5'
base_url='https://pokemonbattle.me:9104/' # переменные

response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token': token}, json={
 "name": "Ron",
 "photo": "https://dolnikov.ru/pokemons/albums/048.png"})
print(response_add_pokemon.json)# вывод ответа, создание покемона


response_change_pokemon = requests.put(f'{base_url}pokemons', headers={'trainer_token': token}, json={
 
    "pokemon_id": "9810",
    "name": "Bri", # новое имя
    "photo": "https://dolnikov.ru/pokemons/albums/048.png"

 })
print(response_change_pokemon.json) # изменение имени покемона


response_add_pokball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token': token}, json={
 
     "pokemon_id": "9810"
 })
print(response_add_pokball.json) # добавление в покебол
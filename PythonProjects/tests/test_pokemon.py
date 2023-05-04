import requests
import pytest
def test_status_code():
    token = '58db7a28f15592e9a5d9376cb6e220c5'
    response = requests.get('httpS://pokemonbattle.me:9104/trainers', headers={'trainer_token' : token}, 
    )
    assert response.status_code == 200
  

def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 4263})
    assert response.json()['trainer_name'] == 'Born'

    
    
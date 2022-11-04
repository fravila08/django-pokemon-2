from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

# Create your views here.
def homepage(request):
    data={
        "types":["fire", 'water', 'electric', 'grass', 'ground', 'psychic', 'ghost', 'fairy']
    }
    return render(request, "pages/index.html", data)

def teamType(request, type):
    answer=[]
    pokemonByType=requests.get(f"https://pokeapi.co/api/v2/type/{type}/")
    pokemonByType=pokemonByType.json()
    def get_pokemon_url():
        randInt=random.randint(1,35)
        trueUrl=pokemonByType['pokemon'][randInt]["pokemon"]['url']
        return trueUrl
    def get_info(url):
        almost={}
        newPokemon=requests.get(f"{url}")
        newPokemon=newPokemon.json()
        almost["name"]=newPokemon["name"]
        almost['img']=newPokemon["sprites"]["front_default"]
        return almost
    for i in range(6):
        my_url=get_pokemon_url()
        mydic= get_info(my_url)
        answer.append(mydic)
    
    data={
        "info": type,
        "myPokemon": answer
    }
    return render(request, "pages/team.html", data)

def showItems(request):
    return HttpResponse(" Items Page")
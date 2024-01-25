#text styling library
from colorama import Fore
#comunication library
import requests
#library to analyze
from bs4 import BeautifulSoup
from collections import namedtuple

website = "https://store.steampowered.com/app/582010"
juegos = ["422970","526870","582010"]
r= requests.get(website)
resultado = r.text
content = BeautifulSoup(resultado,'html.parser')
juego = content.find_all('div',class_="game_area_purchase_game_wrapper")
print(juego)
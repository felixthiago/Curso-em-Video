import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 73 === Tuplas com Times de Futebol
##### Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

from cursoemvideo.utils import *
clear()


times = ("Palmeiras", "SãoPaulo", "Bragantino", "Chapecoense", "Ceará", "Cruzeiro", "Bahia", "Internacional", "Corinthians", "Vasco",
         "Juventude", "Mirassol", "Fortaleza", "Vitória", "Grêmio", "Fluminense", "Santos", "Sport", "Coritiba", "Ferroviaria")


print(f"{cer}Veja a lista de times no brasileirão > {times}")
print(f"{cer}Os 4 Ultimos times da tabela do brasileirão em ordem > {times[len(times)- 4:]}")
print(f"{cer}Os 4 Primeiros times da tabela do brasileirão em ordem > {times[:4]}")
print(f"{cer}Aqui estão os times em ordem alfabética > {sorted(times)}")
print(f"{cer}O Chapecoense está na {times.index('Chapecoense') + 1}° Posição")
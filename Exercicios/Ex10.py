######## Nivel: Simples 
######## Exercicio === Maior e Menor sequencia
######## Descrição: "Recebe uma lista de idades dadas pelo usuario e verifica a maioridade de todas as pessoas"
####### Módulo finalizado em Março de 2021

from vars import *
try:
    inputs_qtd = int(input(f'{choice}Quantas pessoas deseja pesar? > '))
except:
    print(f'{err} O que foi digitado não se parece com um número! ')
    quit()

p = []

for inp in range(inputs_qtd):
    user_input = float(input(f'{strTime} Digite o peso da {inp + 1}° Pessoa > '))
    p.append(user_input)
print(f'{cer} A pessoa mais gorda dessa lista pesa {max(p)}KG ')
print(f'{cer} A pessoa mais magra dessa lista pesa {min(p)}KG ')


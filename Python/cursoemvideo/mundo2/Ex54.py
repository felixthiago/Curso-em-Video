import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Maior e Menor sequencia
######## Descrição: "Recebe uma lista de idades dadas pelo usuario e verifica a maioridade de todas as pessoas"

from cursoemvideo.utils import *

inputs_qtd = safe_int_input(f'{choice}Quantas pessoas deseja pesar? > ')

p = []

for inp in range(inputs_qtd):
    user_input = safe_float_input(f'{strTime} Digite o peso da {inp + 1}° Pessoa > ')
    p.append(user_input)
print(f'{cer} A pessoa mais gorda dessa lista pesa {max(p)}KG ')
print(f'{cer} A pessoa mais magra dessa lista pesa {min(p)}KG ')


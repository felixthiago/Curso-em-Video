import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Criando um Menu de Opções
######## Descrição: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

from Exercicios.utils import *
clear()


def menu():
    try:
        n1 = int(input(f"{strTime} Digite o primeiro número > "))
        n2 = int(input(f"{strTime} Digite o segundo número > "))

        choices = [1, 2, 3, 4, 5]
        choice = int(input((f"""
    {strTime}Seja bem vindo ao menu de opções!
                Escolha uma das opções abaixo
                        {a}[ {la}1{a} ] {b}Somar{reset}
                        {a}[ {la}2{a} ] {b}Multiplicar{reset}
                        {a}[ {la}3{a} ] {b}Maior{reset}
                        {a}[ {la}4{a} ] {b}Novos números{reset}
                        {a}[ {la}5{a} ] {b}Sair do programa{reset}
                > """)))

        while choice not in choices:
            choice = int(input(f"{err} Opção inválida! Digite novamente: "))

    except ValueError:
        print(f'{err} O que foi digitado não se parece com um número! ')
        quit()

    if choice == 1:
        soma = n1 + n2
        print(f'{strTime} A soma entre {n1} e {n2} é == {cer}{soma}')

    elif choice == 2:
        multiplicacao = n1 * n2
        print(f'{strTime} A multiplicação entre {n1} * {n2} é == {cer}{multiplicacao}')

    elif choice == 3: 
        if n1 > n2:
            print(f'{strTime} O maior número é {cer}{n1}')
        elif n2 > n1:
            print(f'{strTime} O maior número é {cer}{n2}')
        else:
            print(f'{strTime} Os números são iguais!') 

    elif choice == 4:
        try:
            n1 = int(input(f'{strTime} Atualize o primeiro número > '))
            n2 = int(input(f'{strTime} Atualize o segundo número > '))
        except ValueError:
            print(f'{err} O que foi digitado não se parece com um número! ')
            quit()
        print(f'{strTime} Os números foram atualizados para {cer}{n1} e {n2}')

    elif choice == 5:
        print(f'{strTime} Saindo do programa...')
        quit()
if __name__ == '__main__':
    try:
        while True:
            menu()
    except KeyboardInterrupt:
        print(f"\n\n{err}{Fore.RED}C^")
        quit()
        
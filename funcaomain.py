#1° parte do codigo
import random

#2° criar estruturas de dados e as funcoes de suporte
def aleatorio(n1, n2):
    return print(f'o numero aleatorio é: {random.randint(n1, n2)}')

#3° criando a funcao principal
def main():
    n1 = int(input("digite o 1° numero:"))
    n2 = int(input('digite o 2° numero:'))
    aleatorio(n1, n2)

#4° executacao da funcao principal
if __name__== "__main__":
    main()
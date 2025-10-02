import random


pokemons ={
    'charmander':{'ataque':'bola de fogo', 'dano' : 35},
    'squirtle':{'ataque':'jato de agua', 'dano' : 33},
    'bulbassauro':{'ataque':'chicote de vinha', 'dano' : 31}
}



def selecionar_poke1():
    print("selecione seu pokemon".center(40,'-'))
    pokemon= input('(1) charmander\n(2) squirtle\n(3) bulbassauro')
    print('_'*40)
    escolha= int (input('escolha seu pokemon (1,2 ou 3)'))
    if escolha == 1 :
        escolha ='charmander' #se a escolha for 1 -> charmander
    if escolha == 2 :
        escolha ='squirtle'   #se a escolha for 2 -> squitle
    if escolha == 3 :
        escolha ='bulbassauro' #se a escolha for 3 -> bulbassauro


selecionar_poke1()

def fichahabilidades(escolha):
    print(' FICHA HABILIDADES' .center)
    print(escolha)
    

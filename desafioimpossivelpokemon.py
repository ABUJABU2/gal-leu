import random


pokemons ={
    'charmander':{'ataque':'bola de fogo', 'dano' : 35,'vida':100},
    'squirtle':{'ataque':'jato de agua', 'dano' : 33,'vida':100},
    'bulbassauro':{'ataque':'chicote de vinha', 'dano' : 31,'vida':100}
}

jogador1 = ''
jogador2 = ''

def selecionar_poke1(jogador):
    print("selecione seu pokemon📍".center(40,'-'))
    pokemon= input('(1) charmander\n(2) squirtle\n(3) bulbassauro')
    print('_'*40)
    escolha= int (input('escolha seu pokemon✅ (1,2 ou 3)'))
    if escolha == 1 :
        escolha ='charmander' #se a escolha for 1 -> charmander
    elif escolha == 2 :
        escolha ='squirtle'   #se a escolha for 2 -> squitle
    elif escolha == 3 :
        escolha ='bulbassauro' #se a escolha for 3 -> bulbassauro
    else:
        print(f'seu burro, é para selecionar 1,2 ou 3 seu idiotaaa🧠🧠🧠❌❌❌(se vc for o vitor, seu autistaa🧠🧠🧠❌❌❌)')

    return escolha

escolha1 = selecionar_poke1(jogador1)
escolha2 = selecionar_poke1(jogador2)

def fichahabilidades(escolha):
    print(f'FICHA DE HABILIDADES📋' .center(40,'—'))
    print(f'ataque 💥: {pokemons[escolha]['ataque']} Dano 💯: {pokemons[escolha]['dano']}') #o primeiro '[]' retorna ao pokemon q o jogador escolheu e o segundo'[]'
                                                                                       #retorna ao criterio q voce escolheu ex: 'ataque' , 'dano'
fichahabilidades(escolha1)
print('_'*40)
fichahabilidades(escolha2)
print('_'*40)
def dano_crítico (escolha):
    dano_crítico = pokemons[escolha]['dano'] * random.uniform(1,2)
    print(f' O dano crítico💯 do {escolha} é de {dano_crítico:.2f}')
    print('_'*40)
    return dano_crítico

d1 = dano_crítico(escolha1)
d2 = dano_crítico(escolha2)

#CRIEM UMA FUNCAO CHAMADA BATALHA (DANOCRITICO1 E DANOCRITICO2)
#CADA POKEMON TEM 100 DE VIDA 
#NO FINAL MOSTRE O VENCEDOR

def batalha(d1 , d2):

    vida1 = 100
    vida2 = 100

    print(f" UMA BATALHA SE INICIOU! ".center(40,'-'))
    print('_'*40)

    while vida1 or vida2 >0:
        d1 = dano_crítico(escolha1)
        d2 = dano_crítico(escolha2)
    vida1-=0
    vida2-=0 

    escolha22= int (input('vez do jogador 1 (digite atacar para atacar)'))
    if escolha22 == 'atacar' :
        print(f'{pokemons[escolha1]} usou {pokemons[escolha1]['ataque']}')
        escolha22 =vida1  - d2
    escolha22= int (input('vez do jogador 2 (digite atacar para atacar)'))
    if escolha22 == 'atacar' :
        print(f'{pokemons[escolha2]} usou {pokemons[escolha2]['ataque']}')
        escolha22 = vida2 - d1
    

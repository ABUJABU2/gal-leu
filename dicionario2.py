lojajogos ={
    'minecrack' : {'preco': 9.90 , 'estoque' : 5},
    'bomba' : {'preco' : 19.101 , 'estoque' :3},
    'godpeace' : { 'preco' : 149.90 , 'estoque' : 4}
}
carrinho ={}


print(lojajogos['bomba']['preco'])

#indexacao de dicionarios de dicionarios

for jogo, info in lojajogos.items():
    print(f' {jogo} - {info['preco']} - estoque: {info["estoque"]}')



print("-" * 50)

while True:

    escolha_cliente = input("qual jogo voce deseja? (digite sair pre finalizar ) : ").strip()
    if escolha_cliente=='sair':
        break


    if escolha_cliente in lojajogos:
        print("o jogo esta disponivel")
        quantidade_solicitada = int(input("quantas unidades vc quer? : "))
        if quantidade_solicitada > lojajogos[escolha_cliente]["estoque"]:
            print("não tem estoque suficiente")
        else: #cenário onde tem estoque disponivel, vamos subtrair a quantidade do dicionário loja jogos
            print("o jogo não esta disponivel")
            lojajogos[escolha_cliente]['estoque'] -=  quantidade_solicitada
            carrinho[escolha_cliente] = quantidade_solicitada

    else:
        print("o jogo nao esta disponivel")


    print(carrinho)
    print(f'o estoque atual do jogo escolhido é: {lojajogos[escolha_cliente]['estoque']}')

total = 0
print('RESUMO DA COMPRA'.center(40,'-'))
for jogo, qtd in carrinho.items():
    preco = lojajogos[jogo]['Preco']
    total += preco * qtd
    print(f'{jogo}  x{qtd} estoque'.center(40))
print('-'*40)
print(f'Total: R$ {total}'.center(40))



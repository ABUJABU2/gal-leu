'''-----------------------------------------------------MÉTODOS DE LISTA-------------------------------------------------------------------------------------
método .append(elemento a adicionar) adiciona um elemento no final da lista
crie uma lista com as frutas banana maça e morango'''

lista_frutas = ['banana' , 'maça','morango']
lista_frutas.append('kiwi')
print(lista_frutas)

'''método .insert , adiciona um elemento em uma posiçao específica
insira a pera na primeira posição'''

lista_frutas.insert(0 , 'pera')
print(lista_frutas)

'''metodo .remove('coisa da lista') , ele remove um elemento especifico
agora remova a banana'''

lista_frutas.remove('banana')
print(lista_frutas)


lista_idades = [33,11,13,19,42]

'''método .sot() , ele organiza uma lista em ordem alfabética ou numérica
agora organize em ordem crescente'''
lista_idades.sort(reverse=False)
print(lista_idades)

'''se você quiser fazer em ordem crescente faça .sort(reverse=True)'''

lista_idades.sort(reverse=True)
print(lista_idades)

'''método .reverse() ele reverte a ordem da lista, porém não a organisa
agora reverta a lista_idades'''

lista_idades.reverse()
print(lista_idades)

lista_frutas2 = ['banana' , 'maça','morango','banana','banana']

'''método .count(item procurado) , ele conta o número de vezes q um item aparece na lista 
quantas vezes a banana foi repetida? Use o .count para descobrir 💀💀💀'''

print(lista_frutas2.count('banana'))
#criem uma variavel q chama texto
#escrevam de maneira zuada :c00lKiDd     ->armazenem a frase na variavel
texto= '   ViniCius É uM toLeTe nO forSaKEN'
#vou usar comando para mudar o texto da variável texto

#método .cpitalize
print(texto.capitalize())

#metodo.title  ->coloca em maiuscula a primeira letra de toda palavra
print(texto.title())

#metodo .center(numero,caracter)
nome = 'mafioso'
print(nome.center(40, '-'))

#metodo len(variaveltexto)   ->ele vai contarquantos caracterespossui uma frase
print(len(texto))

#metodo .lower()   ->ele vai colocar todas as letras em minusculas
print(texto.lower())

#metodo .upper()   ->ele vai deixar tudo em maiusculo
print(texto.upper())

#metodo .replace('palavra antiga' , 'palavra nova')
frase = 'abujabu é ruim no forsaken e o vininini e um coco'
print(frase.replace('ruim','bom'))
#MÉTODO .strip ---->remove os expacos iniciais e os finais
print(texto.strip())

print(texto.lower().strip().replace('um tolete','o pior jogador'))

pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]
somaentregues=[]
print('produtos entregues' .center(40,'-'))
for i in pedidos:
    if i[3]=='Entregue':
        print(f'-{i[0]}')


for i in pedidos:
    if i[3]=='Entregue':
        somaentregues.append(i[2])
        soma=sum(somaentregues)
print(f'soma:{soma}')



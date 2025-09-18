nome = input("digite o seu nome: ")
listanotas = input("qual são suas notas mais recentes")


def mediadenotas(listanotas):
    media = sum(listanotas)/len(listanotas)
    return print(f'a média das notas é:{media}')

mediadenotas(listanotas)



def main():
    if mediadenotas >= 9:
        print(f'parabens{nome}, voce tem notas otimas')
    if mediadenotas >=7 and <=











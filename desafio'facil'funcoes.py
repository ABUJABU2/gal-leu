nome = input("digite o seu nome: ")
listanotas = input("qual são suas notas mais recentes:")


def mediadenotas(listanotas):
    media = sum(listanotas)/len(listanotas)
    return print(f'a média das notas é:{media}')

mediadenotas(listanotas)



def main():
    if mediadenotas >= 9:
        print(f'parabens{nome}, voce tem notas otimas')
    if mediadenotas >= 7 and mediadenotas<=8:
        print(f"voce está na média,{nome}")
    if mediadenotas >= 5 and mediadenotas<=6.9:
        print(f"voce está na média,{nome}")










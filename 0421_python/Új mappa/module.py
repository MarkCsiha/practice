from os import system
from random import randint
from time import sleep


def koszon(nev:str, napszak:str) -> None:
    print(f'Szia {nev}!')
    valasz:str = input(f'Hogy vagy ma {napszak}?')
    if 'jól' in valasz:
        print(f'Na az jó {nev}!')
    elif 'szarul' in valasz:
        print(f'Az szar, {nev} :(')
    else:   print('ok')


def kerdes() -> bool: 
    rszam:int = randint(1, 10)
    ered:int = int(input(f'Mennyi {rszam} négyzete? '))
    if rszam ** 2 == ered:
        return True
    else:
        return False

def befejezes(nev:str) -> None:
    print(f'Rendben {nev}, mára végeztünk!')
    print('Viszontlátásra! ')
    for x in range(3):
        print(end=f'{3 - x}')
        for y in range(3):
            print(end= '.')
            sleep(.5)
        system('cls')


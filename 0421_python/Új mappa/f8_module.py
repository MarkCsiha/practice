from random import randint
from string import ascii_letters

def feltolt(elemszam:int = 100, legkisebb:int = 10, legnagyobb:int = 99) -> list[int]:
    lst:list[int] = []
    for _ in range(elemszam):
        vsz:int = randint(legkisebb, legnagyobb)
        lst.append(vsz)
    return lst

def kiir(lst:list[int], sortores:int = 10) -> None:
    for i in range(len(lst)):
        print(f'{lst[i]}', end=' ')
        if (i + 1) % 10 == 0:
            print(end='\n')

def random_karakter() -> str:
    lehetseges:str = ascii_letters

def random_jelszo(hossz:int = 8) -> str:
    pwd:str = ''
    for _ in range(hossz):
        pwd += random_karakter()
    return pwd

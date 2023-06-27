from modmodule import *

hallgatok:list[Hallgato] = []
file = open(file='C:\\Users\\markc\\OneDrive\\Desktop\\JEDLIK\\JEDLIK\\coruses.txt', mode='r', encoding='UTF-8')

for s in file:
    hallgatok.append(Hallgato(s))

print(f'1. feladat: {len(hallgatok)}')

atlag:int = 0
for h in hallgatok:
    atlag += int(h.eredmenyek['backend']) / len(hallgatok)
print(f'átlag: {atlag:.2f}%')

legjobb:int = 0
for i in range(1, len(hallgatok)):
    if hallgatok[legjobb].osszeredmeny < hallgatok[i].osszeredmeny:
        legjobb = i
print(f'legjobb tanuló neve: {hallgatok[legjobb].nev}')

befizetettek:int = 0
for h in hallgatok:
    if h.befiz >= 2600:
        print(f'\t{h.nev}')

asd = input('Kérek egy nevet: ')
for h in hallgatok:
    if h.bukas == True:
        print(f'{asd}-nak/nek ebből bukott: \n\t-{}')
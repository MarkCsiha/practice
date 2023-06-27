from asd import *
jatekosok:list[Jatekos] = []
file = open(file='C:\\Users\\markc\\OneDrive\\Desktop\\jackie\\juventus.txt', mode='r', encoding='UTF-8')
for sor in file:
    jatekosok.append(Jatekos(sor))

print(f'1. feladat: {len(jatekosok)}')

atlag = 0
for j in jatekosok:
    atlag += (2019 - j.szul) / len(jatekosok)
print(f'2. feladat: {atlag:.2f} év')

hatvedek = 0
for j in jatekosok:
    if j.poszt == 'hátvéd':
        hatvedek += 1
    szazalek = hatvedek / len(jatekosok) * 100
print(f'2. feladat: a játékosok {szazalek}%-a hátvéd')  

user = input('Írj be egy nemzetiséget: ')
for j in jatekosok:
    if user == j.nemz:
        print(f'Van {user} nemzetiségű játékos')
        break
else:
    print(f'Nincs {user} nevű játékos')
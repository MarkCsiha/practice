from module2 import *
autok:list[Auto] = []
file = open(file='C:\\Users\\markc\\OneDrive\\Desktop\\euallamok\\auto.txt', mode='r', encoding='UTF-8')
for sor in file:
    autok.append(Auto(sor))

print(f'4. feladat: {len(autok)}')

gyev:int = 0
for a in autok:
    if a.gyartas > 2000:
        gyev += 1
print(f'5. feladat: {gyev}')

atlag = 0
for a in autok:
    atlag += float(a.fogyasztas)
print(f'6. feladat: {int(atlag/len(autok))} liter')

user = float(input('Írd be a benzin jelenlegi árát: '))
benzinara:int = 0
for a in autok:
    benzinara = user * a.meret
print(benzinara)

for a in autok:
    if a.meret == 38:
        print(a.tipus)
        break
    else:
        print('Nincs ilyen autó')

legnagyobb:int = 0
for a in autok:
    if legnagyobb < a.fogyasztas:
        legnagyobb = a.fogyasztas
        print(a.tipus)
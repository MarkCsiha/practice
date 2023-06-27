from module2 import *
epuletek:list[Épület] = []
file = open(file='legmagasabb.txt', mode='r', encoding='UTF-8')
for sor in file.readlines()[1:]:
    epuletek.append(Épület(sor))

print(f'3.2 feladat: Épületek száma: {len(epuletek)} db ')

emeletek:int = 0
for e in epuletek:
    emeletek += e.emelet
print(f'3.3 feladat: Emeletek összege: {emeletek}')

maxMagassag:int = 0
for i in range(1, len(epuletek)):
    if epuletek[i].magasság > epuletek[maxMagassag].magasság:
        maxMagassag = i
print('3.4 feladat: A legmagasabb épület adatai ')
print(f'\tNév: {epuletek[maxMagassag].nev}')
print(f'\tVáros: {epuletek[maxMagassag].varos}')
print(f'\tOrszág: {epuletek[maxMagassag].orszag}')
print(f'\tMagasság: {epuletek[maxMagassag].magasság} m')
print(f'\tEmeletek száma: {epuletek[maxMagassag].emelet}')
print(f'\tÉpítés éve: {epuletek[maxMagassag].ev}')

for e in epuletek:
    if e.orszag == 'Olaszország':
        print('3.5 feladat: Van olasz épület az adatok között! ')
        break
else:
    print('Nincs olasz épület az adatok között! ')        
from module import *
versenyzok:list[Snooker] = []
file = open(file='C:\\Users\\markc\\OneDrive\\Desktop\\snooker\\snooker.txt', mode='r')
for sor in file:
    versenyzok.append(Snooker(sor))

print(f'1. feladat: {len(versenyzok)}')

atlag = 0
for v in versenyzok:
    atlag += v.nyeremeny / len(versenyzok)
print(f'2. feladat: {atlag:.2f} fontot kerestek')

maxNyeremeny:int = 0
for v in versenyzok:
    if v.orszag == 'Kína':
        if v.nyeremeny > maxNyeremeny:
            v.nyeremeny == maxNyeremeny
        break
    print(f'A legjobban kereső kínai versenyző: \n\tHelyezés: {v.helyezes} \n\tNév: {v.nev} \n\tOrszág: {v.orszag} \n\tNyeremény összege: {maxNyeremeny * 380}')

for v in versenyzok:
    if v.orszag == 'Norvégia':
        print('Volt norvég játékos')
else:
    print('Nem volt norvég játékos')

kina:int = 0
anglia:int = 0
wales:int = 0
skocia:int = 0
for v in versenyzok:
    if v.orszag == 'Kína':
        kina += 1
    elif v.orszag == 'Anglia':
        anglia += 1
    elif v.orszag == 'Wales':
        wales += 1
    elif v.orszag == 'Skócia':
        skocia += 1
print(f'7. feladat: statisztika \n\t Kína - {kina} fő \n\t Anglia - {anglia} fő \n\t Wales - {wales} fő \n\t Skócia - {skocia} fő')
    
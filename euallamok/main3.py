from module3 import *
hegysegek:list[Hegyseg] = []
with open('C:\\Users\\markc\\OneDrive\\Desktop\\euallamok\\hegyekMo.txt', 'r', encoding='UTF-8') as file:
    for i, sor in enumerate(file):
        if i == 0:
            # Skip the first line of the file, which contains header information
            continue
        hegysegek.append(Hegyseg(sor.strip()))

print(f'1. feladat: {len(hegysegek)}')

atlag:int = 0
for h in hegysegek:
    atlag += h.magassag / len(hegysegek)
print(f'{atlag:.2f} méter')

maxHegyseg = 0
for h in hegysegek:
    if h.magassag > maxHegyseg:
        maxHegyseg = h.magassag
print(f'{maxHegyseg} m')

user = int(input('Írj be egy magasságértéket: '))
for h in hegysegek:
    if h.hegyseg == 'Börzsöny' and user > h.magassag:
        print('Nem található ennél nagyobb')
        break
else:
    print('Van ennél nagyobb hegység')
    
Matra = 0
Bukk = 0
Borzsony = 0
Zemplen = 0
Koszeg = 0
for h in hegysegek:
    if h.hegyseg == 'Mátra':
        Matra += 1
    elif h.hegyseg == 'Bükk-vidék':
        Bukk += 1
    elif h.hegyseg == 'Börzsöny':
        Borzsony += 1
    elif h.hegyseg == 'Zempléni-hegység':
        Zemplen += 1
    else:
        Koszeg += 1
print(f'Hegység statisztika \n\tMátra - {Matra} db')


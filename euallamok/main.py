from module import *
hegyek:list[Hegy] = []
with open('C:\\Users\\markc\\OneDrive\\Desktop\\euallamok\\hegyekMo.txt', 'r', encoding='UTF-8') as file:
    for i, sor in enumerate(file):
        if i == 0:
            # Skip the first line of the file, which contains header information
            continue
        hegyek.append(Hegy(sor.strip()))

print(f'3. feladat: {len(hegyek)}')

atlag = 0
for h in hegyek:
    atlag += h.mag / len(hegyek)
print(f'4. feladat: A hegyek átlagmagassága {atlag:.2f} méter')

maxHegy:int = 0
for h in hegyek:
    if maxHegy < h.mag:
        maxHegy = h.mag
print(f'5. feladat: A legmagasabb hegycsúcs adatai: \t Név: {h.nev} \t Hegység: {h.hegyseg} \t Magasság: {maxHegy} m')

user = int(input('Írjon be egy magasságértéket: '))
magassag = 0
for h in hegyek:
    if h.hegyseg == 'Börzsöny' and h.mag > user:
        print(f'6. feladat: Van {user} m-nél nagyobb hegység Börzsönyben!')
        break
else:
    print('Nincs ilyen hegység a Börzsönyben.')


matra = 0
bukk = 0
borzsony = 0
zemplen = 0
koszeg = 0

for h in hegyek:
    if h.hegyseg == 'Mátra':
        matra += 1
    elif h.hegyseg == 'Bükk-vidék': 
        bukk += 1
    elif h.hegyseg == 'Börzsöny':
        borzsony += 1
    elif h.hegyseg == 'Zempléni-hegység':
        zemplen += 1
    else:
        koszeg += 1

print(f'Mátra: {matra} db')
print(f'Bükk-vidék: {bukk} db')
print(f'Börzsöny: {borzsony} db')
print(f'Zemplén: {zemplen} db')
print(f'Kőszegi-hegység: {koszeg} db')

lab = h.mag * 3.280839895
hegys = 0
for h in hegyek:
    if lab > 3000:
        hegys += 1
print(hegys)
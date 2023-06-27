from module2 import *

egitestek:list[Egitest] = []
file = open(file='egitestek.txt', mode='r', encoding='UTF-8')
for sor in file: egitestek.append(Egitest(sor))

print(f'Égitestek száma: {len(egitestek)}')

nkksz:int = 0
for e in egitestek:
    if e.hol_kering == 'Nap': nkksz += 1
print(f'Nap körül keringő égitestek száma: {nkksz}')

lti:int = 0
for i in range(1, len(egitestek)): 
    if egitestek[i].tavolsag < egitestek[lti].tavolsag:
        lti = i
print(f'A legközelebb a bolygójához a(z) {egitestek[lti].elnevezes}')

holdak:list[str] = []
for e in egitestek:
    if not e.direkt_irany:
        holdak.append(e.elnevezes)
for h in holdak:
    print('\t- {h}')

ker_egit:str = input('Keresett égitest neve: ')
for e in egitestek:
    if e.elnevezes == ker_egit:
        if e.felfedezes_eve == '---' and e.felfedezes_eve == '0000':
            print('Felfedezője nem ismert!')
        print('Megvan')
        print(f'Felfedező neve: {e.felfedezo_neve}')
        print(f'Felfedezés éve: {e.felfedezes_eve}')
        break
else:
    print('Nincs ilyen!')
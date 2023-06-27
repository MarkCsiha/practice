from module import *
from random import randint

nev:str = input('Hogy hívnak? ')
nsz:str = input('Milyen napszak van? ')

koszon(nev, nsz)

print('Akkor kezdjük a munkát? ')

pont:int = 0
for x in range(5): 
    print(f'{x+1}: ', end=' ')
    kiert:bool = kerdes()
    if kiert == True:
        print('Helyes')
        pont += 1
    else:
        print('Helytelen')

print(f'Találatok száma: {pont}/5')

befejezes(nev)
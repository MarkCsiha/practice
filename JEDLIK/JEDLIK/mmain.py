from module2 import *
epuletek:list[Épület] = []
file = open(file='C:\\Users\\markc\\OneDrive\\Desktop\\JEDLIK\\JEDLIK\\legmagasabb.txt', mode='r', encoding='UTF-8')

for sor in file.readlines()[1:]:
    epuletek.append(Épület(sor))

print(f'1.: {len(epuletek)}')

emeletek:int = 0
for e in epuletek:
    emeletek += e.emelet
print(f'{emeletek}')

max:int = 0
for i in range(1, len(epuletek)):
    if epuletek[i].magasság > epuletek[max].magasság:
        max = i
print('Adatok: ')
print(f'{epuletek[max].nev}')
print(f'{epuletek[max].varos}')

for e in epuletek:
    if e.orszag == 'Olaszország':
        print(f'Van olasz épület')
        break
else:
    print('Nincs')
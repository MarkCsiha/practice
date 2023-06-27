import random

welcome = print('Betűkitalálós játék, találd ki a számot ')
szamok:int = random.randint(1, 5)

probalkozasok:int = 0
user = None
while user != szamok:
    probalkozasok += 1
    user = int(input('Tippelj egy számot 1 és 500 között: '))
    if user >= szamok:
        print('Kisebb')
    elif user <= szamok:
        print('Nagyobb')
else:
    print('Eltaláltad')
    print(f'Ennyi próbálkozás kellett: {probalkozasok}')


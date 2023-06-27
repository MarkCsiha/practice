from module import *

print('2. feladat: Szökőév listázó')
a:int = int(input('Írj be egy évszámot: '))
b:int = int(input('Írj be egy évszámot: '))

if a > b:
    (a, b) = (b, a)

leap_years:list[int] = []
for y in range(a, b+1):
    if is_leap_year(y): leap_years.append(y)

if len(leap_years) == 0:
    print('Nincs szökőév a megadott tartományban! ')
else:
    print(end='Szökőévek: ')
    for y in leap_years[:-1]:
        print(f'{y}; ')
    print(leap_years[-1])

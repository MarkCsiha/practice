paradicsom:int = 1199
paprika:int = 1349
vöröshagyma:int = 289

kinalat = print(f'Kínálat: Paradicsom: {paradicsom} \nPaprika: {paprika} \nVöröshagyma: {vöröshagyma}')

user = input('Kíván valamit vásárolni? ')
while user == 'igen':
    kerdes = input('melyik termékből? ')
    if kerdes == 'paradicsom':
        paradicsomok = float(input('Hány kg-t szeretne? '))
    elif kerdes == 'paprika':
        paradicsomok = float(input('Hány kg-t szeretne? '))
    elif kerdes == 'vöröshagyma':
        paradicsomok = float(input('Hány kg-t szeretne? '))

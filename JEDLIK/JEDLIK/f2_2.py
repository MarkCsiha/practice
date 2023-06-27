paprika = 1000
paradicsom = 500
vöröshagyma = 300
user = input('Szeretnél valamit vásárolni? ')
while user == 'igen':
    kerdes = input('Mit szeretnél? ')
    if kerdes == 'paprika':
        paprikak = float(input('Hány kg?'))
        k = input('Szeretnél még vásárolni? ')
        if k == 'nem':
            print('köszönjük a vásárlást! ')
            if vöröshagyma or paradicsom == None:
                 pass
                 print((paradicsomok * paradicsom) + (paprikak * paprika) + (vöröshagyma * vorosek))
            break
    elif kerdes == 'paradicsom':
        paradicsomok = float(input('Hány kg? '))
        k = input('Szeretnél még vásárolni? ')
        if k == 'nem':
            print('köszönjük a vásárlást! ')
            if paprika or vöröshagyma == None:
                 pass
                 print((paradicsomok * paradicsom) + (paprikak * paprika) + (vöröshagyma * vorosek))
            break
        
    elif kerdes == 'vöröshagyma':
        vorosek = float(input('Hány kg? '))
        k = input('Szeretnél még vásárolni? ')
        if k == 'nem':
            print('köszönjük a vásárlást! ')
            if paprika or paradicsom == None:
                pass
                print((paradicsomok * paradicsom) + (paprikak * paprika) + (vöröshagyma * vorosek))
            break
    else:
            print('Ilyen termék nincs! ')    
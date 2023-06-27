honap = int(input('Írj be egy hónapot (számban): '))

if honap <= 2:
    print('Tél')
elif honap <= 5:
    print('Tavasz')
elif honap <= 8:
    print('Nyár')
elif honap <= 11:
    print('Ősz')
elif honap == 12:
    print('Tél')
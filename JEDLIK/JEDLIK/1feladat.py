szo = input('szöveg: ')
if len(szo) > 8:
    kisbetus:str = szo.lower()
    print(kisbetus[::-1])
else:
    print('több mint 8 betűnek kell lennie')
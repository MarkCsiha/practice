from random import randint

betuk:list[str] = ['A', 'B', 'C', 'D', 'E', 'F']

rszam1:int = randint(2, 5)
rszam2:int = randint(2, 5)
rszam3:int = randint(2, 5)
rszam4:int = randint(2, 5)
rszam5:int = randint(2, 5)
rszam6:int = randint(2, 5)
print(betuk[0] * rszam1, betuk[1] * rszam2, betuk[2] * rszam3, betuk[3] * rszam4, betuk[4] * rszam5, betuk[5] * rszam6, end=' ')


from module import *

from module import *

egitestek:list[Egitest] = []
f = open(file='egitestek.txt', mode='r', encoding='UTF-8')

for sor in f:
    darabok:list[str] = sor.strip().split(';')
    h:str = darabok[0]
    e:str = darabok[1]
    t:int = int(darabok[3])
    d:bool = darabok[3] == '1'
    a:int = int(darabok[4])
    fn:str = darabok[5]
    fe:int = int(darabok[6])

    e = Egitest(h, e, t, d, a, fn, fe)
    egitestek.append(eg)

for e in egitestek:
    print(e.elnevezes)
class Jatekos:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.mezszam:int = int(v[0])
        self.nev:str = v[1]
        self.nemz:str = v[2]
        self.poszt:str = v[3]
        self.szul:int = int(v[4])
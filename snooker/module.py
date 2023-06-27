class Snooker: 
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.helyezes:int = v[0]
        self.nev:str = v[1]
        self.orszag:str = v[2]
        self.nyeremeny:int = int(v[3])

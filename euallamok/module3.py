class Hegyseg:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.hegyseg:str = v[1]
        self.magassag:int = int(v[2])
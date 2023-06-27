class Epulet:
    def __init__ (self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.varos:str = v[1]
        self.mag:int = float(v[2].replace(',', '.'))
        self.emelet:int = int(v[3])
        self.epult:str = v[4]
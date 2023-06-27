class Auto:
    def __init__ (self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.tipus:str = v[0]
        self.fogyasztas = float(v[1].replace(',', '.'))
        self.meret:int = int(v[2])
        self.gyartas:int = int(v[3])
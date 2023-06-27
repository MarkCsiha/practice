class Hallgato:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.nem:bool = v[1] == 'f' == True
        self.befiz:int = int(v[2])
        self.eredmenyek:dict[int, str] = {
            'hálózat': int(v[3]),
            'mobil': int(v[4]),
            'frontend': int(v[5]),
            'backend': int(v[6])
        }
        self.osszeredmeny:int = sum(self.eredmenyek.values())
        self.bukas = False
        for e in self.eredmenyek.values():
            if e <= 50: self.bukas = True
            break
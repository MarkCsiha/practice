class Épület:
    def __init__ (self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.varos:str = v[1]
        self.orszag:str = v[2]
        self.magasság:float = float(v[3].replace(',', '.'))
        self.emelet:int = int(v[4])
        self.ev:int = int(v[5])

def is_leap_year(year:int) -> bool:
    if year % 400 == 0: return True
    elif year % 4 == 0 and year % 100 != 0: return True
    else: return False
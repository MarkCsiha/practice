class Verseny:
    def __init__(self, sor: str) -> None:
        v:list[str] = sor.strip().split(';')
        self.year = int(v[0])
        self.races = int(v[1])
        self.wins = int(v[2])
        self.podiums = int(v[3])
        self.poles = int(v[4])
        self.fastests = int(v[5])

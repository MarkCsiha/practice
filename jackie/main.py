class Verseny:
    def __init__(self, sor: str) -> None:
        v:list[str] = sor.strip().split('\t')
        self.year = int(v[0])
        self.races = int(v[1])
        self.wins = int(v[2])
        self.podiums = int(v[3])
        self.poles = int(v[4])
        self.fastests = int(v[5])
        self.wins6:bool = '1964', '1965', '1966', '1967', '1968', '1969' == True

versenyek:list[Verseny] = []
with open('C:\\Users\\markc\\OneDrive\\Desktop\\jackie\\jackie.txt', 'r', encoding='UTF-8') as file:
    for i, sor in enumerate(file):
        if i == 0:
            # Skip the first line of the file, which contains header information
            continue
        versenyek.append(Verseny(sor.strip()))


print(f'3. feladat: {len(versenyek)}')

maxRaces = 0
maxElem = None
for elem in versenyek:
    if elem.races > maxRaces:
        maxRaces = elem.races
        maxElem = elem
print(f'4. feladat: {maxElem.year}')

    # Initialize the variables to store the total number of races won in each category
races_1964_1969 = 0
races_1970_1973 = 0
    
    # Loop through each line in the input file
for v in versenyek:
        # Convert the races value to an integer
    races = int(v.wins)
        
        # Categorize the races based on the year
    if int(v.year) >= 1964 and int(v.year) <= 1969:
            races_1964_1969 += races
    elif int(v.year) >= 1970 and int(v.year) <= 1973:
            races_1970_1973 += races
    
    # Print the results
print("Total number of races won by Jackie Stewart from 1964 to 1969:", races_1964_1969)
print("Total number of races won by Jackie Stewart from 1970 to 1973:", races_1970_1973)

hatvanasok = 0
hetvenesek = 0

for v in versenyek:
    if v.year >= 1964 and v.year <= 1969:
        hatvanasok += v.wins
    elif v.year >= 1970 and v.year <= 1973:
         hetvenesek += v.wins

print(f'Hatvanas években: {hatvanasok}')
print(f'Hetvenes években: {hetvenesek}')
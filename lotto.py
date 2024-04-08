'''
* Dit programma berekent het verlies op de Belgische Lotto.
*
* Gebruik: python lotto.py n1 n2 n3 n4 n5 n6
* hierbij zijn nX de zes lottogetallen
*
* Wanneer je niet genoeg lottogetallen meegeeft, wordt de lijst aangevuld met een standaardreeks.
*
* Zorg ervoor dat je eerst de juiste databestanden download (trekkingsresultaten en financiële resultaten)
* van de lottowebsite: https://www.nationale-loterij.be/onze-spelen/lotto/uitslagen-trekking/statistieken
*
'''

import sys
import glob
from lotto_utils import bepaal_rang

def get_nummers(lijn:str) -> list[int]:
    items = lijn.split(";")
    return [int(s) for s in items[1:]]

def get_bedragen(lijn:str) -> list[float]:
    items = lijn.split(";")
    return [float(s.replace(',','.')) for s in items[4:22:2]]

def lees_argumenten(default_lijst):
    for index,nummer in enumerate(sys.argv[1:]):
        default_lijst[index] = int(nummer)
    return default_lijst

def test_data():
    gamedata_bestanden = glob.glob( './data/lotto-gamedata-NL-*.csv')
    financialdata_bestanden = glob.glob('./data/lotto-financialdata-NL-*.csv')
    gamedata_bestanden.sort()
    financialdata_bestanden.sort()
    if len(gamedata_bestanden) == 0 or len(gamedata_bestanden) != len(financialdata_bestanden):
        return False
    for gamedata_bestand, financialdata_bestand in zip(gamedata_bestanden, financialdata_bestanden):
        if gamedata_bestand[-8:] != financialdata_bestand[-8:]:
            return False
    return True

if not test_data():
    print("Download eerst de juiste gamedata- en financialdatabestanden van de Lotto website")
    sys.exit(1)

gamedata_bestanden = glob.glob( './data/lotto-gamedata-NL-*.csv')
financialdata_bestanden = glob.glob('./data/lotto-financialdata-NL-*.csv')
gewonnen_bedrag = 0
mijn_nummers = lees_argumenten([7, 20, 26, 31, 35, 42])
print(f"Lottowinst voor {mijn_nummers}")
aantal_trekkingen = 0
aantal_gewonnen = 0
rang_verdeling = dict({ (key, 0) for key in range(1, 10)})

for (gamedata_bestand, financialdata_bestand) in zip(gamedata_bestanden, financialdata_bestanden):
    with open(gamedata_bestand, 'r') as game_f:
        with open(financialdata_bestand, 'r') as financial_f:
           game_f.readline()
           financial_f.readline()
           for (game_lijn, financial_lijn) in zip(game_f, financial_f) :
               aantal_trekkingen += 1
               nummers = get_nummers(game_lijn)
               rang = bepaal_rang(nummers[:6], nummers[6], mijn_nummers)

               bedragen = get_bedragen(financial_lijn)
               if rang is not None:

                   rang_verdeling[rang] += bedragen[rang -1]
                   gewonnen_bedrag += bedragen[rang -1]
                   aantal_gewonnen += 1

uitgegeven_bedrag = aantal_trekkingen * 1.25

winst = gewonnen_bedrag - uitgegeven_bedrag
if winst < 0:
    print(f"Het verlies na {aantal_trekkingen} lotttrekkingen is {winst} EUR.")
    print('\n"Op de Lotto spelen kan uw portemonnee schaden."')
else:
    print("Er zit een fout in de berekening.")


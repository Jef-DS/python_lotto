#
# Script met hulpfunctie voor de berekening van een lottorang
#

import unittest
from collections.abc import Iterable

def bepaal_rang(lotto_nummers:Iterable[int], bonusnummer:int, mijn_nummers:Iterable[int]) -> int|None:
    aantal_juist = 0
    for nummer in mijn_nummers:
        if nummer in lotto_nummers: aantal_juist += 1
    heeft_bonus = bonusnummer in mijn_nummers
    match(aantal_juist):
        case 6:
            rang = 1
        case 3| 4| 5:
            rang = 13 - (2 * aantal_juist)
            if heeft_bonus: rang -= 1
        case 1|2 if heeft_bonus:
            rang = 10 - aantal_juist
        case _:
            rang = None
    return rang

class TestLottoGetallen(unittest.TestCase):
    def test_rang1(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 4, 5, 6]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 1 
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang2(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 4, 5, 7]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 2 
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang3(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 4, 5, 8]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 3 
        self.assertEqual(test_rang, oracle_rang)

        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 4, 8, 7]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 4
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang5(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 4, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 5
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang6(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 7, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 6 
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang7(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 3, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 7 
        self.assertEqual(test_rang, oracle_rang)

    def test_rang8(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 7, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 8 
        self.assertEqual(test_rang, oracle_rang)
    
    def test_rang9(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 11, 7, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        oracle_rang = 9 
        self.assertEqual(test_rang, oracle_rang)

    def test_rangNone_1juist(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 11, 12, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        self.assertIsNone(test_rang)
    
    def test_rangNone_2juist(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [1, 2, 12, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        self.assertIsNone(test_rang)  

    def test_rangNone_0juist(self):
        lotto_getallen = [1, 2, 3, 4, 5, 6]
        speelgetallen = [14, 13, 12, 10, 8, 9]
        bonusgetal = 7
        test_rang = bepaal_rang(lotto_getallen, bonusgetal, speelgetallen)
        self.assertIsNone(test_rang)

if __name__ == '__main__':
    unittest.main()
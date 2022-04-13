import unittest
from translator import englishtofrench, frenchtoenglish
class EnglishtoFrench(unittest.TestCase):
    def englishtofrenchtest(self): #This function translates english to french
        self.assertEqual(englishtofrench(''),'Text entered is invalid')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
class FrecnchtoEnglish(unittest.TestCase):
    def frenchtoenglishtest(self): #This function translatesfrench to english
        self.assertEqual(frenchtoenglish(''),'Text entered is invalid')
        self.assertEqual(frenchtoenglish('Bojour'),'Hello')

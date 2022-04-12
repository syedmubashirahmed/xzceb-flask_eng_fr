import unittest
from translator import languagetranslator, englishtofrench, frenchtoenglish
class EnglishtoFrench(unittest.TestCase):
    def englishtofrenchtest(self): #This function translates english to french
        self.assertEqual(englishtofrench('','Please enter some text to translate'))
        self.assertEqual(englishtofrench('Hello','Bonjour'))
class FrecnchtoEnglish(unittest.TestCase):
    def frenchtoenglishtest(self): #This function translatesfrench to english
        self.assertEqual(frenchtoenglish('','Please enter some text to translate'))
        self.assertEqual(frenchtoenglish('Bojour','Hello'))

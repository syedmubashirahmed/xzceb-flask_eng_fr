import unittest
import machinetranslation
from machinetranslation import translator
class EnglishtoFrench(unittest.TestCase):
    def englishtofrenchtest(self): #This function translates english to french
        self.assertEqual(translator.englishtofrench(''),'Text entered is invalid')
        self.assertEqual(translator.englishtofrench('Hello'),'Bonjour')
class FrecnchtoEnglish(unittest.TestCase):
    def frenchtoenglishtest(self): #This function translatesfrench to english
        self.assertEqual(translator.frenchtoenglish(''),'Text entered is invalid')
        self.assertEqual(translator.frenchtoenglish('Bojour'),'Hello')

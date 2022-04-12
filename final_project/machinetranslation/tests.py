import unittest
from translator import englishtofrench, frenchtoenglish
class EnglishtoFrench(unittest.TestCase):
    def englishtofrenchtest(self): #This function translates english to french
        self.assertEqual(translator.englishtofrench(''),'Please enter some text to translate')
        self.assertEqual(translator.englishtofrench('Hello'),'Bonjour')
class FrecnchtoEnglish(unittest.TestCase):
    def frenchtoenglishtest(self): #This function translatesfrench to english
        self.assertEqual(translator.frenchtoenglish(''),'Please enter some text to translate')
        self.assertEqual(translator.frenchtoenglish('Bojour'),'Hello')

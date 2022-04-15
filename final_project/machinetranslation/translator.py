"""Language Translator"""
#  apikey="2n9ksWcmASg1fqufKsysdIjLr-qQvepVXDKDM3TSk_nO"
 # url="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/e6d3bba4-30c2-4ede-8ec0-fd92271c3d93"
import json
import unittest
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
APIKEY=os.environ["apikey"]
URL=os.environ['url']
authenticator=IAMAuthenticator(APIKEY)
language_translator=LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(URL)
def englishtofrench(englishtext):
    """English to French Translation"""
   
    translation=language_translator.translate(
        text=englishtext,model_id='en-fr').get_result()
    returnvalue=(translation["translations"][0]["translation"])
   
   
    return returnvalue
def frenchtoenglish(frenchtext):
    """French to English Translation"""
    
    
    translation=language_translator.translate(
        text=frenchtext,model_id='fr-en').get_result()
    
    returnvalue=(translation["translations"][0]["translation"])
   
    
    return returnvalue
    

class EnglishtoFrench(unittest.TestCase):
    def testenglishtofrench(self): #This function translates english to french
       # self.assertEqual(englishtofrench(''),'Text entered is invalid')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('Hello'),'Hello')
class FrecnchtoEnglish(unittest.TestCase):
    def testfrenchtoenglish(self): #This function translatesfrench to english
        #self.assertEqual(frenchtoenglish(''),'Text entered is invalid')
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchtoenglish('Bonjour'),'Bonjour')
unittest.main()

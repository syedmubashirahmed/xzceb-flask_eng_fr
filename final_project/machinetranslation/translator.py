"""Language Translator"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.environ['API_KEY']
URL = os.environ['URL']
def englishToFrench(englishText):
    """English to French Translation"""
    frenchText=""
    return frenchText
def frenchToEnglish(frenchText):
    """French to English Translation"""
    englishText=""
    return englishText
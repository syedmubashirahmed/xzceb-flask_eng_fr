"""Language Translator"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.environ['API_KEY']
URL = os.environ['URL']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

def translator(texttotranslate):
    # This function translates text from one language to another
    translation = language_translator.translate(
    text=texttotranslate,
    model_id='en-fr').get_result()
    return json.dumps(translation, indent=2, ensure_ascii=False)
def englishToFrench(englishtext):
    """English to French Translation"""
    frenchtext=translator(englishtext)
    return frenchtext
def frenchToEnglish(frenchtext):
    """French to English Translation"""
    englishtext=translator(frenchtext)
    return englishtext
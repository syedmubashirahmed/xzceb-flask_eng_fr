"""Language Translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
APIKEY=os.environ['API_KEY']
URL=os.environ['URL']
authenticator=IAMAuthenticator(APIKEY)
language_translator=LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url('{URL}')
def languagetranslator(texttotranslate):
    """This function translates text from one language to another"""
    translation = language_translator.translate(
    text=texttotranslate, model_id='en-fr').get_result()
    if texttotranslate == '': 
        return "Please enter some text to translate."
    return json.dumps(translation, indent=2, ensure_ascii=False)
def englishtofrench(englishtext):
    """English to French Translation"""
    frenchtext=languagetranslator(englishtext)
    return frenchtext
def frenchtoenglish(frenchtext):
    """French to English Translation"""
    englishtext = languagetranslator(frenchtext)
    return englishtext

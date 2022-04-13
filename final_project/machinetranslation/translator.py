"""Language Translator"""
import json
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
    returnvalue=''
    if englishtext!='':
        translation=language_translator.translate(
            text=englishtext,model_id='en-fr').get_result()
        returnvalue=(translation["translations"][0]["translation"])
    else:
        returnvalue="Text entered is invalid"
    return returnvalue
def frenchtoenglish(frenchtext):
    """French to English Translation"""
    returnvalue=''
    if frenchtext !='':
        translation=language_translator.translate(
             text=frenchtext,model_id='fr-en').get_result()
        returnvalue=(translation["translations"][0]["translation"])
    else:
        returnvalue="Text entered is invalid"
    return returnvalue
    
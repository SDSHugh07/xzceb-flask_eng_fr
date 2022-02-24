"""
docstring
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    docstring
    """

    if english_text != "":
        translation_response = language_translator.translate(text=english_text, model_id='en-fr')
        translation=translation_response.get_result()
        french_text=translation['translations'][0]['translation']
        return french_text
    return "Null input"


def frenchToEnglish(french_text):
    """
    docstring
    """

    if french_text != "":
        translation_response = language_translator.translate(text=french_text, model_id='fr-en')
        translation=translation_response.get_result()
        english_text=translation['translations'][0]['translation']
        return english_text
    return "Null input"
    
"""
print(englishToFrench("You look wonderful tonight"))
print(frenchToEnglish("Tu as l'air merveilleuse ce soir"))
print(englishToFrench(""))
print(frenchToEnglish(""))
"""
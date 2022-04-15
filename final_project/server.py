from flask import Flask, request
from machinetranslation import translator
app = Flask("Web Translator")
@app.route("/englishtofrench")
def englishtofrench():
    """English to French"""
    texttotranslate = request.args.get('textToTranslate')
    returnedvalue=translator.englishtofrench(texttotranslate)
    return f"<h1>The translation of {texttotranslate} in french  is: {returnedvalue}</h1>"
@app.route("/frenchtoenglish")
def frenchtoenglish():
    """French to English"""
    texttotranslate = request.args.get('textToTranslate')
    returnedvalue=translator.frenchtoenglish(texttotranslate)
    return f"<h1>The translation of {texttotranslate} in English is: {returnedvalue} </h1>"
@app.route("/")
def renderindexpage():
    """ Write the code to render template"""
    return "hello World"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

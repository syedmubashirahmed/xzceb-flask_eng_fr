import json
import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
app = Flask("Web Translator")
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #Write your code here
    returnedvalue=translator.englishtofrench(textToTranslate)
    return '''<h1>The translation of {} in french  is: {}</h1>'''.format(textToTranslate,returnedvalue)
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    returnedvalue=translator.frenchtoenglish(textToTranslate)
    return '''<h1>The translation of {} in English is: {} </h1>'''.format(textToTranslate,returnedvalue)
    #return "french to english"
    
    
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return "hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

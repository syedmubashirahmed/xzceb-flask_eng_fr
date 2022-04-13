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
    return returnedvalue
    #return textToTranslate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    returnedvalue=translator.frenchtoenglish(textToTranslate)
    return returnedvalue
    
    
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return "hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

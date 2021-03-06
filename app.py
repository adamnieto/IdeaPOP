from flask import Flask, render_template, request, url_for, Markup
import getString, getImage, os
app = Flask(__name__)

# setting up the basic route

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/get_data", methods=['POST'])
def handle_data():
    textBox = request.form["ideaBox"]
    indexValues = getString.processString(textBox)
    searchTerms = getString.getSearchValues(indexValues, textBox)
    arrayLinks = getImage.main(searchTerms)
    termCounter = 0
    termInfo = ""
    code = ""
    for linkAddress in arrayLinks:
        linkAddress1 = linkAddress.strip("}")
        code += '<a href="' + linkAddress1 + '">' + '<img class="img-circle" src="'+ linkAddress1 + '" ></a>'

    for term in searchTerms:
        if termCounter == 0:
            termInfo += term.strip("\n")
            termInfo += " "
            termCounter += 1
        else:
            termInfo += ", " + term.strip("\n")
            termInfo += " "
    return render_template("product.html",images= Markup(code),termInfo=termInfo,textBox=textBox)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

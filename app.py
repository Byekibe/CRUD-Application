from flask import Flask, request, url_for
from flask.templating import render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=['GET', 'POST']) 
def form():
    if request.form:
        name = request.form["name"]
        print(name)
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True, port=7000)
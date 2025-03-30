from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/", methods=["POST","GET"])

def calculate():
    try:

        birth_year =int(request.form.get("birth_year"))

        current_year = datetime.now().year

        if birth_year > current_year or birth_year < 1900:
            return render_template("idnex.html", error="Please Enter A Valid Year (1900 - Current Year).")
        
        h = current_year - birth_year

        return render_template("index.html",age=h)
    
    except ValueError:

        return render_template("index.html",error="Please Enter A Valid Number")
    
if __name__ == "__main__":
    app.run(debug=True)    
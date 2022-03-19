from src.srcsub1.calculator import Calculator
from flask import Flask, render_template, request

cal = Calculator() # Realization
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"]) # get: get info from backend; POST: stream info from frontend
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"]
        if operator == "+":
            result = cal.add(float(num1),float(num2))
        elif operator == "-":
            result = float(num1)-float(num2)
        elif operator == "*":
            result = float(num1)*float(num2)
        else:
            result = float(num1)/float(num2)

    return render_template('index.html', result=result)

@app.route('/health')  # show the contents on the subpage called "health"
def health():
    return "I am healthy"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1",port=5000)


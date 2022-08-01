
from flask import Flask, render_template, request
import util


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == "POST":
        age = request.form['age']
        sex = request.form['sex']
        bmi = request.form['bmi']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']

    result = (util.predict_charge(age, sex, bmi, children, smoker, region))
    return render_template('home.html', result = result)



if __name__ == "__main__":
    util.load_saved_model()
    app.run(debug=True)
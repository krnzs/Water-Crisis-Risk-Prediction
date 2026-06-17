from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('water_crisis_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    rainfall = float(request.form['rainfall'])
    population = float(request.form['population'])
    groundwater = float(request.form['groundwater'])

    prediction = model.predict(
        [[rainfall, population, groundwater]]
    )

    if prediction[0] == 1:
        result = "High Water Crisis Risk"
    else:
        result = "Low Water Crisis Risk"

    return render_template(
        'index.html',
        prediction=result
    )

if __name__ == '__main__':
    app.run(debug=True)
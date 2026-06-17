from flask import Flask, render_template, request
import pickle

app = Flask(name)

model = pickle.load(open('water_crisis_model.pkl', 'rb'))

@app.route('/')
def home():
return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

rainfall = float(request.form['rainfall'])
population = float(request.form['population'])
groundwater = float(request.form['groundwater'])

prediction = model.predict([[groundwater]])

if prediction[0] == 1:
    result = "🔴 High Water Crisis Risk"
else:
    result = "🟢 Low Water Crisis Risk"

return render_template(
    'index.html',
    prediction=result
)

if name == "main":
app.run(debug=True)

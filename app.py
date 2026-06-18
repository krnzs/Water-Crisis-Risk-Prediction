from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('water_crisis_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs
        rainfall = float(request.form['rainfall'])
        population = float(request.form['population'])
        groundwater = float(request.form['groundwater'])

        # Backend Validation
        if rainfall < 0:
            return render_template(
                'index.html',
                prediction="❌ Rainfall cannot be negative."
            )

        if population < 0:
            return render_template(
                'index.html',
                prediction="❌ Population cannot be negative."
            )

        if groundwater < 0:
            return render_template(
                'index.html',
                prediction="❌ Groundwater level cannot be negative."
            )

        # Make prediction
        prediction = model.predict([[rainfall, population, groundwater]])

        # Display result
        if prediction[0] == 1:
            result = "🔴 High Water Crisis Risk"
        else:
            result = "🟢 Low Water Crisis Risk"

        return render_template(
            'index.html',
            prediction=result
        )

    except ValueError:
        return render_template(
            'index.html',
            prediction="❌ Please enter valid numeric values only."
        )

    except Exception:
        return render_template(
            'index.html',
            prediction="❌ Something went wrong. Please try again."
        )


if __name__ == "__main__":
    app.run(debug=True)

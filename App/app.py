from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


model = joblib.load('Models/stock_movement_classifier.pkl')
scaler = joblib.load('Models/scaler.pkl')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        sentiment = float(request.form['sentiment'])
        historical_price = float(request.form['historical_price'])

        features = np.array([[sentiment, historical_price]])

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)

        return render_template('index.html', prediction=prediction[0])
    
    except Exception as e:
        return render_template('index.html', prediction=str(e))
    

if __name__ == '__main__':
    app.run(debug=True)


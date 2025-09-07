from flask import Flask, request, jsonify
import joblib
from logging_setup import setup_logging

app = Flask(__name__)
logger = setup_logging()

model = joblib.load('models/rf_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    logger.info(f"Request data: {data}")
    try:
        # For demo, ignore country filtering
        features = [data['features']]
        prediction = model.predict(features)[0]
        logger.info(f"Prediction: {prediction}")
        return jsonify({'prediction': prediction})
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

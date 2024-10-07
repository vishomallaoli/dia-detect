from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the SVM model using joblib
svm_model = joblib.load('svm_model.joblib')

# Home route - renders the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route - handles form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from the form (these must match the number of features)
        features = [float(x) for x in request.form.values()]
        
        # Convert input into NumPy array for model prediction
        final_features = [np.array(features)]
        
        # Make prediction using the loaded model
        prediction = svm_model.predict(final_features)
        
        # Assuming binary classification: 1 = Diabetic, 0 = Not Diabetic
        result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
        
        return render_template('index.html', prediction_text=f'Prediction: {result}')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)

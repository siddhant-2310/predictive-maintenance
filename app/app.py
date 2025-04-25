from flask import Flask, request, jsonify, render_template


import numpy as np
import tensorflow as tf
import os

# Load the trained model
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/models/predictive_maintenance_model.h5"))
print("Loading model from:", model_path)
model = tf.keras.models.load_model(model_path, compile=True)

# Create Flask app with absolute static folder path
static_path = os.path.join(os.path.dirname(__file__), 'static')
print(f"Static files path: {static_path}")
print(f"Static files exist: {os.path.exists(static_path)}")
app = Flask(__name__, static_folder=static_path)




# Define prediction function
def predict_maintenance(sensor_data):
    try:
        # Ensure input matches the required format (7 features)
        features = np.array([[ 
            float(sensor_data['Type']),
            float(sensor_data['Air temperature [K]']),
            float(sensor_data['Process temperature [K]']),
            float(sensor_data['Rotational speed [rpm]']),
            float(sensor_data['Torque [Nm]']),
            float(sensor_data['Vibration Levels']),
            float(sensor_data['Operational Hours'])
        ]], dtype=np.float32)


        # Get prediction
        prediction = model.predict(features)[0][0]  # Assuming binary classification
        
        # Convert probability to class label
        result = "Normal" if prediction < 0.5 else "Maintenance Required"
        return result
    
    except Exception as e:
        return str(e)

# Define API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON input from user
    result = predict_maintenance(data)  # Get model prediction
    return jsonify({"prediction": result})  # Return response in JSON format

# Serve web interface
@app.route('/')
def index():
    return render_template('index.html')



# Run the app
if __name__ == '__main__':
    app.run(debug=True)

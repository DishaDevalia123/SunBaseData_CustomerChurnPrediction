from flask import Flask, request, jsonify, render_template
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(_name_)

model = load_model("final_model.h5")

def Prediction_mockery():
    """Mocking the prediction on some complex random data."""
    return np.random.rand()
@app.route('/Predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)
        location = data['location']
        age = data['age']
        subscription_length = data['subscriptionLength']  
        monthly_bill = data['monthlyBill']  
        total_usage_gb = data['totalUsage']  

        location_categories = ['Miami', 'New York', 'Los Angeles', 'Chicago', 'Houston']
        location_features = [int(location == category) for category in location_categories]

        input_data = [age, subscription_length, monthly_bill, total_usage_gb] + location_features

        
        input_data = np.array([input_data])  
        churn_prediction = model.predict(input_data)
        print(churn_prediction)

        result = "Churn" if churn_prediction[0][0] > 0.5 else "No Churn"

        print("Sending prediction:", result) 
        return jsonify({"prediction": result})

    except Exception as e:
        print("Error encountered:", str(e))  
        return jsonify({"error": str(e)})

@app.route('/')
def index():
    return render_template('app.html')

if _name_ == '_main_':
    app.run(debug=True)
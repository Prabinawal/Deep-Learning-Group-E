from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np

# Initializing the Flask app
app = Flask(__name__)
CORS(app)

# Loading the trained model
with open('rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Prediction function of churn
def predict_churn(features):
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return prediction[0]

# Defining  a route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Extracting the  features from the JSON data
    features = [
        data.get("CR_PROD_CNT_IL", 0), 
        data.get("AMOUNT_RUB_CLO_PRC", 0), 
        data.get("PRC_ACCEPTS_A_EMAIL_LINK", 0),
        data.get("Region_code", 0), 
        data.get("PRC_ACCEPTS_A_POS", 0), 
        data.get("PRC_ACCEPTS_A_TK", 0),
        data.get("TURNOVER_DYNAMIC_IL_1M", 0), 
        data.get("CNT_TRAN_AUT_TENDENCY1M", 0), 
        data.get("SUM_TRAN_AUT_TENDENCY1M", 0),
        data.get("LDEAL_ACT_DAYS_ACC_PCT_AVG", 0), 
        data.get("REST_DYNAMIC_CC_3M", 0), 
        data.get("MED_DEBT_PRC_YWZ", 0),
        data.get("LDEAL_ACT_DAYS_PCT_TR3", 0), 
        data.get("LDEAL_ACT_DAYS_PCT_AAVG", 0), 
        data.get("LDEAL_DELINQ_PER_MAXYWZ", 0),
        data.get("TURNOVER_DYNAMIC_CC_3M", 0), 
        data.get("LDEAL_ACT_DAYS_PCT_TR", 0), 
        data.get("LDEAL_ACT_DAYS_PCT_TR4", 0),
        data.get("LDEAL_ACT_DAYS_PCT_CURR", 0)
    ]

    # Making predictions from features
    prediction = predict_churn(features)
    
    # Preparing the responses
    response = {'prediction': prediction}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

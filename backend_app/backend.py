from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path,'rb') as model_file:
        model = pickle.load(model_file)
    return model

model_churn = open_model("model.pkl")

def churn_inference(data,model=model_churn):
    """
    input : list with length 17 ---> [''SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Partner',
       'Dependents', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
       """
    LABEL = ['Churn','Not Churn']
    columns = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Partner',
    'Dependents', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
    data = pd.DataFrame([data], columns=columns)  
    res = model.predict(data)
    return res [0] , LABEL[res[0]]

@app.route("/")  # Home
def home():
    return "Program is up and running"

@app.route("/predict", methods=["POST"]) # Predict
def churn_predict():
    args = request.json
    senior_citizen = args.get("Senior_Citizen")
    tenure = args.get("tenure")
    monthly_charges = args.get("monthly_charges")
    total_charges = args.get("total_charges")
    partner = args.get("partner")
    dependents = args.get("dependents")
    multiple_lines = args.get("multiple_lines")
    internet_services = args.get("internet_services")
    online_security = args.get("online_security")
    online_backup = args.get("online_backup")
    device_protection = args.get("device_protection")
    tech_support = args.get("tech_support")
    streaming_tv = args.get("streaming_tv")
    streaming_movies = args.get("streaming_movies")
    contract = args.get("contract")
    paperless_billing = args.get("paperless_billing")
    payment_method = args.get("payment_method")
    new_data = [senior_citizen,tenure,monthly_charges,total_charges,partner,dependents,
                multiple_lines,internet_services,online_security,online_backup,device_protection,
                tech_support,streaming_tv,streaming_movies,contract,paperless_billing,payment_method]
    idx, label = churn_inference(new_data)
    response = jsonify(result=str(idx) , label_names=label)
    return response

# app.run(debug=True)
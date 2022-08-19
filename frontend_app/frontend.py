import streamlit as st
import requests

st.title("Predict Telco Customer Churn")
sc = st.selectbox("Senior Citizen", [0,1])
tnr = st.number_input("Tenure")
mc = st.number_input("monthly charges")
tc = st.number_input("total charges")
part = st.selectbox("Partner", ["No","Yes"])
depend = st.selectbox("Dependents", ["No","Yes"])
multiple = st.selectbox("Multiple Lines", ['Yes' ,'No' ,'No phone service'])
internet = st.selectbox("Internet Services", ['Fiber optic', 'DSL', 'No'])
security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
backup = st.selectbox("Online Backup", ['Yes', 'No' ,'No internet service'])
protection = st.selectbox("Device Protection", ['No' ,'Yes' ,'No internet service'])
support =st.selectbox("Tech Support", ['No', 'Yes' ,'No internet service'])
tv = st.selectbox("Streaming TV", ['No', 'Yes' ,'No internet service'])
movies = st.selectbox("Streaming Movies", ['No', 'Yes' ,'No internet service'])
contr = st.selectbox("Contract", ['Month-to-month', 'One year' ,'Two year'])
billing = st.selectbox("Paperless Billing", ['Yes' ,'No'])
payment = st.selectbox("Payment Method", ['Electronic check' ,'Credit card (automatic)' ,'Bank transfer (automatic)'
 ,'Mailed check'])

# inference 
URL = "https://model-predict-churn.herokuapp.com/predict"
param = {'Senior_Citizen' : sc,
         'tenure' : tnr,
         'monthly_charges' : mc,
         'total_charges' : tc,
         'partner' : part,
         'dependents' : depend,
         'multiple_lines' : multiple,
         'internet_services' : internet,
         'online_security' : security,
         'online_backup' : backup,
         'device_protection' : protection,
         'tech_support' : support,
         'streaming_tv' : tv,
         'streaming_movies' : movies,
         'contract' : contr,
         'paperless_billing': billing,
         'payment_method' : payment }

r = requests.post(URL, json =param)
if r.status_code == 200:
    res = r.json()
    st.title(res['label_names'])
else :
    st.title('Unexpected Error')
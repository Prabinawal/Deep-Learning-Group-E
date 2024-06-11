import streamlit as st
import requests

st.title('Bank Customer Churn Prediction')

# Creating form for user input
with st.form(key='prediction_form'):
    CR_PROD_CNT_IL = st.number_input('CR_PROD_CNT_IL')
    AMOUNT_RUB_CLO_PRC = st.number_input('AMOUNT_RUB_CLO_PRC')
    PRC_ACCEPTS_A_EMAIL_LINK = st.number_input('PRC_ACCEPTS_A_EMAIL_LINK')
    Region_code = st.number_input('Region_code')
    PRC_ACCEPTS_A_POS = st.number_input('PRC_ACCEPTS_A_POS')
    PRC_ACCEPTS_A_TK = st.number_input('PRC_ACCEPTS_A_TK')
    TURNOVER_DYNAMIC_IL_1M = st.number_input('TURNOVER_DYNAMIC_IL_1M')
    CNT_TRAN_AUT_TENDENCY1M = st.number_input('CNT_TRAN_AUT_TENDENCY1M')
    SUM_TRAN_AUT_TENDENCY1M = st.number_input('SUM_TRAN_AUT_TENDENCY1M')
    LDEAL_ACT_DAYS_ACC_PCT_AVG = st.number_input('LDEAL_ACT_DAYS_ACC_PCT_AVG')
    REST_DYNAMIC_CC_3M = st.number_input('REST_DYNAMIC_CC_3M')
    MED_DEBT_PRC_YWZ = st.number_input('MED_DEBT_PRC_YWZ')
    LDEAL_ACT_DAYS_PCT_TR3 = st.number_input('LDEAL_ACT_DAYS_PCT_TR3')
    LDEAL_ACT_DAYS_PCT_AAVG = st.number_input('LDEAL_ACT_DAYS_PCT_AAVG')
    LDEAL_DELINQ_PER_MAXYWZ = st.number_input('LDEAL_DELINQ_PER_MAXYWZ')
    TURNOVER_DYNAMIC_CC_3M = st.number_input('TURNOVER_DYNAMIC_CC_3M')
    LDEAL_ACT_DAYS_PCT_TR = st.number_input('LDEAL_ACT_DAYS_PCT_TR')
    LDEAL_ACT_DAYS_PCT_TR4 = st.number_input('LDEAL_ACT_DAYS_PCT_TR4')
    LDEAL_ACT_DAYS_PCT_CURR = st.number_input('LDEAL_ACT_DAYS_PCT_CURR')

    submit_button = st.form_submit_button('Predict')

if submit_button:
    # Collecting the entered into a dictionary
    input_data = {
        'features': [
            CR_PROD_CNT_IL,
            AMOUNT_RUB_CLO_PRC,
            PRC_ACCEPTS_A_EMAIL_LINK,
            Region_code,
            PRC_ACCEPTS_A_POS,
            PRC_ACCEPTS_A_TK,
            TURNOVER_DYNAMIC_IL_1M,
            CNT_TRAN_AUT_TENDENCY1M,
            SUM_TRAN_AUT_TENDENCY1M,
            LDEAL_ACT_DAYS_ACC_PCT_AVG,
            REST_DYNAMIC_CC_3M,
            MED_DEBT_PRC_YWZ,
            LDEAL_ACT_DAYS_PCT_TR3,
            LDEAL_ACT_DAYS_PCT_AAVG,
            LDEAL_DELINQ_PER_MAXYWZ,
            TURNOVER_DYNAMIC_CC_3M,
            LDEAL_ACT_DAYS_PCT_TR,
            LDEAL_ACT_DAYS_PCT_TR4,
            LDEAL_ACT_DAYS_PCT_CURR
        ]
    }

    
    try:
        response = requests.post('http://127.0.0.1:5000/predict', json=input_data)
        response_data = response.json()
        
        # to check the error cause
        if 'error' in response_data:
            st.write(f"Error: {response_data['error']}")
        elif 'prediction' in response_data:
            st.write(f'The prediction for the customer is: {response_data["prediction"]}')
        else:
            st.write('Unexpected response# Make request to the Flask API format')
    except Exception as e:
        st.write(f'Error: {str(e)}')

import streamlit as st
import joblib # pyright: ignore[reportMissingImports]

# Load Models
loan_status_model = joblib.load("loan_status_model.pkl")
loan_amount_model = joblib.load("loan_amount_model.pkl")

st.set_page_config(page_title="Loan Prediction System")

st.title("🏦 Loan Prediction System")

tab1, tab2 = st.tabs(
    ["Loan Amount Prediction", "Loan Status Prediction"]
)

# =====================================
# LOAN AMOUNT PREDICTION
# =====================================

with tab1:

    st.header("Predict Loan Amount")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", [0, 1, 2, 3])

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0
    )

    loan_term = st.number_input(
        "Loan Amount Term",
        value=360
    )

    credit_history = st.selectbox(
        "Credit History",
        [0, 1]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Rural", "Semiurban", "Urban"]
    )

    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0

    semiurban = 1 if property_area == "Semiurban" else 0
    urban = 1 if property_area == "Urban" else 0

    if st.button("Predict Loan Amount"):

        features = [[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_term,
            credit_history,
            semiurban,
            urban
        ]]

        prediction = loan_amount_model.predict(features)

        st.success(
            f"Estimated Loan Amount: {prediction[0]:.2f}"
        )

# =====================================
# LOAN STATUS PREDICTION
# =====================================

with tab2:

    st.header("Predict Loan Status")

    gender2 = st.selectbox(
        "Gender",
        ["Male", "Female"],
        key="g"
    )

    married2 = st.selectbox(
        "Married",
        ["Yes", "No"],
        key="m"
    )

    dependents2 = st.selectbox(
        "Dependents",
        [0, 1, 2, 3],
        key="d"
    )

    education2 = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"],
        key="e"
    )

    self_employed2 = st.selectbox(
        "Self Employed",
        ["No", "Yes"],
        key="s"
    )

    applicant_income2 = st.number_input(
        "Applicant Income",
        min_value=0,
        key="a"
    )

    coapplicant_income2 = st.number_input(
        "Coapplicant Income",
        min_value=0,
        key="c"
    )

    loan_amount2 = st.number_input(
        "Loan Amount",
        min_value=0,
        key="l"
    )

    loan_term2 = st.number_input(
        "Loan Amount Term",
        value=360,
        key="t"
    )

    credit_history2 = st.selectbox(
        "Credit History",
        [0, 1],
        key="h"
    )

    property_area2 = st.selectbox(
        "Property Area",
        ["Rural", "Semiurban", "Urban"],
        key="p"
    )

    gender2 = 1 if gender2 == "Male" else 0
    married2 = 1 if married2 == "Yes" else 0
    education2 = 0 if education2 == "Graduate" else 1
    self_employed2 = 1 if self_employed2 == "Yes" else 0

    semiurban2 = 1 if property_area2 == "Semiurban" else 0
    urban2 = 1 if property_area2 == "Urban" else 0

    if st.button("Predict Loan Status"):

        features = [[
            gender2,
            married2,
            dependents2,
            education2,
            self_employed2,
            applicant_income2,
            coapplicant_income2,
            loan_amount2,
            loan_term2,
            credit_history2,
            semiurban2,
            urban2
        ]]

        prediction = loan_status_model.predict(features)

        if prediction[0] == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")
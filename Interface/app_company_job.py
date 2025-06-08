# © 2025 Sangamesh Hulyal
# Licensed under the MIT License
# Original work for academic and personal research use only
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from serpapi import GoogleSearch
from datetime import datetime, timedelta
import pickle
import matplotlib.pyplot as plt
import base64

#fuction for setting Background image(if necessary)
def set_bg(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load the trained SALARY model
with open("Salary_Predictor/salary_model.pkl", 'rb') as file:
    model = pickle.load(file)


# Set page configuration and title
st.set_page_config(page_title="IT-Salary-Job Predictor", layout="centered")
# ✅ Set background image here
set_bg("Interface/ratan_tata_4_.png")

st.title('💼 IT-Salary Predictior',"c" )

# --- User Inputs ---
experience = st.number_input('📅 Years of Experience:', min_value=0)
Age = st.number_input("🎂 Your Age:", min_value=18)
education_level = st.selectbox('🎓 Education Level:', ['Diploma', 'Bachelor', 'Masters', 'PhD'])
job_title = st.selectbox('👔 Job Title:', [
    'Analyst (General-Entry-Level)',
    'Web Developer',
    'Software Developer',
    'Cloud Engineer',
    'AI Engineer',
    'Manager',
    'Director'
])

# --- Prepare Input Data ---
input_data = pd.DataFrame({
    'Experience': [experience],
    'Age': [Age],
    'Education_Bachelor': [1 if education_level == 'Bachelor' else 0],
    'Education_Diploma': [1 if education_level == 'Diploma' else 0],
    'Education_Masters': [1 if education_level == 'Masters' else 0],
    'Education_PhD': [1 if education_level == 'PhD' else 0],
    'Job_Title_AI Engineer': [1 if job_title == 'AI Engineer' else 0],
    'Job_Title_Analyst': [1 if job_title == 'Analyst (General-Entry-Level)' else 0],
    'Job_Title_Cloud Engineer': [1 if job_title == 'Cloud Engineer' else 0],
    'Job_Title_Director': [1 if job_title == 'Director' else 0],
    'Job_Title_Manager': [1 if job_title == 'Manager' else 0],
    'Job_Title_Software Developer': [1 if job_title == 'Software Developer' else 0],
    'Job_Title_Web Developer': [1 if job_title == 'Web Developer' else 0]
})

# --- Predict Salary ---
if st.button('📌 Predict Salary'):
    prediction = model.predict(input_data)[0]

    # Display predicted salary in a styled success box
    st.markdown(
        f"""<div style='padding: 15px; background-color: #1a4d2e; border-radius: 10px; color: white; text-align: center; font-size: 20px;'>
            💰 <strong>Predicted Salary:</strong> ₹{prediction:,.2f} RUPEES
        </div>""",
        unsafe_allow_html=True
    )

    # --- 📈 Salary Comparison Chart ---
    st.markdown("### 📊 Salary Comparison by Job Title")
    job_titles = [
        'Analyst (General-Entry-Level)',
        'Web Developer',
        'Software Developer',
        'Cloud Engineer',
        'AI Engineer',
        'Manager',
        'Director'
    ]

    # Sample prediction using same experience/age with other job titles
    comparison_data = []
    for jt in job_titles:
        row = {
            'Experience': experience,
            'Age': Age,
            'Education_Bachelor': [1 if education_level == 'Bachelor' else 0][0],
            'Education_Diploma': [1 if education_level == 'Diploma' else 0][0],
            'Education_Masters': [1 if education_level == 'Masters' else 0][0],
            'Education_PhD': [1 if education_level == 'PhD' else 0][0],
            'Job_Title_AI Engineer': 1 if jt == 'AI Engineer' else 0,
            'Job_Title_Analyst': 1 if jt == 'Analyst (General-Entry-Level)' else 0,
            'Job_Title_Cloud Engineer': 1 if jt == 'Cloud Engineer' else 0,
            'Job_Title_Director': 1 if jt == 'Director' else 0,
            'Job_Title_Manager': 1 if jt == 'Manager' else 0,
            'Job_Title_Software Developer': 1 if jt == 'Software Developer' else 0,
            'Job_Title_Web Developer': 1 if jt == 'Web Developer' else 0
        }
        df_row = pd.DataFrame([row])
        salary_pred = model.predict(df_row)[0]
        comparison_data.append(salary_pred)

    
    fig, ax = plt.subplots()
    ax.bar(job_titles, comparison_data, color='skyblue', width=0.3)
    ax.set_ylabel("Predicted Monthly Salary (₹)")
    ax.set_xticklabels(job_titles, rotation=45, ha='right')
    fig.tight_layout()
    st.pyplot(fig)

#Lets build a Job and Company Interface

'''---JOB CLASSIFIER INTERFACE 👇 ---'''

# Load JOB and COMPANY models
job_model = joblib.load("JOB_classifier/JOB_model.joblib")
company_model = joblib.load("COMPANY_classifier/COMPANY_model.joblib")

# Load label encoders
job_label = joblib.load("JOB_classifier/JOB_label_encoder.joblib")
company_label = joblib.load("COMPANY_classifier/COMPANY_label_encoder.joblib")

# Define features
internships = ['AIML', 'Cloud', 'Cybersecurity', 'DevOps', 'Software Dev', 'Web Dev']
languages = ['C#', 'C++', 'Go', 'Java', 'JavaScript', 'Python', 'R', 'Rust', 'SQL', 'TypeScript']
technologies = ['AI', 'Backend', 'Big Data', 'Cloud Computing', 'Cybersecurity', 'DBMS',
                'Data Analytics', 'DevOps', 'Front End', 'ML']

st.title("🔮 Job and Company Predictor")

# --- 1. CGPA ---
cgpa = st.slider("🎓 Enter your CGPA", 4.0, 10.0, step=0.1)

if cgpa < 6.0:
    st.markdown(
        "<span style='color:red; font-weight:bold;'>"
        "⚠️ Your CGPA is less than 6, which collapses most companies' eligibility criteria."
        "</span>",
        unsafe_allow_html=True,
    )

# --- 2. Internship types ---
selected_internships = st.multiselect("🛠️ Select Internship Types", internships)

# --- 3. Programming languages ---
selected_languages = st.multiselect("💻 Select Programming Languages", languages)

# --- 4. Technologies ---
selected_technologies = st.multiselect("📡 Select Technologies", technologies)

# Submit
if st.button("🚀 Predict"):

    # Binary encode input
    internship_values = [1 if i in selected_internships else 0 for i in internships]
    lang_values = [1 if l in selected_languages else 0 for l in languages]
    tech_values = [1 if t in selected_technologies else 0 for t in technologies]

    input_vector = [cgpa] + internship_values + lang_values + tech_values
    input_array = np.array(input_vector).reshape(1, -1)

    # --- Job Role Prediction ---
    job_pred_index = job_model.predict(input_array)[0]
    job_pred_label = job_label.inverse_transform([job_pred_index])[0]
    st.success(f"🎯 Predicted Job Role: **{job_pred_label}**")

    # --- Company Prediction (only if CGPA ≥ 6.0) ---
    if cgpa < 6.0:
        st.warning("❌ Company prediction is disabled due to CGPA below 6.")
    else:
        full_input = np.append(input_array[0], job_pred_index).reshape(1, -1)

        company_pred_index = company_model.predict(full_input)[0]
        company_pred_label = company_label.inverse_transform([company_pred_index])[0]
        st.success(f"🏢 Predicted Company: **{company_pred_label}**")

        # Top 3 predictions
        company_proba = company_model.predict_proba(full_input)[0]
        top3_indices = np.argsort(company_proba)[::-1][:3]

        st.subheader("🔝 Top 3 Company Predictions:")
        for idx in top3_indices:
            label = company_label.inverse_transform([idx])[0]
            st.write(f"{label}: **{company_proba[idx]*100:.2f}%**")



        # --- News Fetching using SerpAPI ---
        def get_news(query):
            today = datetime.today()
            last_year = today - timedelta(days=365)
            params = {
                "engine": "google",
                "q": query,
                "tbm": "nws",
                "tbs": f"cdr:1,cd_min:{last_year.strftime('%m/%d/%Y')},cd_max:{today.strftime('%m/%d/%Y')}",
                "api_key": "c515c96adc23d5be418685da68988ff8900e96a4467959fbc9e1ab1aad74da23"#Replace with your Api Key of serp API for good results
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            return results.get("news_results", [])[:3]

        news = get_news(f"{company_pred_label} {job_pred_label}")

        st.subheader("📰 Latest Related News OF Classified Role And Companies(From Past 1 Year):")
        if news:
            for article in news:
                st.markdown(f"### {article['title']}")
                st.write(article["snippet"])
                st.markdown(f"[🔗 Read more]({article['link']})")

                 # Check for higher-res key first
                image_url = article.get("image") or article.get("thumbnail")
                if image_url:
                    st.image(image_url, width=600)  # Adjust as needed

            

























# import streamlit as st
# import numpy as np
# import joblib


# # Load models
# job_model = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/JOB_classifier/JOB_model.joblib")
# company_model = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/COMPANY_classifier/COMPANY_model.joblib")

# # Load label encoders
# job_label = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_project/JOB_classifier/JOB_label_encoder.joblib")
# company_label = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/COMPANY_classifier/COMPANY_label_encoder.joblib")

# # Feature categories
# internship_types = ['AIML', 'Cloud', 'Cybersecurity', 'DevOps', 'Software Dev', 'Web Dev']
# programming_languages = ['C#', 'C++', 'Go', 'Java', 'JavaScript', 'Python', 'R', 'Rust', 'SQL', 'TypeScript']
# technologies = ['AI', 'Backend', 'Big Data', 'Cloud Computing', 'Cybersecurity', 'DBMS',
#                 'Data Analytics', 'DevOps', 'Front End', 'ML']

# st.title("🎓 Job & Company Predictor")

# # --- User Inputs ---
# cgpa = st.slider("Enter your CGPA:", 4.0, 10.0, step=0.1)
# selected_internships = st.multiselect("Select Internship Types (choose at least 1):", internship_types)
# selected_languages = st.multiselect("Select Programming Languages (choose at least 1):", programming_languages)
# selected_tech = st.multiselect("Select Technologies (choose at least 1):", technologies)

# # Ensure all inputs are given
# if st.button("Predict Job & Companies"):
#     if not selected_internships or not selected_languages or not selected_tech:
#         st.warning("⚠️ Please select at least one option from each category before prediction.")
#     else:
#         # Build input vector
#         input_vector = [cgpa]

#         # Internship One-hot
#         for intern in internship_types:
#             input_vector.append(1 if intern in selected_internships else 0)

#         # Language One-hot
#         for lang in programming_languages:
#             input_vector.append(1 if lang in selected_languages else 0)

#         # Technology One-hot
#         for tech in technologies:
#             input_vector.append(1 if tech in selected_tech else 0)

#         input_vector = np.array(input_vector).reshape(1, -1)

#         # Predict Job Role
#         job_pred_index = job_model.predict(input_vector)[0]
#         job_pred_label = job_label.inverse_transform([job_pred_index])[0]

#         st.subheader("🎯 Predicted Job Role:")
#         st.success(f"{job_pred_label}")

#         if cgpa < 6.0:
#             st.error("❌ YOUR CGPA IS LESS THAN 6.0 WHICH COLLAPSES MOST COMPANIES ELIGIBILITY.")
#             st.info("Only Job Role prediction is shown. Company prediction is skipped.")
#         else:
#             # Prepare input for company model
#             job_encoded = job_label.transform([job_pred_label])[0]
#             extended_input = np.append(input_vector, job_encoded).reshape(1, -1)

#             # Predict Top 3 Companies
#             company_probs = company_model.predict_proba(extended_input)[0]
#             top_3_indices = np.argsort(company_probs)[::-1][:3]
#             top_3_companies = company_label.inverse_transform(top_3_indices)
#             top_3_probs = company_probs[top_3_indices]

#             st.subheader("🏢 Top 3 Recommended Companies:")
#             for i, (comp, prob) in enumerate(zip(top_3_companies, top_3_probs), start=1):
#                 st.info(f"{i}. {comp} (Confidence: {prob:.2f})")















# import streamlit as st
# import numpy as np
# import joblib

# # Load models and encoders
# job_model = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/JOB_classifier/JOB_model.joblib")
# company_model = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/COMPANY_classifier/COMPANY_model.joblib")
# job_label = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_project/JOB_classifier/JOB_label_encoder.joblib")
# company_label = joblib.load("C:/Users/sanga/OneDrive/Desktop/Job_Company_Project/COMPANY_classifier/COMPANY_label_encoder.joblib")

# # Input features
# input_features = [
#     'CGPA',
#     'Internship Type_AIML', 'Internship Type_Cloud', 'Internship Type_Cybersecurity',
#     'Internship Type_DevOps', 'Internship Type_Software Dev', 'Internship Type_Web Dev',
#     'Programming Language_C#', 'Programming Language_C++', 'Programming Language_Go',
#     'Programming Language_Java', 'Programming Language_JavaScript', 'Programming Language_Python',
#     'Programming Language_R', 'Programming Language_Rust', 'Programming Language_SQL',
#     'Programming Language_TypeScript',
#     'Technology_AI', 'Technology_Backend', 'Technology_Big Data', 'Technology_Cloud Computing',
#     'Technology_Cybersecurity', 'Technology_DBMS', 'Technology_Data Analytics',
#     'Technology_DevOps', 'Technology_Front End', 'Technology_ML'
# ]

# st.title("Job and Company Predictor App 🚀")

# # Collect user input
# cgpa = st.slider("CGPA", 6.0, 10.0, 8.0)

# internship_options = ['AIML', 'Cloud', 'Cybersecurity', 'DevOps', 'Software Dev', 'Web Dev']
# selected_internship = st.multiselect("Select Internship Types", internship_options)

# programming_options = ['C#', 'C++', 'Go', 'Java', 'JavaScript', 'Python', 'R', 'Rust', 'SQL', 'TypeScript']
# selected_programming = st.multiselect("Select Programming Languages", programming_options)

# tech_options = ['AI', 'Backend', 'Big Data', 'Cloud Computing', 'Cybersecurity',
#                 'DBMS', 'Data Analytics', 'DevOps', 'Front End', 'ML']
# selected_technologies = st.multiselect("Select Technologies", tech_options)

# # Prepare input vector
# def create_input_vector():
#     input_data = [0] * len(input_features)
#     input_data[0] = cgpa

#     for i, col in enumerate(input_features[1:], start=1):
#         feature_name = col.split('_', 1)[-1]
#         if (
#             ('Internship Type' in col and feature_name in selected_internship) or
#             ('Programming Language' in col and feature_name in selected_programming) or
#             ('Technology' in col and feature_name in selected_technologies)
#         ):
#             input_data[i] = 1
#     return np.array(input_data).reshape(1, -1)

# if st.button("Predict Job and Company"):
#     input_vector = create_input_vector()
    
#     # Predict job role
#     job_pred_index = job_model.predict(input_vector)[0]
#     job_pred_label = job_label.inverse_transform([job_pred_index])[0]
#     st.success(f"🎯 Predicted Job Role: **{job_pred_label}**")
    
#     # Add job role to input vector
#     # Append label encoded job role (not one-hot) to input
#     job_role_encoded_value = job_label.transform([job_pred_label])[0]
#     extended_input = np.append(input_vector, job_role_encoded_value).reshape(1, -1)


#     # Predict company
#     company_pred_index = company_model.predict(extended_input)[0]
#     company_pred_label = company_label.inverse_transform([company_pred_index])[0]
#     st.success(f"🏢 Predicted Company: **{company_pred_label}**")



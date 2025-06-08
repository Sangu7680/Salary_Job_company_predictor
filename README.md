# Salary_Job-company_predictior

Acquiring a appropriate job and salary that satisfy rewards one’s efforts has become increasingly difficult for students and fresh graduates. To solve this problem, this project Uses a machine learning approach to estimate ideal job titles and predicted salary ranges based on CGPA, internship, programming, and relevant job technologies for Job role prediction with specific companies. Other components like age, experience, educational background, and type of work were added for salary estimation. A custom dataset reflecting benchmarks of student performance was designed to be structured in a realistically albeit artificially customized fashion. The dataset was subjected to preprocessing like one-hot encoding and stratified train-test split to enable balanced model training. Classification and regression tasks were performed using Random Forest Classifier, Logistic Regression, and Linear Regression machine learning models. The analysis conducted demonstrates the accuracy of predictions if meaningful features are integrated with appropriate ML algorithms when estimating job titles and salaries. Students, educational institutions, and training and placement cells can use the proposed system as a decision-support framework for informed strategic academic and professional engagement.

📚 Research Paper
This project is based on an IEEE-format research paper titled:
"Salary and Job Prediction for Students and Technical Staff Using Machine Learning"
Presented at Tontadarya College of Engineering, Gadag.

📄 View Paper (PDF)

🚀 Key Features

🎯 Salary Prediction: Based on age, experience, education, and job role

🧠 Job Role & Company Prediction: Based on CGPA, internship domain, programming languages, and technologies

📊 Uses multiple ML models: Linear Regression, Logistic Regression, Random Forest

🌐 Simple web interface using Streamlit

🛠️  Technologies Used

Python – pandas, NumPy, scikit-learn

Streamlit – for building the UI

Machine Learning – Linear Regression, Logistic Regression, Random Forest, KNN

Data Preprocessing – One-Hot Encoding, Label Encoding, Stratified Train-Test Split

📁 Setup & Run

1. Clone the Repo

git clone https://github.com/Sangu7680/Salary_Job_company_predictior.git
cd Salary_Job_company_predictior

2.Install Dependencies

pip install -r requirements.txt

3.Run the Streamlit app

Note-Change the Serp api in app_company_job.py file in interface folder to your serp api by creating ur api in serp app and rplacing in the respective file.

streamlit run app.py

4.Open in Browser
U done it and the models are ready for their work in the app interface.
Streamlit will show a URL (like http://localhost:8501) — open it in your browser.


Sample output-

![image](https://github.com/user-attachments/assets/632fe313-8b91-4ab8-866e-ae3b4c391655)

Figure 1: Salary Prediction On specific user input

![image](https://github.com/user-attachments/assets/6d96e305-8bc8-477b-a618-b12108c2a9a2)

Figure 2: Salary Comparision according to other Job titles by taking users given Age, Experience and education

![image](https://github.com/user-attachments/assets/e3a77024-daa5-4a7b-93d4-1388ac9f4163)

Figure 3:Job and company Prediction On specific user input

![image](https://github.com/user-attachments/assets/cb3a2ee4-45d2-44f0-9c8d-7c22fa399a6a)

Figure 4: Top 3 companies Prediction and latest news of those companies.







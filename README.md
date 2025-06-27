
# Resume Screening ML App 💼📄

A machine learning-based web application to automatically predict the most suitable job role from an uploaded resume (PDF format).

## 🚀 Live Demo
🔗 [Click here to try it live](https://resume-screening-ml-v2sukwo6mu3kwxlgudiuym.streamlit.app)

 ⚠️ If the app link doesn't open directly or says "You do not have access",  
 just right-click the link ➜ **Copy link address** ➜ paste it manually into a new browser tab.

## 📌 Features
- Upload a resume in PDF format
- ML model predicts the best-matching job role
- Confidence filtering for irrelevant PDFs
- Clean UI with Streamlit

## 🧠 Tech Stack
- Python
- Scikit-learn
- Streamlit
- PyMuPDF
- TfidfVectorizer + Logistic Regression

## 📂 Project Structure
```
resume-screening-ml/
├── app/
│   ├── app.py           # Streamlit frontend
│   └── predict.py       # ML prediction logic
├── data/
│   └── dataset.csv      # Cleaned training data
├── models/
│   └── model.pkl        # Trained ML model
├── requirements.txt     # Python dependencies
```

## 🛠️ How to Run Locally
```bash
git clone https://github.com/Bhuvanesh1312/resume-screening-ml.git
cd resume-screening-ml
pip install -r requirements.txt
streamlit run app/app.py
```

## 👨‍💻 Made with ❤️ by Bhuvanesh

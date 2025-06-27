import joblib
import re

def clean_resume(text):
    text = re.sub('http\S+|www\S+|\S+@\S+', ' ', text)
    text = re.sub(r'\b\d{10}\b', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = text.lower()
    text = re.sub(r' +', ' ', text)
    return text.strip()

def extract_text_from_pdf(file_path):
    import fitz
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

model = joblib.load('models/model.pkl')

def predict_role(file_path):
    text = extract_text_from_pdf(file_path)
    cleaned = clean_resume(text)
    prediction = model.predict([cleaned])
    return prediction[0]

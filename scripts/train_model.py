import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os
import re

def clean_resume(text):
    text = re.sub('http\S+|www\S+|\S+@\S+', ' ', text)
    text = re.sub(r'\b\d{10}\b', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = text.lower()
    text = re.sub(r' +', ' ', text)
    return text.strip()

data_path = os.path.join('data', 'dataset.csv')
df = pd.read_csv(data_path)

df = df[df['Category'].str.len() < 30]
df['Resume'] = df['Resume'].apply(clean_resume)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=3000)),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(df['Resume'], df['Category'])

os.makedirs('models', exist_ok=True)
joblib.dump(pipeline, 'models/model.pkl')
print("✅ Model training complete and saved.")

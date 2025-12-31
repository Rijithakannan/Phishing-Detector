import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Page Configuration
st.set_page_config(page_title="CyberGuard Phishing Detector", page_icon="🛡️")

# 2. Function to extract features from a URL
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(url.count('.'))
    return features

# 3. Load Data & Train Model (Simple Simulation for Demo)
# In a real scenario, you'd load a massive CSV here.
@st.cache_resource
def train_model():
    # Creating a small synthetic dataset for the demo to ensure it runs
    data = {
        'url_length': [15, 80, 20, 95, 12, 110],
        'has_at': [0, 1, 0, 1, 0, 1],
        'dots': [1, 4, 1, 5, 2, 6],
        'label': [0, 1, 0, 1, 0, 1]  # 0 = Safe, 1 = Phishing
    }
    df = pd.DataFrame(data)
    X = df[['url_length', 'has_at', 'dots']]
    y = df['label']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# 4. User Interface
st.title("🛡️ Phishing Link Detector")
st.write("Enter a URL below to check if it's a potential security threat.")

url_input = st.text_input("Paste URL here:", placeholder="https://example.com")

if st.button("Analyze Link"):
    if url_input:
        # Extract features from user input
        features = extract_features(url_input)
        
        # Predict
        prediction = model.predict([features])
        probability = model.predict_proba([features])[0][1]
        
        if prediction[0] == 0:
            st.success(f"✅ Safe! (Phishing Probability: {probability:.2%})")
            st.balloons()
        else:
            st.error(f"🚨 Warning: This looks like a Phishing Link! (Phishing Probability: {probability:.2%})")
            st.info("Technical Flags: High URL length or unusual character count detected.")
    else:
        st.warning("Please enter a URL first.")
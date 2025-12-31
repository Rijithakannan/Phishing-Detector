# 🛡️ CyberGuard: AI-Powered Phishing Link Detector

### [Live Demo Link](INSERT_YOUR_STREAMLIT_URL_HERE)

## 📌 Overview
**CyberGuard** is a Machine Learning-based security tool designed to identify malicious URLs. While traditional antivirus software relies on databases of known "bad" links, this project uses **Feature Engineering** and the **Random Forest Algorithm** to analyze the structure of a URL and predict if it is a threat in real-time.

## 🚀 Features
* **Real-time Analysis:** Get instant results on whether a link is safe or dangerous.
* **ML-Based Detection:** Analyzes URL length, special characters, and subdomain patterns.
* **Probability Scoring:** Shows the confidence level of the prediction.
* **Clean UI:** Built with a modern, responsive interface using Streamlit.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Manipulation:** Pandas
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Community Cloud

## 📊 How It Works
The system extracts specific features from a URL that are common in phishing attempts:
1.  **URL Length:** Phishing links are often significantly longer than legitimate ones.
2.  **Special Characters:** Checking for `@` symbols and excessive hyphens `-`.
3.  **Subdomain Counts:** Identifying "squatting" (e.g., `paypal.secure-login.com`).
4.  **HTTPS Check:** Verifying secure protocol usage.

## 📂 Project Structure
```text
├── app.py              # Main application logic and UI
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🔧 Installation & Local Setup
Clone the repository:
https://github.com/Rijithakannan/Phishing-Detector.git
Install dependencies:
pip install -r requirements.txt
Run the application:
python -m streamlit run app.py
🎓 Academic Credit
Course: B.Tech Information Technology

Project Type: Cybersecurity / Machine Learning

Author: rijitha

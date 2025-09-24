# Spam Detection Web App

This project classifies messages as spam or not spam using a trained machine learning model and provides a simple web interface for predictions.

## Features
- Predicts whether a message is **spam** or **not spam**.
- User-friendly **Flask web interface**.
- Supports bulk predictions with preprocessed text.
- Easy to deploy and extend.

## Tech Stack
- Python
- Flask
- scikit-learn
- Pandas
- Pickle (for model & vectorizer)

## ⚙️ How It Works
1. **Input:** Enter a message in the web interface.
2. **Preprocessing:** Text is cleaned and vectorized using the trained vectorizer.
3. **Prediction:** The model predicts if the message is **spam** or **not spam**.
4. **Output:** The result is displayed on the web page.

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/akshaysharma1740/spam_detection.git
cd spam_detection
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python app.py

Open your browser and go to http://127.0.0.1:5000 to start predicting.

📊 Example Output
User enters: "Congratulations! You won a lottery."
Output: Spam
User enters: "Hey, are we meeting tomorrow?"
Output: Not Spam
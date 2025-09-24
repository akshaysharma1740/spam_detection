# Spam Classifier Flask App

This project is a **Flask web application** that predicts whether a message is **Ham** or **Spam** using a LinearSVC model trained with GridSearch.

---

## **Features**

- Predicts **Ham** or **Spam** messages instantly.  
- Uses a trained **LinearSVC model with GridSearch** for accurate predictions.  
- Text cleaning and preprocessing with **spaCy**.  
- Simple and user-friendly **web interface**.

---

## **Tech Stack**

- Python 
- Flask  
- scikit-learn  
- Pandas  
- spaCy  

---

## **⚙️ How It Works**

1. **Input:** User enters a text message in the web app.  
2. **Preprocessing:** Text is cleaned and lemmatized using spaCy.  
3. **Prediction:** The trained LinearSVC model predicts **Ham** or **Spam**.  
4. **Output:** The app displays the prediction instantly on the webpage.

---

## **🚀 Getting Started**

1. **Clone the repository**
```bash
git clone https://github.com/akshaysharma1740/spam_detection.git
cd spam_detection

import pickle
from flask import Flask, request, render_template
import spacy

app = Flask(__name__)

# -----------------
# Load model/vectorizer
# -----------------
with open("artifacts/best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# -----------------
# Load spaCy model for preprocessing
# -----------------
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# -----------------
# Main page route
# -----------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = ""

    if request.method == "POST":
        message = request.form["message"]

        clean_message = preprocess_text(message)

        X_new = vectorizer.transform([clean_message])
        pred = model.predict(X_new)[0]

        label_map = {0: "ham", 1: "spam"}
        prediction = label_map.get(pred, pred)

    return render_template("index.html", prediction=prediction, message=message)

# -----------------
# Run app
# -----------------
if __name__ == "__main__":
    app.run(debug=True)

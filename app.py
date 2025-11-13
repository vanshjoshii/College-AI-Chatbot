import google.generativeai as genai
import markdown
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# 🔑 Configure Gemini
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json["message"]

    try:
        response = model.generate_content(user_query)
        # Convert markdown response to HTML
        html_response = markdown.markdown(response.text)
        return jsonify({"response": html_response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

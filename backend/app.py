from flask import Flask, request, jsonify
from chatbot import get_chatbot_response
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Perform sentiment analysis
    sentiment = analyze_sentiment(user_message)

    # Generate chatbot response
    bot_response = get_chatbot_response(user_message, sentiment)

    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

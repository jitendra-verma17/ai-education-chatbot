from flask import Flask, request, jsonify

app = Flask(__name__)
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."
    elif "study" in user_input:
        return "Make a timetable and practice daily."
    else:
        return "Sorry, I didn't understand."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

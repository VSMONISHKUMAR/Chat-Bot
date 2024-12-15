from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
DATA_FILE = "data.json"
def initialize_json():
    try:
        with open(DATA_FILE, "r") as file:
            pass 
    except FileNotFoundError:
        with open(DATA_FILE, "w") as file:
            json.dump([], file)  
def read_chat_history():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
def write_chat_history(history):
    with open(DATA_FILE, "w") as file:
        json.dump(history, file, indent=4)
def generate_response(user_message):
    if "hello" in user_message or "hi" in user_message or "hlo" in user_message:
        return "Hi there! How can I assist you today?"
    elif "price" in user_message or "cost" in user_message:
        return "Can you specify which product you're asking about?"
    elif "help" in user_message or "assist" in user_message:
        return "Sure, I'm here to help! Please provide more details."
    elif "thank" in user_message or "thanks" in user_message:
        return "You're welcome! Let me know if you need anything else."
    elif "order status" in user_message or "where is my order" in user_message or "order" in user_message:
        return "Could you please provide your order ID? I'll check the status for you."
    elif "product" in user_message :
        return "Could you please provide your Product Details ? I'll check the status for you."
    elif "late delivery" in user_message or "delayed" in user_message:
        return "I'm sorry for the delay. Let me check the latest update on your delivery."
    elif "damaged product" in user_message or "broken item" in user_message:
        return "I'm really sorry to hear that. Could you please share your order ID and a brief description of the issue? We’ll resolve it as quickly as possible."
    elif "wrong product" in user_message or "incorrect item" in user_message:
        return "I apologize for the inconvenience. Could you share your order ID so we can arrange for a replacement or refund?"
    elif "refund" in user_message or "return" in user_message:
        return "Refunds and returns are our priority! Please share your order ID and issue so we can assist you further."
    elif "cancel" in user_message or "cancel order" in user_message:
        return "If you'd like to cancel your order, please provide the order ID. I'll check if it's still possible."
    elif "replacement" in user_message or "exchange" in user_message:
        return "If you need a replacement, please share your order ID and the issue with the product. I'll help you with the next steps."
    elif "tracking" in user_message or "track order" in user_message:
        return "Please provide your order ID, and I'll share the tracking details with you."
    elif "delivery address" in user_message or "wrong address" in user_message:
        return "If there's an issue with your delivery address, let us know your order ID and the correct address. We'll look into it immediately."
    elif "complaint" in user_message or "feedback" in user_message:
        return "We value your feedback. Please let us know your concerns so we can improve our service."
    elif "contact support" in user_message or "speak to a human" in user_message:
        return "Sure, I can connect you to one of our support agents. Please wait for a moment."
    elif "product warranty" in user_message or "warranty claim" in user_message:
        return "For warranty claims, please provide the product details and order ID. We’ll assist you further."
    elif "lost package" in user_message or "missing order" in user_message:
        return "I'm sorry to hear that your package is missing. Please share your order ID so we can investigate this for you."
    elif "offer" in user_message or "discount" in user_message:
        return "We have amazing offers and discounts! Let me know the product you’re interested in, and I’ll share the details."
    elif "delivery time" in user_message or "expected date" in user_message:
        return "Let me know your order ID, and I’ll check the estimated delivery time for you."
    elif "apology" in user_message:
        return "I sincerely apologize for the inconvenience caused. We’re doing our best to resolve this for you."
    elif "escalate" in user_message:
        return "I understand your frustration. Let me escalate this issue to our higher support team for quicker resolution."
    elif "confirmation" in user_message or "confirm order" in user_message:
        return "Could you share your order ID so I can confirm the details for you?"
    else:
        return "I'm not sure about that. Could you please provide more details so I can assist you better?"
@app.route('/chat', methods=['POST'])
def chat():  
    initialize_json()
    chat_history = read_chat_history()   
    data = request.get_json()
    user_message = data.get('message')
    if user_message:       
        bot_response = generate_response(user_message)       
        new_entry = {"user": user_message, "bot": bot_response}
        chat_history.append(new_entry)
        write_chat_history(chat_history)
        return jsonify({"chat": new_entry})
    else:
        return jsonify({"error": "Message not provided"}), 400
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

# META CONFIGURATION

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


# WEBHOOK VERIFICATION

@app.route("/webhook", methods=["GET"])
def verify_webhook():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK VERIFIED")
        return challenge, 200

    return "Verification failed", 403


# RECEIVE MESSAGES

@app.route("/webhook", methods=["POST"])
def receive_message():

    data = request.get_json()

    print("\n===== NEW WEBHOOK EVENT =====")
    print(data)

    if data.get("object") == "page":

        for entry in data.get("entry", []):

            for messaging_event in entry.get("messaging", []):

                sender = messaging_event.get("sender", {})
                message = messaging_event.get("message", {})

                sender_id = sender.get("id")
                message_text = message.get("text")

                if message_text:
                    print(f"Sender ID: {sender_id}")
                    print(f"Message: {message_text}")

    return "EVENT_RECEIVED", 200


# HOME

@app.route("/")
def home():
    return "JCSGO Messenger Bot is running!"


# RUN SERVER

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
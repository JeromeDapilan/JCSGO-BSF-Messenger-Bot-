from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)


# META CONFIGURATION


VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")



# CHURCH INFORMATION


SUNDAY_SERVICE = "9:00 AM"

CHURCH_ADDRESS = (
    "099 Mabuhay Street, Sitio Veterans, "
    "Barangay Bagong Silangan, Quezon City"
)

GOOGLE_MAPS = "https://maps.app.goo.gl/RHXsQXyE9KtyZq2YA"

FACEBOOK_PAGE = "JCSGO Bagong Silangan Family"

EMAIL = "jcsgobsmultimedia@gmail.com"



# SEND MESSAGE


def send_message(recipient_id, message_text):

    url = "https://graph.facebook.com/v26.0/me/messages"

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    }

    response = requests.post(
        url,
        params=params,
        json=payload
    )

    print(
        "SEND MESSAGE STATUS:",
        response.status_code,
        flush=True
    )

    print(
        "SEND MESSAGE RESPONSE:",
        response.text,
        flush=True
    )



# CHATBOT RESPONSE


def get_bot_response(message_text):

    message = message_text.lower().strip()


    
    # GREETING
    

    if any(word in message for word in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):

        return (
            "Magandang araw! 🙏 Maligayang pagdating sa "
            "JCSGO Bagong Silangan Family Facebook Page!\n\n"
            
            "Salamat sa pag-message sa amin. Masaya kaming makausap kayo.\n\n\n"


            "Paano po namin kayo matutulungan?"
        )


    
    # SUNDAY SERVICE
    

    elif (
        "sunday service" in message
        or "sunday worship" in message
        or "church service" in message
        or "service schedule" in message
        or message == "service"
        or "what time is your service" in message
        or "what time is church" in message
        or "anong oras ang service" in message
        or "anong oras ang church" in message
    ):

        return (
            "🕊️ SUNDAY SERVICE\n\n"
            f"Our Sunday Service starts at {SUNDAY_SERVICE}.\n"
            "We would be blessed to worship with you!\n\n"

            "🕊️ SUNDAY SERVICE\n\n"
            f"Ang ating Sunday Service ay nagsisimula ng {SUNDAY_SERVICE}.\n"
            "Inaanyayahan po namin kayo na sama-sama tayong "
            "sumamba at makinig sa Salita ng Diyos. 🙏"
        )


    
    # LOCATION
    

    elif any(word in message for word in [
        "location",
        "address",
        "where are you",
        "where is your church",
        "saan kayo",
        "saan ang church",
        "saan yung church",
        "nasaan kayo",
        "address nyo",
        "location nyo"
    ]):

        return (
            "📍 CHURCH LOCATION\n\n"
            f"Our church is located at:\n"
            f"{CHURCH_ADDRESS}\n\n"

            f"🗺️ Google Maps:\n{GOOGLE_MAPS}\n\n"

            "📍 LOKASYON NG SIMBAHAN\n\n"
            f"Matatagpuan po ang ating church sa:\n"
            f"{CHURCH_ADDRESS}\n\n"

            "Maaari po ninyong gamitin ang Google Maps link "
            "para mas madaling mahanap ang location namin. 😊"
        )


    
    # CONTACT
    

    elif any(word in message for word in [
        "contact",
        "contact us",
        "email",
        "e-mail",
        "how can i contact you",
        "paano kayo makontak",
        "contact information",
        "contact info"
    ]):

        return (
            "📞 CONTACT INFORMATION\n\n"
            f"Facebook Page: {FACEBOOK_PAGE}\n"
            f"Email: {EMAIL}\n\n"

            "📞 CONTACT INFORMATION\n\n"
            f"Facebook Page: {FACEBOOK_PAGE}\n"
            f"Email: {EMAIL}\n\n"

            "Feel free to send us a message anytime.\n"
            "Maaari po kayong mag-message sa amin kung mayroon "
            "kayong mga katanungan. 🙏"
        )


    
    # ABOUT JCSGO
    

    elif any(word in message for word in [
        "about",
        "about jcsgo",
        "what is jcsgo",
        "what is your church",
        "tell me about jcsgo",
        "jcsgo"
    ]):

        return (
            "⛪ ABOUT JCSGO BAGONG SILANGAN FAMILY\n\n"

            "JCSGO Bagong Silangan Family is a Christian church "
            "community committed to worshiping God, growing in faith, "
            "and serving others.\n\n"

            "⛪ TUNGKOL SA JCSGO BAGONG SILANGAN FAMILY\n\n"

            "Ang JCSGO Bagong Silangan Family ay isang Christian "
            "church community na naglalayong sumamba sa Diyos, "
            "lumago sa pananampalataya, at maglingkod sa kapwa.\n\n"

            "Everyone is welcome to worship and fellowship with us. ❤️"
        )


    
    # PRAYER REQUEST
    

    elif any(word in message for word in [
        "prayer",
        "prayer request",
        "pray for me",
        "please pray",
        "panalangin",
        "prayer po",
        "ipagdasal"
    ]):

        return (
            "🙏 PRAYER REQUEST\n\n"

            "We would be honored to pray with you. "
            "Please send us your prayer request and our team "
            "will be glad to pray with you.\n\n"

            "🙏 PANALANGIN\n\n"

            "Ikagagalak po naming makasama kayo sa panalangin. "
            "Ipadala lamang po ang inyong prayer request at "
            "ipapanalangin po namin kayo.\n\n"

            "God bless you! ❤️"
        )


    
    # GENERAL HELP
    

    elif any(word in message for word in [
        "help",
        "menu",
        "information",
        "info",
        "what can you do",
        "ano ang pwede",
        "ano pwede"
    ]):

        return (
            "🤖 HOW CAN I HELP YOU?\n\n"

            "You can ask me about:\n"
            "🕊️ Sunday Service\n"
            "📍 Church Location\n"
            "📞 Contact Information\n"
            "⛪ About JCSGO\n"
            "🙏 Prayer Request\n\n"

            "🤖 PAANO KO PO KAYO MATUTULUNGAN?\n\n"

            "Maaari po kayong magtanong tungkol sa:\n"
            "🕊️ Sunday Service\n"
            "📍 Location ng Church\n"
            "📞 Contact Information\n"
            "⛪ Tungkol sa JCSGO\n"
            "🙏 Prayer Request"
        )


    
    # DEFAULT RESPONSE
    

    else:

        return (
            "Thank you for messaging JCSGO Bagong Silangan Family! 🙏\n\n"
            "I'm here to help you with information about our "
            "Sunday Service, church location, contact information, "
            "and prayer requests.\n\n"

            "Salamat po sa pag-message sa JCSGO Bagong Silangan Family! 🙏\n\n"
            "Maaari po kayong magtanong tungkol sa ating "
            "Sunday Service, church location, contact information, "
            "o prayer request.\n\n"

            "Type 'Help' to see the available options. 😊"
        )



# WEBHOOK VERIFICATION


@app.route("/webhook", methods=["GET"])
def verify_webhook():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:

        print(
            "WEBHOOK VERIFIED",
            flush=True
        )

        return challenge, 200

    return "Verification failed", 403



# RECEIVE MESSAGES


@app.route("/webhook", methods=["POST"])
def receive_message():

    data = request.get_json()

    print(
        "\n===== NEW WEBHOOK EVENT =====",
        flush=True
    )

    print(
        data,
        flush=True
    )


    if data.get("object") == "page":

        for entry in data.get("entry", []):

            for messaging_event in entry.get(
                "messaging",
                []
            ):

                sender = messaging_event.get(
                    "sender",
                    {}
                )

                message = messaging_event.get(
                    "message",
                    {}
                )

                sender_id = sender.get("id")

                message_text = message.get("text")


                if message_text:

                    print(
                        f"Sender ID: {sender_id}",
                        flush=True
                    )

                    print(
                        f"Message: {message_text}",
                        flush=True
                    )


                    # GET CHATBOT RESPONSE

                    reply = get_bot_response(
                        message_text
                    )


                    # SEND CHATBOT RESPONSE

                    send_message(
                        sender_id,
                        reply
                    )


    return "EVENT_RECEIVED", 200



# HOME


@app.route("/")
def home():

    return "JCSGO Messenger Bot is running!"



# RUN SERVER


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )

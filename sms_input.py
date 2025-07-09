# sms_input.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from text_analysis import extract_keywords_and_topics

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    """Respond to incoming SMS messages and extract topics"""
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    print(f"📩 SMS Received from {sender}: {incoming_msg}")

    # Analyze the message content
    topics = extract_keywords_and_topics(incoming_msg)

    # Send an auto-reply
    response = MessagingResponse()
    response.message("Thank you for your report. We are analyzing your input for action.")

    # Optional: Save the message and topic to database or file
    with open("sms_logs.txt", "a") as log:
        log.write(f"{sender}: {incoming_msg} | Topics: {topics}\n")

    return str(response)

if __name__ == "__main__":
    print("🚀 Starting SMS server...")
    app.run(debug=True)

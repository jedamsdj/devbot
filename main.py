__author__ = 'Devon'

import os
from twilio.rest import TwilioRestClient


# Access the environment variables for TWILIO and Google
GOOGLE_SHEET_KEY = os.environ.get('GOOGLE_SHEET_KEY')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')


# Send a text
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
client.messages.create(
    to="15855904906",
    from_=TWILIO_PHONE_NUMBER,
    body="This is just a test.")

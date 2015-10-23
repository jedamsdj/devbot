import sys
from devbot import Spreadsheet, Phone

__author__ = 'Devon'


def send_text(message, phone, gsheet):
    for number in enumerate(gsheet.texting_number_list()):
        phone.send_text(number, message)

sheet = Spreadsheet()
phone = Phone()

input_arguments = sys.argv
if len(input_arguments) > 1:
    day = input_arguments[1]
else:
    day = ''

if day.lower() == 'friday':
    text_message = sheet.messages['standard message f']
    send_text(text_message, phone, sheet)
elif day.lower() == 'saturday':
    text_message = sheet.messages['standard message s']
    send_text(text_message, phone, sheet)
else:
    text_message = sheet.messages['standard message f']
    send_text(text_message, phone, sheet)

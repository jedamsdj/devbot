import sys
from devbot import Spreadsheet, Phone

__author__ = 'Devon'


sheet = Spreadsheet()
phone = Phone()

input_arguments = sys.argv
if len(input_arguments) > 1:
    day = input_arguments[1]
else:
    day = ''

if day.lower() == 'friday':
    text_message = sheet.messages['standard message f']
elif day.lower() == 'saturday':
    text_message = sheet.messages['standard message s']
else:
    text_message = sheet.messages['standard message f']

phone.send_text(sheet.texting_number_list(), text_message)

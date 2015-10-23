from devbot import Spreadsheet, ResponseAI
import sys

number = sys.argv[1]
text = ''
for word in sys.argv[2:]:
    text += word + ' '
text = text.rstrip()
text = text.lstrip()
text = text.lstrip('+')

try:
    sheet = Spreadsheet()
    response = ResponseAI(number, sheet, text)

    if response.recognized_member:
        if response.name == 'temp':
            response.add_member_to_spreadsheet()
        else:
            response.get_response_from_member()
    else:
        response.get_response_from_nonmember()
    print response.execute_response()

except IOError:
    print 'Sorry, something went wrong. Text back in a little bit!'

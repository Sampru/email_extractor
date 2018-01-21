import email
from utils import string_utils


class Email_model:

    def __init__(self, raw_email):
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        self.email_from = string_utils.find_between(email_from, '<', '>')

    def get_from(self):
        return self.email_from
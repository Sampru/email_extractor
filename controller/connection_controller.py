import imaplib
import email
from model import email_model

class Connection_controller:

    def __init__(self):
        IMAP_SERVER = "imap.gmail.com"
        IMAP_PORT = 993
        self.conn = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

    def open_connection(self, username, password):
        self.conn.login(username, password)

    def search_in_tag(self, inbox):
        emails = []
        self.conn.select(inbox)
        print('Consultando correo...')
        response, search_data = self.conn.search(None, 'ALL')
        if not response == 'OK':
            print('La busqueda acabo con error: %s' % response)
            raise imaplib.IMAP4.error
        print('%d elementos encontrados' % len(search_data[0]))
        for i in search_data[0].split():
            response, mail_data = self.conn.fetch(i, '(RFC822)')
            if not response == 'OK':
                print('No se ha podido leer email: %s' % response)
                raise imaplib.IMAP4.error
            email = email_model.Email_model(mail_data[0][1])
            emails.append(email.get_from())
        return emails


    def close_connection(self):
        self.conn.close()

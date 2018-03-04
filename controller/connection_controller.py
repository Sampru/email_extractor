import imaplib
import email
from model import email_model

class Connection_controller:

    def open_connection(self, username, password):
        servers = {'gmail'   : 'imap.gmail.com',
                   'outlook' : 'outlook.office365.com',
                   'hotmail' : 'outlook.office365.com'}
        server_name = '.'.join(username.split('@')[1].split('.')[:-1])
        self.IMAP_SERVER = servers.get(server_name ,'imap.gmail.com')
        self.IMAP_PORT = 993
        self.conn = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
        self.conn.login(username, password)

    def search_in_tag(self, inbox):
        emails = []
        next_print = 0
        self.conn.select(inbox)
        print('Consultando correo...')
        response, search_data = self.conn.search(None, 'ALL')
        if not response == 'OK':
            print('La busqueda acabo con error: %s' % response)
            raise imaplib.IMAP4.error
        num_email = len(search_data[0].split())
        print('%d elementos encontrados' % num_email)
        for i in search_data[0].split():
            percentage = int(i)*100/num_email
            if percentage > next_print :
                print('%d emails de %d (%d%s)' % (int(i), num_email, int(percentage), '%'))
                next_print += 10
            response, mail_data = self.conn.fetch(i, '(RFC822)')
            if not response == 'OK':
                print('No se ha podido leer email: %s' % response)
                raise imaplib.IMAP4.error
            email = email_model.Email_model(mail_data[0][1])
            emails.append(email.get_from())
        return emails


    def close_connection(self):
        self.conn.close()

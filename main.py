import imaplib
import getpass
from controller import connection_controller
from utils import string_utils

CONTROLLER = connection_controller.Connection_controller()


def login():
    logged = False
    while not logged:
        try:
            uname = input('Usuario: ')
            pword = getpass.getpass('Contraseña: ')
            print('Iniciando sesion para: %s' % uname)
            CONTROLLER.open_connection(uname, pword)
            logged = True
            print('Sesion iniciada correctamente')
        except imaplib.IMAP4.error:
            print('Credenciales incorrectas')
            logged = False


def search():
    inbox = input('Seleciona una carpetas (para subcarpetas separar por /): ')
    try:
        emails = CONTROLLER.search_in_tag(inbox)
        string_utils.create_output(emails)
    except imaplib.IMAP4.error:
        print('Ha habido un problema con el tratamiento.')


if __name__ == '__main__':
    login()
    search()
    CONTROLLER.close_connection()
    input('Press enter to finish')

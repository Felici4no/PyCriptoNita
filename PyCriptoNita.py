import string
import random


def show_banner():
    banner = """
    ############################################################
    #                                                          #
    #                  Welcome to PyCriptoNita                 #
    #                                                          #
    #              Secure your text with ease and style!       #
    #                                                          #
    ############################################################
    """
    print(banner)

all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + " ÇçÃãÕõÁáÉéÍíÓóÚúÂâÊêÎîÔôÛûÀàÈèÌìÒòÙùÄäËëÏïÖöÜü"
print(all_characters)
def key_generator(all_characters):
    list_characters = list(all_characters)
    random.shuffle(list_characters)
    key = ''.join(list_characters)
    return key

def input_msg():
    while True:
        msg = input("Enter your message: ")
        if len(msg) < 1:
            print('\n- insert a larger message.\n')
        elif msg.isspace():
            print('\n- it is just space.\n')
        else:
            return msg
            break

def encrypt_msg(msg):
    encrypted = ''
    for i in range(len(msg)):
        if msg[i] in all_characters:

msg = input_msg()
print(msg)
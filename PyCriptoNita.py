import string
import random
print('.PyCriptoNita')

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


# Todos os caracteres, incluindo letras, dígitos, pontuações e caracteres especiais
all_characters = (
    string.ascii_uppercase +  # Letras maiúsculas A-Z
    string.ascii_lowercase +  # Letras minúsculas a-z
    string.digits +           # Dígitos 0-9
    string.punctuation +      # Pontuações
    " ñÑÇçÃãÕõÁáÉéÍíÓóÚúÂâÊêÎîÔôÛûÀàÈèÌìÒòÙùÄäËëÏïÖöÜü"  # Caracteres especiais
)

#print(all_characters)

def key_generator(all_characters):
    list_characters = list(all_characters)
    random.shuffle(list_characters)
    key = ''.join(list_characters)
    return key
key = key_generator(all_characters)
def input_msg():

    while True:
        msg = input("Enter your message: ")
        if len(msg) < 1:
            print('\n- Insert a larger message.\n')
        elif msg.isspace():
            print('\n- It is just space.\n')
        else:
            return msg

def encrypt_msg(msg):
    criptonita = ''
    for i in range(len(msg)):
        if msg[i] in key:
            x = key.index(msg[i])
            criptonita += key[(x + 1) % len(key)]
        else:
            criptonita += msg[i]
    return criptonita

def decrypt_msg(encrypted_msg):
    original_msg = ''
    for i in range(len(encrypted_msg)):
        if encrypted_msg[i] in key:
            x = key.index(encrypted_msg[i])
            original_msg += key[(x - 1) % len(key)]
        else:
            original_msg += encrypted_msg[i]
    return original_msg

# Testando
'''
decrypted_message = decrypt_msg(encrypted_message)
print("Decrypted Message:", decrypted_message)
'''
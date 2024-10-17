import string
import random

print('.PyCriptoNita')

def space(lines):
    for x in range(lines):
        print('\n')

def line():
    print('    ############################################################')
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
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation +
    " ñÑÇçÃãÕõÁáÉéÍíÓóÚúÂâÊêÎîÔôÛûÀàÈèÌìÒòÙùÄäËëÏïÖöÜü"
)

# Função para gerar chave de criptografia
def key_generator(all_characters):
    list_characters = list(all_characters)
    random.shuffle(list_characters)
    key = ''.join(list_characters)
    return key

# Função para receber uma mensagem de entrada
def input_msg():
    while True:
        msg = input("Enter your message: ")
        if len(msg) < 1:
            print('\n- Insert a larger message.\n')
        elif msg.isspace():
            print('\n- It is just space.\n')
        else:
            return msg

# Função para criptografar a mensagem
def encrypt_msg(msg, key):
    criptonita = ''
    for i in range(len(msg)):
        if msg[i] in key:
            x = key.index(msg[i])
            criptonita += key[(x + 1) % len(key)]
        else:
            criptonita += msg[i]
    return criptonita

# Função para descriptografar a mensagem
def decrypt_msg(encrypted_msg, key):
    original_msg = ''
    for i in range(len(encrypted_msg)):
        if encrypted_msg[i] in key:
            x = key.index(encrypted_msg[i])
            original_msg += key[(x - 1) % len(key)]
        else:
            original_msg += encrypted_msg[i]
    return original_msg

# Função principal para interação com o usuário
def main():
    show_banner()
    key = key_generator(all_characters)  # Gera a chave uma vez ao iniciar o programa

    while True:
        user = input('[1] Encrypt\n[2] Decrypt\n[3] Last key\n[4] Generate key\n[5] About\n[6] Quit\n - ')
        if user == '6':
            print('PyCriptoNita is dead.')
            break
        elif user == '1':
            message = input_msg()
            encrypted_message = encrypt_msg(message, key)
            print("Encrypted Message:", encrypted_message)
        elif user == '2':
            encrypted_msg = input('Enter your encrypted message: ')
            if len(key) == 143:
                decrypted_message = decrypt_msg(encrypted_msg, key)
                print("Decrypted Message:", decrypted_message)
            else:
                print('This is not a valid key\n\n\n\n')
        elif user == '3':
            print('Last key:')
            print(key)
        elif user == '4':
            key = key_generator(all_characters)  # Gera uma nova chave
            print("New key generated.")
        elif user == '5':
            show_banner()
            print('    By Felici4no')
            print('    https://github.com/Felici4no/PyCriptoNita')
            space(1)
            line()

# Executa a função principal
if __name__ == "__main__":
    main()
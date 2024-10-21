from mod.pretty import clear_terminal, get_escape
print('.main')

# importando a classe principal do módulo criado
from pycriptonita import PyCriptoNita

# executando a função dessa mesma classe
PyCriptoNita.run()

# testando apenas os comandos acima, o resto não deverá ser executado
exit()

"""
key = key_generator(all_characters)

while True:

    clear_terminal()
    show_banner()
    
    user = input('[1] Encrypt\n[2] Decrypt\n[3] Last key\n[4] Generate key\n[5] About\n[6] Quit\n - ')

    match user:

        case '6':
            break
        
        case '1':
            message = input_msg()
            encrypted_message = encrypt_msg(message, key)
            print("Encrypted Message:", encrypted_message)

        case '2':

            encrypted_msg = input('Enter your message: ')
            provided_key = input('Enter your key: ')

            if len(provided_key) == len(key):
                decrypted_message = decrypt_msg(encrypted_msg, provided_key)
                print("Decrypted Message:", decrypted_message)
            else:
                print('This is not a valid key\n\n\n\n')

        case '3':

            print('Last key:')
            print(key)

        case '4':

            key = key_generator(all_characters)
            print("New key generated.")

        case '5':
            show_banner()

        case _:

           print("Unexpected input") 

print('{}PyCriptoNita is dead.{}'.format(get_escape(1, 31), get_escape()))
"""

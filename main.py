from PyCriptoNita import *
print('.main')
show_banner()

key = key_generator(all_characters)

while True:
    user = input('[1] Encrypt\n[2] Decrypt\n[3] Last key\n[4] Generate key\n[5] About\n[6] Quit\n - ')
    if user == '6':
        break
    elif user == '1':
        message = input_msg()
        encrypted_message = encrypt_msg(message, key)
        print("Encrypted Message:", encrypted_message)
    elif user == '2':
        encrypted_msg = input('Enter your message: ')
        provided_key = input('Enter your key: ')
        if len(provided_key) == len(key):
            decrypted_message = decrypt_msg(encrypted_msg, provided_key)
            print("Decrypted Message:", decrypted_message)
        else:
            print('This is not a valid key\n\n\n\n')
    elif user == '3':
        print('Last key:')
        print(key)
    elif user == '4':
        key = key_generator(all_characters)
        print("New key generated.")
    elif user == '5':
        show_banner()

print('PyCriptoNita is dead.')
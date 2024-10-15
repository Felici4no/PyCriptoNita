from PyCriptoNita import *
show_banner()

message = input_msg()
encrypted_message = encrypt_msg(message)
print("Encrypted Message:", encrypted_message)
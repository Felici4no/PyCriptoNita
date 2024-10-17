## PyCriptoNita

**PyCriptoNita** is a simple Python script designed to encrypt and decrypt text messages using a randomly generated substitution cipher. 

### How it works:
1. **Key Generation:** A unique key is created by randomly shuffling all possible characters (letters, digits, punctuation, and special characters).
2. **Encryption:** Each character in the input message is replaced with the corresponding character in the key, shifted by one position to the right.
3. **Decryption:** The encrypted message is decrypted by reversing the encryption process, shifting each character in the encrypted message one position to the left.

### Usage:
1. **Run the script:** Execute the `main.py` file.
2. **Enter your message:** The script will prompt you to input the message you want to encrypt or decrypt.
3. **View the result:** The encrypted or decrypted message will be displayed on the console.

### Example:
```
Enter your message: Hello, world!

Encrypted message: Ifmmpx, yxovl!
```

### Note:
- The security of this encryption method is limited.
- The script assumes that the same key is used for both encryption and decryption. In a real-world application, the key should be securely distributed to authorized parties.

### Future enhancements:
- Implement different encryption algorithms.
- Allow users to choose the key.
- Provide options for saving and loading encrypted messages.
- Add a graphical user interface for easier interaction.
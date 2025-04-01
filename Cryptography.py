from Crypto.Cipher import AES
from Crypto.Hash import SHA256, SHA3_256
from Crypto.Random import get_random_bytes
import base64


class Cryptography:

    def generate_aes_key(self):
        return get_random_bytes(32)

    def encrypt_aes(self, key, plaintext):
        #create random 16 byte Initialization Vector
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        #AES requires the text to be a length of 16 so this adds some padding
        padding_length = 16 - (len(plaintext) % 16)
        padded_text = plaintext + (chr(padding_length) * padding_length)

        ciphertext = cipher.encrypt(padded_text.encode())

        #return the ciphertext with the IV concatenated in front all in byte format
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt_aes(self, key, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        #seperate the IV from the actual "data"
        iv, ciphertext = encrypted_data[:16], encrypted_data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        #decrypt the ciphertext and use .decode() to turn it back into a readable string
        decrypted_padded = cipher.decrypt(ciphertext).decode()

        padding_length = ord(decrypted_padded[-1])
        return decrypted_padded[:-padding_length]

    def sha3(self, message):
        #hashes the input and returns the message digest
        hasher = SHA3_256.new(message.encode())
        return hasher.hexdigest()



if __name__ == "__main__":
    crypto = Cryptography()
    plaintext = "Hello World!"
    print("Original Text: " + plaintext)
    # AES Example
    aes_key = crypto.generate_aes_key()
    print("AES Key: " + base64.b64encode(aes_key).decode())

    encrypted_text = crypto.encrypt_aes(aes_key, plaintext)
    decrypted_text = crypto.decrypt_aes(aes_key, encrypted_text)
    print("AES Encrypted:", encrypted_text)
    print("AES Decrypted:", decrypted_text)

    # Hashing Examples
    hashed_sha3 = crypto.sha3(plaintext)
    print("SHA3-256 Hash:", hashed_sha3)

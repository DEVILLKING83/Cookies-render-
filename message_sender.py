#encrypted:by devil
#decrypt nhi hogi bro key mere yani devil ke pass hai

from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization

# Private key load karein
def load_rsa_private_key():
    with open('private_key.pem', 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
    return private_key

# AES key ko RSA private key se decrypt karein
def rsa_decrypt_aes_key(encrypted_key, private_key):
    aes_key = private_key.decrypt(
        encrypted_key,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return aes_key

# Script ko decrypt karein
def aes_decrypt(encrypted_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext

# Encrypted file ko load karein
with open('message_sender_encrypted.bin', 'rb') as f:
    iv = f.read(16)  # Pehle 16 bytes IV hota hai
    encrypted_key = f.read(256)  # RSA encrypted AES key
    ciphertext = f.read()  # Baaki ciphertext

# Private key load karein
private_key = load_rsa_private_key()

# RSA se AES key ko decrypt karein
aes_key = rsa_decrypt_aes_key(encrypted_key, private_key)

# AES decryption
plaintext = aes_decrypt(ciphertext, aes_key, iv)

# Decrypted script ko wapas save karein
with open('message_sender_decrypted.py', 'wb') as f:
    f.write(plaintext)

print("Decryption successful! Script saved as 'message_sender_decrypted.py'")

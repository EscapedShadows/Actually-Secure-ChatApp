from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class AESCipher:
    def __init__(self, custom_key: str):
        self.custom_key = custom_key

    def derive_key(self, salt: bytes) -> bytes:
        """Derives a 32-byte AES key from the custom key and salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(self.custom_key.encode())

    def encrypt(self, text: str) -> str:
        """Encrypts the text using AES with the custom key."""
        salt = os.urandom(16)
        key = self.derive_key(salt)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(text.encode()) + encryptor.finalize()

        return base64.b64encode(salt + iv + ciphertext).decode()

    def decrypt(self, encrypted_text: str) -> str:
        """Decrypts the AES encrypted text using the custom key."""
        decoded_data = base64.b64decode(encrypted_text.encode())
        salt = decoded_data[:16]
        iv = decoded_data[16:32]
        ciphertext = decoded_data[32:]
        key = self.derive_key(salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode()
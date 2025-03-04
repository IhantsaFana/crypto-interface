import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Chiffrement de César
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26) + ord('a' if char.islower() else 'A'))
            result += new_char
        else:
            result += char
    return result

# Chiffrement de Vigenère
def vigenere_cipher(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            new_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            result += new_char
            key_index += 1
        else:
            result += char
    return result

# Chiffrement et déchiffrement AES
def aes_encrypt(text, key):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv=b'0123456789abcdef')
    encrypted_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + encrypted_bytes).decode()

def aes_decrypt(cipher_text, key):
    data = base64.b64decode(cipher_text)
    iv = data[:16]
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(data[16:]), AES.block_size)
    return decrypted_text.decode()

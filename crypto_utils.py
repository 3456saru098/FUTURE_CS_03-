from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY = get_random_bytes(16)

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        file_data = f.read()

    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)

    encrypted_path = filepath + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    return encrypted_path

def decrypt_file(filepath):
    with open(filepath, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(KEY, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    decrypted_path = filepath.replace('.enc', '')
    with open(decrypted_path, 'wb') as f:
        f.write(data)

    return decrypted_path

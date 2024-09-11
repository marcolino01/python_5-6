from Crypto.Cipher import AES
import base64

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text
# Sapendo che la chiave di cifra è: XXXXIsASecretKey (non conoscete i primi 4 caratteri della chiave)
# e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==
# Trovare la decodifica del messaggio.
enc = "OgJuOYJZT0FDb47DBOkNgA=="
key = "XXXXIsASecretKey"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    dec = decrypt(enc, key)
                    print("La chiave è: ", key, " e la stringa è: ", dec)
                except:
                # continua
                    continue

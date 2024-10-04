
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generating RSA Key Pair
#1-- creazione della coppia di chivi pubblica e privata e esportazione della pubblica
#key_pair = RSA.generate(2048)
#public_key = key_pair.publickey()
#print(public_key.export_key())

#sPriv eè la nostra chiave privata sPub è la nostra chiave pubblica
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAsfyhxQ0yWJ1OeVuyqwxWFMJhsxZ8xEMixjq+a+Gsm6A2N8jO\nKvKbGWP8GS9w6TTBoK4cm7DleYmxh6gZaKb1c0r6uwHA75fT3KI6leCDCGYffwvV\nEKqF1q+L5e1qMGPJV7FrNpnfb/6MDAiIaHJGk8QlKbWoEv8OgWESdb+S9aEGAtC9\nIh9q8W/cM0qA5r50dtv+2hDF6ZMuw5RGbxoXGcR57RuicbaStil7SXBAkDzxu4MI\n7JvJhzaLuBCGU2YMBYCJ2M+pqJ5+rwLVcd0eecR2JNmCOGqdc5Meyfd9IACv04gd\nvlcp3iKNYhydV/ibt3whJfeo/tyAWC7p/49uPQIDAQABAoIBABACJ3CoP7N9ro22\nxCqjSOjEFPJ9HsquOSX4KaFdYl96+PVqf7SYLoAJoKaJQFARWSsBDfyo2/LjAg8v\n/N0PSztL7qI8RaSnFLye8MMDNvXd7Y5JO6gsli4Ziu0qvebNStIy2HBIRbL2g5Uf\nfVlbkeJ/fVIzjwLqYt0bJIRnrymdZAkPkQORNd44JayntqB9A9Bmsx3eJQD+gDFL\nVQ87ZQqsgmfZ7jhRIHF2EwNton6V2qAvBGUv5p2aCX6KP7K6kRAHdqzGw/XuHG8K\n5lOvkFQ+VyU0O5vP4PrLQpnvLux48LJ1Z/nNwIiJiICHaUyUcwhJ2o/DYErUMBsN\n9ZawQPECgYEAyBtm/sS75ffDKZNe8zvvyd2rqHPI/VAUPVBrFY0shW/OQCcSoWAg\n62aOz6uOHh7ZSiNcJpsWKvvoAEd28B4AmcyFiDAaXlSlMOjHaHj8KMABMsRnbVDl\nvewfnG1466G9mrqilN7HNncGZKhcmJviwKeAF6LYbJ5VIxG5yqIdO1kCgYEA47OH\n98YceGIwYhHt+SYDUAGjXKaLwfLgESQja8r/sHP5yJQY8KQrJrAxRB9HDFlbb+pA\nLcUOMctnQJsmrncjZdGuK10Ij8QFXJPRF5suvi/G+zcggYWKcPhARBhyzgzOZkXd\nPgijMo9CKK3w13WAFNYNrScNbVBqvyKJrjj+QYUCgYAi/P+WPknoXNjn9ReeCfXU\nYwj3rD8RY6YWTnBa1VNahYEXoH1WcBtxbX48+28e/x/ZIbOkIGvQ2jjni5dVRrmu\nKp+Sf26s3boAgkMTlkvoyCGtgb/f0kxJV/bzAAUrlh0z57wzsXw9nrQkd3exS1hr\nfR4dg+C5pTmXpyrILm5UCQKBgDzVSR0sQ4zyBqUczyxCOJ5WYbOuFyaQ4cYSlpgE\n2vzkbzZkQql/4rtqVS8zAANPmDs1JUJVJC6vff1nthTkZYOdWl/hchkesKQEJded\nsQZEs2+IUdnouIzn9ht7QKjGCRqPzcT1/8vRNEaz+eVGUhq++VZqWY777hj0fD4c\noekVAoGAT01Y+F7E2VxzG4eBFMsBzQpCJynodEFdNh+xnOECdDloyhbqImK8l7nS\nx4ya9FSrmZbbkzYkH0s8nrX+SVa9+AhJoDaBXmA+0waRtgaWQCLIfdWYZF/gS66y\nQ5ubJDDkaQ93nQtcT3pQ9f/8GYkwTDPLvdB3IhAdfQCQKGGbMAM=\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsfyhxQ0yWJ1OeVuyqwxW\nFMJhsxZ8xEMixjq+a+Gsm6A2N8jOKvKbGWP8GS9w6TTBoK4cm7DleYmxh6gZaKb1\nc0r6uwHA75fT3KI6leCDCGYffwvVEKqF1q+L5e1qMGPJV7FrNpnfb/6MDAiIaHJG\nk8QlKbWoEv8OgWESdb+S9aEGAtC9Ih9q8W/cM0qA5r50dtv+2hDF6ZMuw5RGbxoX\nGcR57RuicbaStil7SXBAkDzxu4MI7JvJhzaLuBCGU2YMBYCJ2M+pqJ5+rwLVcd0e\necR2JNmCOGqdc5Meyfd9IACv04gdvlcp3iKNYhydV/ibt3whJfeo/tyAWC7p/49u\nPQIDAQAB\n-----END PUBLIC KEY-----"
# ricreiamo le chiavi a partire da queste due stringhe ,dove sPubCollega è la chiave pubblica del nostra collega da dove decripteremo il messaggio decriptato
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
sPubCollega = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAodRTArmVwLiEj9KGI0In\nHWTUM4N7jru3qfClugLG3RbueugS/xTup4FzbUUIT7AQFwU4Y+6riBjhImKiVqtr\n7f4msIyuufyT3u3/Tta3Y8EwEh7jRMDWgIKu1OZE5kQBIig7LAW9sKpazOeyLCgQ\nAEg6yWQSPR3TF6Y5/9Yhy8YP+oNsAk2SiVFJNadgfVX49QRJhn2/IEtppeRZDyMX\npWNkVCGRDGBaLM/jU4od8hmmXCXYpKKNUUY6U0rk8emK3b6J/xad5UoKcPzGpSg6\nGpam0NeMLe5FmtGahCGBw/6GVX/UWtt7Rtr1YxaNzABMD5QWFle5tuc9ogKTBHcg\nEwIDAQAB\n-----END PUBLIC KEY-----"


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
#message = "This is a secret message"
#encrypted_message = encrypt_message(message, public_key)
#decrypted_message = decrypt_message(encrypted_message, key_pair)

#print("Original Message:", message)
#print("Encrypted Message:", encrypted_message)
#print("Decrypted Message:", decrypted_message)



# Per importare una chiave pubblica
#keyDER = base64.b64decode(public_key)
#seq = base64.asn1.DerSequence()
#seq.decode(keyDER)
#keyPub = RSA.construct((seq[0], seq[1]))


#key_pair = RSA.generate(2048)
#print(key_pair.export_key())
#public_key = key_pair.public_key()
#print(public_key.export_key())

# 3 --scrittura del messaggio cifrato da mandare al collega tramite la sua chiave pubblica
public_key_collega = RSA.import_key(sPubCollega)
message = "Questo è i mio messaggio segreto..."
encrypted_message = encrypt_message(message, public_key_collega)
#print("Encrypted Message:", encrypted_message)

# 4 --tramite cifrato noi abbiamo il messagio del collega scritto tramite la nostra chiave e con la funzione decrypt_message riconvertiremo il messaggio 
cifrato = "Tljnw+G4F877sMK8MoKjLfWDfgE3BBEulYZc2zriQN3X+mIARIm1f5A4zuFTvz+e9kNQ1s7JoKyZjo/0wg2AL/qXf5Tr/P01oiOTv+pjk7T+5wYiEalBjMVL1B2RFDn/29r+oXjitSFAsTf3Ist4KrHlYtmDBqu94aneMfmxzikDrP9Ck0TobIu8JjB0LndaMLT7qQPgk8ud7qRwbtzzO6XleiF17XaAKincr5tvBRYQZaRahEwOQrtjfvC8u3Iu1QCB5ImEzfkZYc8207tB5ywSIYO1rqEGhTr3R7JYArq7A5Zeg5Vmg1x2Qbna/iVyfT+m52C2dtTT+I2XPb0yyQ=="
decifrato = decrypt_message(cifrato, key_pair)
print("Il messaggio decifrato: ", decifrato)
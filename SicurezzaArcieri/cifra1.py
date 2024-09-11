import base64

riga = input("inserire una stringa:")
print("Riga letta : ", riga)

riga_b64 = base64.b64encode(riga.encode("utf-8"))
print("Riga base64: ",riga_b64.decode("utf-8"))

riga_decoded = base64.b64decode(riga_b64)
print("Riga decoded: ",riga_decoded.decode("utf-8"))




import subprocess
import os
import platform
import sys


sFile = input ("inserisci il nome del file")
#divido il nome del file
sFileb64 = os.path.splitext(sFile)[0]
#alla nome aggiungo l'ext b64
sFileb64 = sFileb64 + "b.64"
print(sFile)
print(sFileb64)
print(platform.system())
sys.exit()

#crea il file image1.jpeg
subprocess.run(["cp", sFile,"./image1.jpeg"])
#prende image1.jpeg e lo trasforma image2.b64
subprocess.run(["bash", "./creajson.sh"])
#restituisce il nomedelfile.b64
subprocess.run(["cp","./image2.b64", sFileb64])



subprocess.run(["cp", sFile,"./image1.jpeg"])
sOper = platform.platform()
#per farlo funzionare su altri sistemi operativi
if sOper.startswith("Linux"):
    subprocess.run(["bash", "./comando_l.sh"])
if sOper.startswith("macOs"):
    subprocess.run(["bash", "./comando_m.sh"])

#restituisce il nomedelfile.b64
subprocess.run(["cp","./image2.b64", sFileb64])
import time
import sys
sys.stdout = open("./file_per_le_print.txt","w+")
i=1

while i < 10:
    sys.stdout.flush()       #stdout è un puntatore ad un file 
    print("mmmmmy app")
    time.sleep(3)
    i+=1
sys.stdout.close()



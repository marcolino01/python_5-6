import os
sRoot = input("Inserisci la directory dove cercare:")
sParola = input("Inserisci la parola da cercare:")
sOutDir = input("Inserisci la directory dove mettere i file trovati:")


for root, ListDir, ListFiles in os.walk(sRoot): #os.walk torna la root il nome delle direcory e i files
    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} file")

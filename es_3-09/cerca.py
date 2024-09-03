import os
import PyPDF2 #pip3 PyPDF2 da terminale per scaricarlo


def CercaParolaInNomeFile(sFile,sParola):
    sFile1 = sFile.lower()
    sParola1 = sParola.lower()
    iRet = sFile1.find(sParola1)  #find torna sempre -1 se non trova la parola
    if iRet >= 0:
        return True
    else:
        return False
    
def CercaParolaInFileTxt(sPathFile, sParola):
    with open(sPathFile, "r") as file:
        sLine = file.readline()
        while(len(sLine) > 0):
           iRet = sLine.lower().find(sParola.lower())
           if iRet >= 0:
               return True
           else:
               sLine = file.readline()
               print("Riga letta:"+ sLine)
    return False


def CercaParolaInFilePdf(sPathFile, sParola):
    iRet = 0
    object = PyPDF2.PdfReader(sPathFile)    #lettura del file pdf
    numPages = len(object.pages)     #numero delle pagine del file PDF
    print(f"Il file {sPathFile} contiene {numPages} pagine")
    for i in range (0,numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        iRet = text.lower().find(sParola.lower())
        if iRet >= 0:
            return True
    return False

    



def CercaParolaInContenutoFile(sPathFile, sParola):
    bRet = False
    sFileName, sFileExt = os.path.splitext(sPathFile) #permette di seperare il nome file dalla sua estensione
    if(sFileExt.lower()==".txt"):
        bRet = CercaParolaInFileTxt(sPathFile, sParola)
    if(sFileExt.lower()==".pdf"):
        bRet = CercaParolaInFilePdf(sPathFile, sParola)
    return bRet



sRoot = input("Inserisci la directory dove cercare:")
sParola = input("Inserisci la parola da cercare:")
sOutDir = input("Inserisci la directory dove mettere i file trovati:")

bRet = False
for root, ListDir, ListFiles in os.walk(sRoot): #os.walk torna la root il nome delle direcory e i files
    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} file")
    for file in ListFiles:
        #print(f"Devo cercare {sParola} in {file}")
        bRet = CercaParolaInNomeFile(file, sParola)
        if bRet == True:
            print(f"Trovata parola in file {file}")
        else:
            print(f"Prova a cercare nel file")
            sFilePathCompleto = os.path.join(root,file) #os.path.join viene utilizzato principalmente per costruire percorsi di file o directory in modo sicuro, soprattutto in applicazioni che devono funzionare su più sistemi operativi
            bRet = CercaParolaInContenutoFile(sFilePathCompleto,sParola)
            if bRet == True:
                print(f"Trovata la parola in file {file}")

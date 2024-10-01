mylist_1= "['mario', 'gino', 'lucrezia']"
mylist_2= ['mario','gino','lucrezia']

def Deserializza(stringa):
    lista = stringa.split(",")
    return lista

def Serializza(lista):
    lista = str(lista)
    return lista

if Deserializza(mylist_1) == mylist_2:
    print("Procedura di deserializzazione costruita correttamente")
else:
    print("Procedura di deserializzazione NON costruita correttamente")


if Serializza(mylist_2) == mylist_1:
    print ("Procedura di serializzazione costruita correttamente")
else:
    print ("Procedura di serializzazione NON costruita correttamente")




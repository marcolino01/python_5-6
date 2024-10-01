import sys, json

mydict1 = {"brand": "Ford",
"electric": False,
"year": 1964,
"colors" : ["red", "white", "blue"]
}

mydict2 = "{ 'brand': 'Ford'," + \
"'electric': False,'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

str1 = json.dumps(mydict1)



def Serialize(dict, file_path)-> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(dict, file)
        return True
    except Exception as e:
        print(f"Errore durante la serializzazione : {e}")
        return False


def Deserialize(file_path)-> dict:
    try:
        with open(file_path, 'r') as file:
            dict = json.load(file)
        return dict
    except Exception as e:
        print(f"Errore durante la deserializzazione: {e}")
        return None



print(Serialize(mydict1, mydict2))
print(Deserialize(mydict2))
      
resultado=[]
import csv

with open('datos1006.csv', 'r', encoding='utf-8') as entrada:
    contenido= csv.DictReader(entrada)
    for fila in contenido:
        nom= fila ['nombre']
        tel= fila ['telefono']
        print(nom, 'tiene el numero:', tel)
        x=len(tel)
        
        diccionario={
                    'nombre': nom,
                    'fono': tel,
                    'codigo de area':x
                    }
        
        resultado.append(diccionario)
        
import json
nombre_archivo= 'd:/leonor/telefonos.json'

with open (nombre_archivo, 'w', encoding='utf-8') as salida:
    json.dump(resultado, salida, indent=-1)
    
    
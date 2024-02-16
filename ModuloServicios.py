import os
import json


def validarIden(identidad):
    if identidad == "":
        return False
    try:
        identidad = int(identidad) 
        if identidad > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def inscripciones_servicios():
    
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    estado = 'en venta'
    nuevo_servicio = {}
    identidad = input('Ingresa el número de identidad del usuario: ')
    nuevo_servicio['identidad'] = int(identidad)
    nuevo_servicio['nombre'] = input('Ingresa el nombre del servicio: ')
    nuevo_servicio['estado'] = estado
    
    datos_json['datos']['servicios'].append(nuevo_servicio)
    with open(ruta,'w') as archivo:
        json.dump(datos_json,archivo,indent=4)
      

def actualizar_servicios():
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    campers = datos_json["datos"]["servicios"]
    identidad = input("Ingresa el serial del servicio: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El serial debe ser valido.')
    for camper in campers:
        if camper['identidad'] == identidad:
            preguntas = {
                'identidad': ('Ingresa el serial del servicio: ', validarIden),
                'nombre': ('Ingresa el nombre del servicio: ', None),
                'estado': ('Ingrese el estado del usuario: ', None)
            }
    else:
        print(f'No se encontró ningún serial {identidad}')
    with open(ruta, 'w') as archivo:
        json.dump(datos_json, archivo, indent=4)


def buscar_servicios():
    identidad = input("Ingresa el serial de servicio: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El serial no es correcto.')
    return identidad

def mostrar_servicios(ruta):
  with open(ruta, 'r') as archivo:
    datos_json = json.load(archivo)
  usuario = datos_json["datos"]["servicios"]
  for usuarios in usuario:
    print(f"Id: {usuarios['identidad']}")
    print(f"Nombre: {usuarios['nombre']}")
    print()
    
#inscripciones()
#actualizar_campers()
#buscar()
#mostrar_datos()


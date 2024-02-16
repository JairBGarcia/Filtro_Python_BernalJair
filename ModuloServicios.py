import os
import json



def inscripciones_servicios():
    
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    
    nuevo_servicio = {}
    identidad = input('Ingresa el número de identidad del usuario: ')
    nuevo_servicio['identidad'] = int(identidad)
    nuevo_servicio['nombre'] = input('Ingresa el nombre del servicio: ')
    nuevo_servicio['apellido1'] = input('Ingrese el primer apellido del usuario: ')
    nuevo_servicio['direccion'] = input('Ingrese la direccion del usuario: ')
    nuevo_servicio['edad'] = int(input('Ingrese la edad: '))
    nuevo_servicio['celular'] = int(input('Ingrese el numero de telefono '))
    
    
    datos_json['datos']['servicios'].append(nuevo_servicio)
    with open(ruta,'w') as archivo:
        json.dump(datos_json,archivo,indent=4)
      

def actualizar_servicios():
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    campers = datos_json["datos"]["servicios"]
    identidad = input("Ingresa el id del Camper que quieras actualizar: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El id del Camper debe ser un número válido.')
    for camper in campers:
        if camper['identidad'] == identidad:
            preguntas = {
                'identidad': ('Ingresa el número de identidad del ususario: ', validarIden),
                'nombre': ('Ingresa el nombre del usuario: ', None),
                'apellido1': ('Ingrese el primer apellido del usuario: ', None),
                'direccion': ('Ingrese la direccion del usuario: ', None),
                'edad': ('Ingrese la edad del usuario: ', validarEdad),
                'celular': ('Ingresa el número de celular del usuario: ', validarIden),
                'estado': ('Ingrese el estado del usuario: ', None)
            }
            for clave, valor in preguntas.items():
                mensaje, validacion = valor
                nuevo_dato = input(mensaje)
                if validacion:
                    while not validacion(nuevo_dato):
                        print(f'El {clave} debe ser válido.')
                        nuevo_dato = input(mensaje)
                if clave in ['identidad', 'edad', 'celular_acudiente', 'celular', 'telefono']:
                    nuevo_dato = int(nuevo_dato)
                camper[clave] = nuevo_dato
            print(f'Se ha actualizado el camper con id {identidad}')
            break
    else:
        print(f'No se encontró ningún camper con id {identidad}')
    with open(ruta, 'w') as archivo:
        json.dump(datos_json, archivo, indent=4)


def buscar_servicios():
    identidad = input("Ingresa el id del Camper que quieras buscar: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El id del Camper debe ser un número válido.')
    return identidad

def mostrar_servicios(ruta):
  with open(ruta, 'r') as archivo:
    datos_json = json.load(archivo)
  usuario = datos_json["datos"]["usuarios"]
  for usuarios in usuario:
    print(f"Id: {usuarios['identidad']}")
    print(f"Nombre: {usuarios['nombre']}")
    print(f"Apellido 1: {usuarios['apellido1']}")
    print(f"Dirección: {usuarios['direccion']}")
    print(f"Edad: {usuarios['edad']}")
    print(f"Celular: {usuarios['celular']}")
    print()
    
#inscripciones()
#actualizar_campers()
#buscar()
#mostrar_datos()


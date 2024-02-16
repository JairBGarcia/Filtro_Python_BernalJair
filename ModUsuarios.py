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

def validarEdad(edad):
    try:
        edad = int(edad)
        if 16 <= edad <= 28:
            return True
        else:
            return False
    except ValueError:
        return False

def inscripciones():
    
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    estado = 'Nuevo'
    nueva_inscripcion = {}
    identidad = input('Ingresa el número de identidad del usuario: ')
    while not validarIden(identidad):
        print('El número de identidad debe ser un entero positivo.')
        identidad = input('Ingresa el número de identidad del usuario: ')
    nueva_inscripcion['identidad'] = int(identidad)
    nueva_inscripcion['nombre'] = input('Ingresa el nombre del usuario: ')
    nueva_inscripcion['apellido1'] = input('Ingrese el primer apellido del usuario: ')
    nueva_inscripcion['direccion'] = input('Ingrese la direccion del usuario: ')
    nueva_inscripcion['edad'] = int(input('Ingrese la edad: '))
    nueva_inscripcion['celular'] = int(input('Ingrese el numero de telefono '))
    nueva_inscripcion['estado'] = estado
    
    
    datos_json['datos']['usuarios'].append(nueva_inscripcion)
    with open(ruta,'w') as archivo:
        json.dump(datos_json,archivo,indent=4)
      

def actualizar_usuarios():
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    campers = datos_json["datos"]["usuarios"]
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


def buscar():
    identidad = input("Ingresa el id del Camper que quieras buscar: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El id del Camper debe ser un número válido.')
    return identidad

def mostrar_datos(ruta):
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


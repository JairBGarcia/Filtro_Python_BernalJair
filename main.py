import os
from ModuloServicios import leer_trainer, Añadir_trainer, Actualizar_trainer, Eliminar_trainer

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(options):
    while True:
        user_input = input("Seleccione una opción: ").strip()
        if user_input in options:
            return user_input
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def menu_campers():
    print("Estás en el menú de Campers.")

from ModUsuarios import inscripciones
from ModUsuarios import actualizar_usuarios
from ModUsuarios import buscar
from ModUsuarios import mostrar_datos

def menu_inscripcionesCampers():
    
    clear_console()
    while True:
        print("Menu de Usuarios:")
        print("1. Añadir usuario")
        print("2. Actualizar Campers")
        print("3. Buscar")
        print("4. Mostrar Datos")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Inscripciones de Campers.")
            inscripciones()
        elif user_input == "2":
            print("Accediste a Actualizar Campers.")
            actualizar_usuarios()
        elif user_input == "3":
            print("Accediste a Buscar.")
            buscar()
        elif user_input == "4":
            print("Accediste a Mostrar Datos.")
            mostrar_datos()
        elif user_input == "5":
            print("Volviendo al menú coordinador.")
            break

def leer_trainers():
    print("Accediste a Leer Trainers.")

def añadir_trainers():
    print("Accediste a Añadir Trainers.")

def actualizar_trainers():
    print("Accediste a Actualizar Trainers.")

def eliminar_trainers():
    print("Accediste a Eliminar Trainers.")
from ModuloServicios import inscripciones_servicios
from ModuloServicios import actualizar_servicios
from ModuloServicios import buscar_servicios
from ModuloServicios import mostrar_servicios
def menu_trainers():
    clear_console()
    while True:
        print("1. Añadir Servicio")
        print("2. Actualizar Servicio")
        print("3. Buscar servicio")
        print("4. Mostrar servicio")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            inscripciones_servicios()
        elif user_input == "2":
            actualizar_servicios()
        elif user_input == "3":
            buscar_servicios()
        elif user_input == "4":
            mostrar_servicios()
        elif user_input == "5":
            print("Volviendo sal menú principal.")
            break



from ModuloReportes import usuario_antiguo
from ModuloReportes import usuario_nuevo


def menu_reportes():
    
    clear_console()
    while True:
        print("Menu de Reportes:")
        print("1. Usuarios Nuevos")
        print("2. Usuarios Antiguos")
        print("3. Servicios")
        print("4. Volver")
        

        user_input = get_valid_input(["1", "2", "3", "4", "5","6","7"])
        if user_input == "1":
            print("Accediste a usuario Nuevos.")
            usuario_nuevo()
        elif user_input == "2":
            print("Accediste a Usuario Antiguo.")
            usuario_antiguo()
        elif user_input == "3":
            print("Accediste a Usuario Antiguo.")
            usuario_antiguo()
        elif user_input == "4":
            print('Volviendo al menu coordinador')
            break

def actualizar_nota_y_rendimiento():
    print("Accediste a Actualizar Nota y Rendimiento.")


def configurar_ruta():
    print("Accediste a Configurar Ruta.")


def menu_principal():
    clear_console()
    while True:
        print('----------------------------------------')
        print("--  Bienvenido al sistema de gestión  --")
        print('----------------------------------------')
        print('')
        print("1. Menu usuarios")
        print("2. Menú Servicios")
        print("3. Menu Gestiones")
        print("4. Salir")

        user_input = get_valid_input(["1", "2", "3", "4"])
        if user_input == "4":
            print("¡Hasta luego!")
            break
        elif user_input == "1":
            print('Ingresa la siguiente informacion para hacer la busqueda')
            menu_inscripcionesCampers()
        elif user_input == "2":
            menu_trainers()
        elif user_input == "3":
            menu_reportes()

if __name__ == "__main__":
    menu_principal()

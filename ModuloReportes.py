def usuario_nuevo():
    import json
    
    with open('InscritosCampers.json','r') as archivo:
        data = json.load(archivo)
        usuarios = data['datos']['usuarios']
        print('Usuarios recien ingresados')
        for i in usuarios:
            if i['estado'] == 'nuevo':
                print(i)
        
#camperEstadoInscrito()

def usuario_antiguo():
    import json
    with open('InscritosCampers.json','r') as archivo:
        data = json.load(archivo)
        usuarios = data['datos']['usuarios']
        print('usuarios antiguos')
        for i in usuarios:
            if i['estado'] == 'antiguo' 'Antiguo':
                print(i)

#camperEstadoAprobado()


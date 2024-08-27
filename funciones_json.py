#Modulo correspondiente a todas las funciones relacionadas a la biblioteca JSON.
PATH = './Labo1_SP_Python/configs.json'
PATH_TURNOS = './Labo1_SP_Python/turnos.json'
PATH_PACIENTES = './Labo1_SP_Python/pacientes.json'

import json
from paciente import Paciente

def cargar_pacientes_json () -> list:
    '''
    Funcion que se encarga de extraer los pacientes del configs.json si es que hay 
    y calcular el valor del ID auto incremental en base a cuantos haya.
    No recibe nada y retorna la lista de pacientes y el ID auto incremental.
    '''
    id_auto_incremental_paciente = 0
    lista_pacientes = []
    
    try:
        with open (PATH, 'r', encoding='utf-8') as file:
            diccionarios = json.load(file)
    except FileNotFoundError: 
            print("El archivo no se pudo encontrar o abrir.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    
    pacientes = diccionarios.get("pacientes", [])

    if pacientes:
        for diccionario in pacientes:
            id_auto_incremental_paciente += 1
            paciente = Paciente(id_auto_incremental_paciente, diccionario)
            lista_pacientes.append(paciente)
    else:
        print("No hay pacientes registrados en el archivo.")
        
    return lista_pacientes, id_auto_incremental_paciente

def actualizar_json_pacientes (lista_pacientes: list):
    '''
    Funcion que se encarga de actualizar el archivo config.json con la lista de pacientes.
    Resumidamente mantiene las claves de especialidades y obras sociales y solo actualiza "pacientes".
    Itera la lista de pacientes y crea el diccionario para luego anexarlo siempre cuando la lista no esté vacía.
    Recibe la lista de pacientes y no retorna nada.
    '''
    pacientes_json = []
    data_json = {}
    
    #Primero paso los pacientes a diccionarios y luego anexarlos
    if lista_pacientes:
        for paciente in lista_pacientes:
            paciente_dict= {
                "nombre": paciente.get_nombre(),
                "apellido": paciente.get_apellido(),
                "dni": paciente.get_dni(),
                "edad": paciente.get_edad(),
                "fecha_registro": paciente.get_fecha_registro(),
                "obra_social": paciente.get_obra_social()
            }
            pacientes_json.append(paciente_dict)
        
        try:
            with open (PATH, 'r', encoding='utf-8') as file:
                data_json = json.load(file)
        except FileNotFoundError: 
            print("El archivo no se pudo encontrar o abrir.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
        
        #Acá sobrescribo los diccionarios
        data_json['pacientes'] = pacientes_json
        
        try:
            with open (PATH, 'w', encoding='utf-8') as file:
                json.dump(data_json, file, indent=4)
        except FileNotFoundError: 
            print("El archivo no se pudo encontrar o abrir.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            
    else:
        print("La lista está vacía...")
        
def crear_json_turnos (lista_turnos: list):
    '''
    Funcion que se encarga de crear un archivo JSON para los turnos.
    Recibe la lista de turnos y se fija que no esté vacía para poder crear el archivo,
    caso contrario lo informará.
    Recibe la lista de turnos.
    '''

    turnos_json = []
    data_json = {}

    if lista_turnos:
        for turno in lista_turnos:
            turnos_dict = {
                "id_turno": turno.get_id_turno(),
                "id_paciente": turno.get_id_paciente(),
                "especialidad": turno.get_especialidad(),
                "monto": turno.get_monto(),
                "estado_turno": turno.get_estado_turno()
            }
            turnos_json.append(turnos_dict)
        
        data_json['turnos'] = turnos_json

        try:
            with open (PATH_TURNOS, 'w+', encoding='utf-8') as file:
                json.dump(data_json, file, indent=4)
            print("Archivo de turnos creado.")
        except FileNotFoundError: 
            print("El archivo no se pudo encontrar o abrir.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
    else:
        print("La lista está vacía...")

def crear_json_pacientes(lista_pacientes:list):
    '''
    Funcion que se encarga de crear un archivo JSON para los pacientes.
    Recibe la lista de pacientes y se fija que no esté vacía para poder crear el archivo,
    caso contrario lo informará.
    Recibe la lista de pacientes.
    '''

    pacientes_json = []
    data_json = {}
    
    #Primero paso los pacientes a diccionarios y luego anexarlos
    if lista_pacientes:
        for paciente in lista_pacientes:
            paciente_dict= {
                "nombre": paciente.get_nombre(),
                "apellido": paciente.get_apellido(),
                "dni": paciente.get_dni(),
                "edad": paciente.get_edad(),
                "fecha_registro": paciente.get_fecha_registro(),
                "obra_social": paciente.get_obra_social()
            }
            pacientes_json.append(paciente_dict)
        
        #Acá creo el diccionario
        data_json['pacientes'] = pacientes_json
        
        try:
            with open (PATH_PACIENTES, 'w', encoding='utf-8') as file:
                json.dump(data_json, file, indent=4)
        except FileNotFoundError: 
            print("El archivo no se pudo encontrar o abrir.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            
    else:
        print("La lista está vacía...")
                         

def extraer_especialidades () -> list:
    '''
    Funcion que se encarga de extraer las especialidades medicas del JSON.
    No recibe nada y retorna la lista de especialidades.
    '''
    especialidades = []

    try:
        with open (PATH, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
            especialidades = data_json.get("especialidades", [])
    except FileNotFoundError: 
        print("El archivo no se pudo encontrar o abrir.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    return especialidades

def extraer_obras () -> list:
    '''
    Funcion que se encarga de extraer las obras sociales disponibles del JSON.
    No recibe nada y retorna la lista de obras sociales.
    '''
    obras_sociales = []

    try:
        with open (PATH, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
            obras_sociales = data_json.get("obras_sociales", [])
    except FileNotFoundError: 
        print("El archivo no se pudo encontrar o abrir.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    return obras_sociales
